import json
import logging
import random
import os
import env
import avalon_crypto_utils.signature as signature
from src.utilities.worker_utilities import tamper_request
from error_code.error_status import ReceiptCreateStatus
import avalon_crypto_utils.crypto_utility as crypto_utility
from avalon_sdk.work_order_receipt.work_order_receipt \
    import WorkOrderReceiptRequest
import src.utilities.worker_utilities as wconfig
logger = logging.getLogger(__name__)


class WorkOrderReceiptCreate():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0",
                       "method": "WorkOrderReceiptCreate", "id": 6}
        self.params_obj = {}
        self.sig_obj = signature.ClientSignature()
        self.SIGNING_ALGORITHM = "SECP256K1"
        self.HASHING_ALGORITHM = "SHA-256"
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "work_order_create_receipt"

    def add_json_values(self, input_json_params,
                        worker_obj, private_key, tamper, wo_submit):
        """
        This functions should form the param inputs for WorkOrderReceiptCreate listener request
        :param input_json_params: Input json as per EEA spec
        :param worker_obj: worker object
        :param private_key: signature created by the Enclave
        :param tamper: tamper request
        :param wo_submit: workOrderSubmit response
        """
        self.private_key = private_key
        self.worker_obj = worker_obj
        # logger.info("------ Loaded string data: ABCDEFGHIJKLMNOP
        # %s ------2. %s\n", input_json_temp,  type(wo_submit))
        input_json_temp = wo_submit["params"]
        wo_request_hash = self.sig_obj.calculate_request_hash(input_json_temp)
        final_hash_str = crypto_utility.byte_array_to_base64(wo_request_hash)
        input_params_list = input_json_params["params"].keys()
        config_yaml = wconfig.read_yaml(__file__, worker_obj, input_json_temp)
        config_yaml["workOrderId"] = wo_submit["params"]["workOrderId"]
        config_yaml["workerServiceId"] = wo_submit["params"]["workerId"]
        for c_key, c_val in config_yaml.items():
            if c_key in input_params_list:
                value = input_json_temp[c_key] if input_json_temp.get(
                    c_key, "") != "" else c_val
                wconfig.set_parameter(self.params_obj, c_key, value)

        wo_receipt_str = (self.params_obj["workOrderId"] +
                          self.params_obj["workerServiceId"] +
                          self.params_obj["workerId"] +
                          self.params_obj["requesterId"] +
                          str(self.params_obj["receiptCreateStatus"]) +
                          final_hash_str +
                          self.params_obj["requesterGeneratedNonce"])

        wo_receipt_bytes = bytes(wo_receipt_str, "UTF-8")
        wo_receipt_hash = crypto_utility.compute_message_hash(wo_receipt_bytes)
        status, wo_receipt_sign = self.sig_obj.generate_signature(
            wo_receipt_hash,
            private_key
        )
        if "workOrderRequestHash" in input_params_list:
            wconfig.set_parameter(
                self.params_obj,
                "workOrderRequestHash",
                final_hash_str)

        if "requesterSignature" in input_params_list:
            wconfig.set_parameter(
                self.params_obj,
                "requesterSignature",
                wo_receipt_sign)

    def compute_signature(self, tamper):
        """
        This function is used to compute the requester signature
        :param tamper: tamper_request
        :return: JSON with update tampered request
        """
        self._compute_requester_signature()

        input_after_sign = wconfig.to_string(self)
        tamper_instance = 'after_sign'
        tampered_request = tamper_request(input_after_sign, tamper_instance,
                                          tamper)
        return tampered_request

    def _compute_requester_signature(self):
        """
        Set verifyingKey work order parameter
        """
        self.public_key = crypto_utility.get_verifying_key(self.private_key)
        self.params_obj["receiptVerificationKey"] = self.public_key

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        """
        This function forms the request for WorkOrderReceiptCreate as per EEA spec
        :param input_json: Input JSON as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: response received from WorkOrderSubmit request
        :return: Fully formed JSON which can be submitted to listener
        """
        if input_json is None:
            with open(os.path.join(
                    env.work_order_receipt,
                    "work_order_receipt.json"), "r") as file:
                input_json = file.read().rstrip('\n')

        logger.info("***Pre test*****\n%s\n", pre_test_response)
        logger.info("***Input json*****\n%s\n", input_json)
        # private_key of client
        private_key = crypto_utility.generate_signing_keys()
        self.add_json_values(
            input_json, worker_obj, private_key,
            self.tamper, pre_test_response)
        input_work_order = self.compute_signature(self.tamper)
        logger.info('''Compute Signature complete \n''')
        final_json = json.loads(input_work_order)
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        """
        This functions forms the input for WorkOrderReceiptCreate SDK function
        :param input_json: containing input data as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: Response received from WorkOrderSubmit request
        :return: dictionary containing following fields and values associated with them
            {"workOrderId": "",
             "workerServiceId": "",
             "workerId": "",
             "requesterId": "",
             "receiptCreateStatus": ,
             "workOrderRequestHash": "",
             "requesterGeneratedNonce": "",
             "signatureRules": "",
             "receiptVerificationKey": "",
             "requesterSignature":""}
        """
        logger.info("***Pre test*****\n%s\n", pre_test_response)
        logger.info("***Input json*****\n%s\n", input_json)
        jrpc_req_id = input_json["id"]
        client_private_key = crypto_utility.generate_signing_keys()
        wo_request = json.loads(pre_test_response.to_jrpc_string(jrpc_req_id))
        wo_receipt_request_obj = WorkOrderReceiptRequest()
        wo_create_receipt = wo_receipt_request_obj.create_receipt(
            wo_request,
            ReceiptCreateStatus.PENDING.value,
            client_private_key
        )
        logger.info("Work order create receipt request : {} \n \n ".format(
            json.dumps(wo_create_receipt, indent=4)
        ))

        return wo_create_receipt
