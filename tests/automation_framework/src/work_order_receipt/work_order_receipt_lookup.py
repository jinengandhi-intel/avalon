import json
import os
import env
import logging
import src.utilities.worker_utilities as wconfig
import avalon_crypto_utils.signature as signature
logger = logging.getLogger(__name__)


class WorkOrderReceiptLookUp():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0",
                       "method": "WorkOrderReceiptLookUp", "id": 11}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "work_order_receipt_lookup"
        self.config_file = os.path.join(
            env.work_order_receipt, "work_order_receipt_lookup.yaml")

    def configure_data(
            self, input_json, worker_obj, wo_submit):
        return self.form_worker_receipt_lookup_input(input_json, wo_submit)

    def configure_data_sdk(self, input_json, worker_obj, wo_submit):
        """
        This functions returns the requester id present in workOrderSubmit response
        :param input_json: Input JSON as per EEA spec
        :param worker_obj: worker object
        :param wo_submit: workOrderSubmit response
        :return: requester_id from WorkOrderSubmit response
        """
        return self.form_worker_receipt_lookup_input(input_json, wo_submit)

    def form_worker_receipt_lookup_input(self, input_json, wo_submit):
        receipt_lookup_request = wconfig.workorder_getresult_receipt_input(
            self, input_json, wo_submit)
        if env.test_mode == "listener":
            receipt_lookup_request = json.loads(wconfig.to_string(self))
        logger.info(
            '** Receipt Lookup Request ** \n%s\n',
            receipt_lookup_request)
        return receipt_lookup_request
