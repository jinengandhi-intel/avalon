import json
import logging
import os
import env
import src.utilities.worker_utilities as wconfig
import avalon_crypto_utils.signature as signature
import env
logger = logging.getLogger(__name__)


class WorkOrderReceiptRetrieve():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0",
                       "method": "WorkOrderReceiptRetrieve", "id": 11}
        self.params_obj = {}
        self.sig_obj = signature.ClientSignature()
        self.SIGNING_ALGORITHM = "SECP256K1"
        self.HASHING_ALGORITHM = "SHA-256"
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "work_order_retrieve_receipt"
        # self.session_key = self.generate_key()
        # self.session_iv = self.generate_iv()
        self.config_file = os.path.join(
            env.work_order_receipt, "work_order_retrieve_receipt.yaml")

    def add_json_values(self, input_json_temp, tamper, wo_submit):
        input_request_wo_submit = json.loads(wo_submit)

        if "workOrderId" in input_json_temp.keys():
            wconfig.set_parameter(
                self.params_obj,
                "workOrderId",
                input_request_wo_submit["params"]["workOrderId"])

    def configure_data(
            self, input_json, worker_obj, wo_submit):
        #wconfig.add_json_values(input_json, self.tamper, wo_submit)
        #final_json = json.loads(wconfig.to_string(self))
        return self.form_worker_receipt_retrieve_input(input_json, wo_submit)

    def configure_data_sdk(
            self, input_json, worker_obj, wo_submit):
        return self.form_worker_receipt_retrieve_input(input_json, wo_submit)

    def form_worker_receipt_retrieve_input(self, input_json, wo_submit):
        receipt_retrieve_request = wconfig.workorder_getresult_receipt_input(
            self, input_json, wo_submit)
        if env.test_mode == "listener":
            receipt_retrieve_request = json.loads(wconfig.to_string(self))
        logger.info('***** Receipt Retrieve Request ***** \
                        \n%s\n', receipt_retrieve_request)
        return receipt_retrieve_request
