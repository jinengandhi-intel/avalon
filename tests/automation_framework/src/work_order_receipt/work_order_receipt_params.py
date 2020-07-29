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
        self.config_file = os.path.join(
            env.work_order_receipt, "work_order_create_receipt.yaml")

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        """
        This function forms the request for WorkOrderReceiptCreate as per EEA spec
        :param input_json: Input JSON as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: response received from WorkOrderSubmit request
        :return: Fully formed JSON which can be submitted to listener
        """
        return self.form_create_receipt_input(input_json, worker_obj, pre_test_response)

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        """
        This functions forms the input for WorkOrderReceiptCreate SDK function
        :param input_json: containing input data as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: Response received from WorkOrderSubmit request
        :return: workOrderCreateReceipt Response
        """
        return self.form_create_receipt_input(input_json, worker_obj, pre_test_response)
    
    def form_create_receipt_input(self, input_json, worker_obj, pre_test_response):
        if input_json is None:
            input_json = wconfig.read_config(self.config_file, "")
            input_json = json.loads(input_json)

        logger.info("***Pre test*****\n%s\n", pre_test_response)
        logger.info("***Input json*****\n%s\n", input_json)
        
        self.private_key = crypto_utility.generate_signing_keys()
        
        if env.test_mode == "listener":
            
            wconfig.add_json_values(self, input_json, pre_test_response)
            input_work_order = wconfig.compute_signature(self, True)
            logger.info('''Compute Signature complete \n''')
            wo_create_receipt = json.loads(input_work_order)
        else:

            wo_request = json.loads(pre_test_response.to_jrpc_string(input_json["id"]))
            wo_receipt_request_obj = WorkOrderReceiptRequest()
            wo_create_receipt = wo_receipt_request_obj.create_receipt(
                wo_request,
                ReceiptCreateStatus.PENDING.value,
                self.private_key
            )
        logger.info("Work order create receipt request : {} \n \n ".format(
            json.dumps(wo_create_receipt, indent=4)
        ))
        return wo_create_receipt
