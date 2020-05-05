import json
import logging

import avalon_crypto_utils.signature as signature
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

    def add_json_values(self, input_json_temp, tamper, wo_submit):
        input_request_wo_submit = json.loads(wo_submit)
        # if "id" in input_json_temp.keys():
        #    self.set_request_id(input_json_temp["id"])

        if "workOrderId" in input_json_temp.keys():
            # if input_json_temp["workOrderId"] != "" :
            self.set_work_order_id(input_request_wo_submit
                                   ["params"]["workOrderId"])

    def set_work_order_id(self, work_order_id):
        self.params_obj["workOrderId"] = work_order_id

    def to_string(self):
        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()
        return json.dumps(json_rpc_request, indent=4)

    def configure_data(
            self, input_json, worker_obj, wo_submit):
        self.add_json_values(input_json, self.tamper, wo_submit)
        final_json = json.loads(self.to_string())
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, wo_submit):
        workorder_id = wo_submit.get_work_order_id()
        return workorder_id