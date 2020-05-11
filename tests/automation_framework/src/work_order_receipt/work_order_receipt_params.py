import json
import logging
import random
import os
import globals
import avalon_crypto_utils.crypto.crypto as crypto
import avalon_crypto_utils.signature as signature
from src.utilities.tamper_utility import tamper_request
import avalon_crypto_utils.crypto_utility as enclave_helper
from error_code.error_status import ReceiptCreateStatus
import avalon_crypto_utils.crypto_utility as crypto_utility
from avalon_sdk.work_order_receipt.work_order_receipt \
    import WorkOrderReceiptRequest
logger = logging.getLogger(__name__)


class WorkOrderReceiptCreate():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0",
                       "method": "WorkOrderReceiptCreate", "id": 3}
        self.params_obj = {}
        self.sig_obj = signature.ClientSignature()
        self.SIGNING_ALGORITHM = "SECP256K1"
        self.HASHING_ALGORITHM = "SHA-256"
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "work_order_create_receipt"
        # self.session_key = self.generate_key()
        # self.session_iv = self.generate_iv()

    def add_json_values(self, input_json_temp,
                        worker_obj, private_key, tamper, wo_submit):

        self.private_key = private_key
        self.worker_obj = worker_obj
        input_request_wo_submit = json.loads(wo_submit)
        # logger.info("------ Loaded string data: ABCDEFGHIJKLMNOP
        # %s ------2. %s\n", input_json_temp,  type(wo_submit))
        final_hash_str = \
            self.sig_obj.calculate_request_hash(input_request_wo_submit)
        nonce = None
        requester_nonce = nonce
        if nonce is None:
            requester_nonce = str(random.randint(1, 10 ** 10))

        # public_key =  signing_key.GetPublicKey().Serialize()
        input_json_temp = input_json_temp["params"]

        wo_receipt_str = (input_json_temp["workOrderId"] +
                          input_json_temp["workerServiceId"] +
                          input_json_temp["workerId"] +
                          input_json_temp["requesterId"] +
                          str(input_json_temp["receiptCreateStatus"]) +
                          input_json_temp["workOrderRequestHash"] +
                          input_json_temp["requesterGeneratedNonce"])

        wo_receipt_bytes = bytes(wo_receipt_str, "UTF-8")
        wo_receipt_hash = crypto.compute_message_hash(wo_receipt_bytes)
        status, wo_receipt_sign = self.sig_obj.generate_signature(
            wo_receipt_hash,
            private_key
        )

        input_params_list = input_json_temp.keys()
        if "workOrderId" in input_params_list:
            # if input_json_temp["workOrderId"] != "" :
            self.set_work_order_id(input_request_wo_submit
                                   ["params"]["workOrderId"])
            # else :
            #    work_order_id = hex(random.randint(1, 2**64 -1))
            #    self.set_work_order_id(work_order_id)

        if "workerId" in input_params_list:
            if input_json_temp["workerId"] != "" or \
                    input_json_temp["workerServiceId"] != "":
                self.set_worker_id(input_json_temp["workerId"])
                self.set_worker_id(input_json_temp["workerServiceId"])
            else:
                self.set_worker_id(worker_obj.worker_id)

        if "requesterId" in input_params_list:
            if input_json_temp["requesterId"] != "":
                self.set_requester_id(input_json_temp["requesterId"])
            else:
                self.set_requester_id("0x3456")

        if "signatureRules" in input_params_list:
            if input_json_temp["signatureRules"] != "":
                self.set_signatureRules(input_json_temp["signatureRules"])
            else:
                self.set_signatureRules("SHA-256/SECP256K1")

        if "receiptCreateStatus" in input_params_list:
            if input_json_temp["receiptCreateStatus"] != "":
                self.set_receiptCreateStatus(input_json_temp
                                             ["receiptCreateStatus"])
            else:
                self.set_receiptCreateStatus(0)

        if "workOrderRequestHash" in input_params_list:
            # if input_json_temp["workOrderRequestHash"] != "":
            #    self.set_workOrderRequestHash(input_json_temp["workOrderRequestHash"])
            # else:
            self.set_workOrderRequestHash(final_hash_str)

        if "requesterGeneratedNonce" in input_params_list:
            # if input_json_temp["requesterGeneratedNonce"] != "":
            #    self.set_requesterGeneratedNonce(input_json_temp["requesterGeneratedNonce"])
            # else:
            self.set_requesterGeneratedNonce(requester_nonce)

        if "requesterSignature" in input_params_list:
            # if input_json_temp["requesterSignature"] != "":
            # self.set_requesterSignature(input_json_temp["requesterSignature"])
            # else:
            self.set_requesterSignature(wo_receipt_sign)

        # if "receiptVerificationKey" in input_params_list:
        #    self.set_receiptVerificationKey(private_key)

    # def set_receiptVerificationKey(self, receiptVerificationKey):
    #    self.params_obj["receiptVerificationKey"] = receiptVerificationKey

    def set_requesterSignature(self, requesterSignature):
        self.params_obj["requesterSignature"] = requesterSignature

    def set_requesterGeneratedNonce(self, requesterGeneratedNonce):
        self.params_obj["requesterGeneratedNonce"] = requesterGeneratedNonce

    def set_workOrderRequestHash(self, workOrderRequestHash):
        self.params_obj["workOrderRequestHash"] = workOrderRequestHash

    def set_receiptCreateStatus(self, receiptCreateStatus):
        self.params_obj["receiptCreateStatus"] = receiptCreateStatus

    def set_signatureRules(self, signatureRules):
        self.params_obj["signatureRules"] = signatureRules

    def set_requester_id(self, requester_id):
        self.params_obj["requesterId"] = requester_id

    def set_worker_id(self, worker_id):
        self.params_obj["workerId"] = worker_id
        self.params_obj["workerServiceId"] = worker_id

    def set_work_order_id(self, work_order_id):
        self.params_obj["workOrderId"] = work_order_id

    def get_work_order_id(self):
        if "workOrderId" in self.params_obj:
            return self.params_obj["workOrderId"]

    def compute_signature(self, tamper):

        self._compute_requester_signature()

        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()

        input_after_sign = self.to_string()
        tamper_instance = 'after_sign'
        tampered_request = tamper_request(input_after_sign, tamper_instance,
                                          tamper)
        return tampered_request

    def to_string(self):
        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()
        return json.dumps(json_rpc_request, indent=4)

    def get_params(self):
        return self.params_obj.copy()

    def _compute_requester_signature(self):
        self.public_key = self.private_key.GetPublicKey().Serialize()
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
        private_key = enclave_helper.generate_signing_keys()
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

