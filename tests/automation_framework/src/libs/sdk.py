from src.utilities.submit_request_utility import \
    worker_lookup_sdk, \
    worker_retrieve_sdk, workorder_receiptcreate_sdk, \
    workorder_submit_sdk, workorder_getresult_sdk
import logging
import os
import json
import env
from src.worker_lookup.worker_lookup_params \
    import WorkerLookUp
from src.work_order_receipt.work_order_receipt_params \
    import WorkOrderReceiptCreate
from src.utilities.submit_request_utility import \
    submit_request_listener
from src.work_order_get_result.work_order_get_result_params \
    import WorkOrderGetResult
from src.worker_retrieve.worker_retrieve_params \
    import WorkerRetrieve
from src.work_order_submit.work_order_submit_params \
    import WorkOrderSubmit
import avalon_sdk.worker.worker_details as worker
logger = logging.getLogger(__name__)


class SDKImpl():

    def worker_lookup(self):
        lookup_obj = WorkerLookUp()
        worker_type = lookup_obj.configure_data_sdk(
            input_json=None, worker_obj=None, pre_test_response=None)

        lookup_response = worker_lookup_sdk(worker_type)
        return lookup_response

    def worker_retrieve(self, lookup_response):
        worker_obj = worker.SGXWorkerDetails()
        retrieve_obj = WorkerRetrieve()
        worker_id = retrieve_obj.configure_data_sdk(
            input_json=None, worker_obj=None,
            pre_test_response=lookup_response)
        logger.info('*****Worker details Updated with Worker ID***** \
                                           \n%s\n', worker_id)
        retrieve_response = worker_retrieve_sdk(worker_id)
        # worker_obj.load_worker(retrieve_response['result']['details'])
        # if env.proxy_mode and \
        #    env.blockchain_type == "ethereum":
        return retrieve_response

    def work_order_submit(self, response_output):
        submit_obj = WorkOrderSubmit()
        submit_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_success.json")
        submit_request_json = self.read_json(submit_request_file)
        wo_params = submit_obj.configure_data_sdk(
            input_json=submit_request_json, worker_obj=None,
            pre_test_response=response_output)
        submit_response = workorder_submit_sdk(wo_params)
        # input_work_order_submit = submit_obj.compute_signature(
        #    env.wo_submit_tamper)
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return wo_params

    def work_order_create_receipt(self, wo_submit):
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

    def work_order_get_result(self, wo_submit):
        wo_getresult_obj = WorkOrderGetResult()
        wo_getresult_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_getresult.json")
        wo_getresult_request_json = self.read_json(wo_getresult_request_file)
        workorder_id = wo_getresult_obj.configure_data_sdk(
            input_json=wo_getresult_request_json, worker_obj=None,
            pre_test_response=wo_submit)
        get_result_res = workorder_getresult_sdk(
            workorder_id, wo_getresult_request_json)
        logger.info("Work order get result : {}\n ".format(
            json.dumps(get_result_res, indent=4)
        ))
        return get_result_res


    def read_json(self, request_file):
        # Read the method name from JSON file
        with open(request_file, "r") as file:
            input_json = file.read().rstrip('\n')

        input_json_obj = json.loads(input_json)

        return input_json_obj

