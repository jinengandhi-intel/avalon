import json
import logging
import random
import os
import globals
import avalon_crypto_utils.crypto.crypto as crypto
import avalon_crypto_utils.signature as signature
from src.utilities.tamper_utility import tamper_request
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

        self.private_key = private_key
        self.worker_obj = worker_obj
        # logger.info("------ Loaded string data: ABCDEFGHIJKLMNOP
        # %s ------2. %s\n", input_json_temp,  type(wo_submit))
        final_hash_str = self.sig_obj.calculate_request_hash(wo_submit)
        input_json_temp = wo_submit["params"]
        input_params_list = input_json_params["params"].keys()
        config_yaml = wconfig.read_config(__file__, worker_obj, input_json_temp)
        config_yaml["workOrderId"] = wo_submit["params"]["workOrderId"]
        config_yaml["workerServiceId"] = wo_submit["params"]["workerId"]
        for c_key, c_val in config_yaml.items():
            if c_key in input_params_list:
                value = input_json_temp[c_key] if input_json_temp.get(c_key, "") != "" else c_val
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
            wconfig.set_parameter(self.params_obj, "workOrderRequestHash", final_hash_str)

        if "requesterSignature" in input_params_list:
            wconfig.set_parameter(self.params_obj, "requesterSignature", wo_receipt_sign)

    def compute_signature(self, tamper):

        self._compute_requester_signature()

        input_after_sign = wconfig.to_string(self)
        tamper_instance = 'after_sign'
        tampered_request = tamper_request(input_after_sign, tamper_instance,
                                          tamper)
        return tampered_request

    def _compute_requester_signature(self):
        self.public_key = crypto_utility.get_verifying_key(self.private_key)
        self.params_obj["receiptVerificationKey"] = self.public_key

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        if input_json is None:
            with open(os.path.join(
                    globals.work_order_receipt,
                    "work_order_receipt.json"), "r") as file:
                input_json = file.read().rstrip('\n')
        #input_json = json.loads(input_json)
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
