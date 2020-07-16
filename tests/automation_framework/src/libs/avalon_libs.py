import os
import env
import logging
import json
from src.worker_lookup.worker_lookup_params \
    import WorkerLookUp
from src.utilities.submit_request_utility import \
    submit_request_listener
from src.worker_retrieve.worker_retrieve_params \
    import WorkerRetrieve
from src.work_order_submit.work_order_submit_params \
    import WorkOrderSubmit
from src.work_order_get_result.work_order_get_result_params \
    import WorkOrderGetResult
from src.work_order_receipt.work_order_receipt_params \
    import WorkOrderReceiptCreate
from src.utilities.submit_request_utility import \
    worker_lookup_sdk, \
    worker_retrieve_sdk, workorder_receiptcreate_sdk, \
    workorder_submit_sdk, workorder_getresult_sdk
from src.utilities.worker_utilities import configure_data
import avalon_sdk.worker.worker_details as worker
logger = logging.getLogger(__name__)


class AvalonImpl():

    def read_json(self, request_file):
        # Read the method name from JSON file
        with open(request_file, "r") as file:
            input_json = file.read().rstrip('\n')

        input_json_obj = json.loads(input_json)

        return input_json_obj

    def worker_lookup(self):
        lookup_obj = WorkerLookUp()
        configure_data_output = configure_data(
            lookup_obj, input_json=None,
            worker_obj=None,
            pre_test_response=None)
        if env.test_mode == "listener":
            lookup_response = submit_request_listener(
                env.uri_client, configure_data_output,
                env.worker_lookup_output_json_file_name)
        else:
            lookup_response = worker_lookup_sdk(configure_data_output)
        logger.info("Worker Lookup : {}\n ".format(
            json.dumps(lookup_response, indent=4)
        ))
        return lookup_response

    def worker_retrieve(self, lookup_response):
        worker_obj = worker.SGXWorkerDetails()
        retrieve_obj = WorkerRetrieve()
        configure_data_output = configure_data(
            retrieve_obj, input_json=None, worker_obj=None,
            pre_test_response=lookup_response)
        logger.info('*****Worker details Updated with Worker ID***** \
                                       \n%s\n', configure_data_output)
        if env.test_mode == "listener":
            retrieve_response = submit_request_listener(
                env.uri_client, configure_data_output,
                env.worker_retrieve_output_json_file_name)
            worker_obj.load_worker(retrieve_response['result']['details'])
            retrieve_response['workerId'] = configure_data_output["params"]["workerId"]
        else:
            retrieve_response = worker_retrieve_sdk(configure_data_output)

        logger.info("Worker Retrieved : {}\n ".format(
            json.dumps(retrieve_response, indent=4)
        ))
        return retrieve_response

    def work_order_submit(self, response_output):
        submit_obj = WorkOrderSubmit()
        submit_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_success.json")
        submit_request_json = self.read_json(submit_request_file)
        configure_data_output = configure_data(
            submit_obj, input_json=submit_request_json,
            worker_obj=None, pre_test_response=response_output)
        if env.test_mode == "listener":
            submit_response = submit_request_listener(
                env.uri_client, configure_data_output,
                env.wo_submit_output_json_file_name)
            input_work_order_submit = submit_obj.compute_signature(submit_obj.tamper)
            json_obj = json.loads(input_work_order_submit)
            json_obj["sessionKey"] = submit_obj.session_key
            json_obj["sessionKeyIv"] = submit_obj.session_iv
            json_obj["requesterNonce"] = submit_obj.params_obj["requesterNonce"]
        else:
            submit_response = workorder_submit_sdk(configure_data_output)
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return configure_data_output

    def work_order_get_result(self, wo_submit):
        wo_getresult_obj = WorkOrderGetResult()
        wo_getresult_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_getresult.json")
        wo_getresult_request_json = self.read_json(wo_getresult_request_file)
        configure_data_output = configure_data(
            wo_getresult_obj, input_json=wo_getresult_request_json,
            worker_obj=None,
            pre_test_response=wo_submit)

        # submit work order get result request and retrieve response

        if env.test_mode == "listener":
            get_result_response = submit_request_listener(
                env.uri_client, configure_data_output,
                env.wo_result_output_json_file_name)
        else:
            get_result_response = workorder_getresult_sdk(
                configure_data_output, wo_getresult_request_json)
        logger.info("Work order get result : {}\n ".format(
            json.dumps(get_result_response, indent=4)
        ))
        return get_result_response

    def work_order_create_receipt(self, wo_submit):
        if env.test_mode == "sdk":
            receipt_retrieve_obj = WorkOrderReceiptCreate()
            receipt_retrieve_file = os.path.join(
                env.work_order_receipt,
                "work_order_receipt.json")
            receipt_request_json = self.read_json(receipt_retrieve_file)
            wo_create_receipt = receipt_retrieve_obj.configure_data_sdk(
                input_json=receipt_request_json, worker_obj=None,
                pre_test_response=wo_submit)
            receipt_create_response = workorder_receiptcreate_sdk(
                wo_create_receipt, receipt_request_json)
            logger.info("***Receipt created***\n%s\n", receipt_create_response)
            logger.info("***Receipt request***\n%s\n", wo_create_receipt)
            return wo_create_receipt