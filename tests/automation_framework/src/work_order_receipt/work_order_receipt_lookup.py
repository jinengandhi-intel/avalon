import json
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
        self.output_json_file_name = "work_order_retrieve_lookup"

    def configure_data_sdk(self, input_json, worker_obj, wo_submit):
        requester_id = wo_submit.get_requester_id()
        return requester_id
