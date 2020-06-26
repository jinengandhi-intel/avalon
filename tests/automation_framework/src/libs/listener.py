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
import time
from src.utilities.worker_utilities import GetResultWaitTime
import avalon_sdk.worker.worker_details as worker
logger = logging.getLogger(__name__)


class ListenerImpl():

    def read_json(self, request_file):
        # Read the method name from JSON file
        with open(request_file, "r") as file:
            input_json = file.read().rstrip('\n')

        input_json_obj = json.loads(input_json)

        return input_json_obj

    def worker_lookup(self):
        lookup_obj = WorkerLookUp()
        test_final_json = lookup_obj.configure_data(
            input_json=None, worker_obj=None, pre_test_response=None)

        lookup_response = submit_request_listener(
            env.uri_client, test_final_json,
            env.worker_lookup_output_json_file_name)
        return lookup_response

    def worker_retrieve(self, lookup_response):
        worker_obj = worker.SGXWorkerDetails()
        retrieve_obj = WorkerRetrieve()
        input_worker_retrieve = retrieve_obj.configure_data(
            input_json=None, worker_obj=None,
            pre_test_response=lookup_response)
        logger.info('*****Worker details Updated with Worker ID***** \
                                       \n%s\n', input_worker_retrieve)
        retrieve_response = submit_request_listener(
            env.uri_client, input_worker_retrieve,
            env.worker_retrieve_output_json_file_name)

        worker_obj.load_worker(retrieve_response['result']['details'])
        retrieve_response['workerId'] = input_worker_retrieve["params"]["workerId"]

        logger.info('*****Worker retrieve response***** \
                                       \n%s\n', retrieve_response)
        return retrieve_response

    def work_order_submit(self, response_output):
        submit_obj = WorkOrderSubmit()
        submit_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_success.json")
        submit_request_json = self.read_json(submit_request_file)
        submit_json = submit_obj.configure_data(
            input_json=submit_request_json, worker_obj=None,
            pre_test_response=response_output)
        submit_response = submit_request_listener(
            env.uri_client, submit_json,
            env.wo_submit_output_json_file_name)
        input_work_order_submit = submit_obj.compute_signature(submit_obj.tamper)
        json_obj = json.loads(input_work_order_submit)
        json_obj["sessionKey"] = submit_obj.session_key
        json_obj["sessionKeyIv"] = submit_obj.session_iv
        json_obj["requesterNonce"] = submit_obj.params_obj["requesterNonce"]
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return json_obj

    def work_order_get_result(self, wo_submit):
        wo_getresult_obj = WorkOrderGetResult()
        wo_getresult_request_file = os.path.join(
            env.work_order_input_file,
            "work_order_getresult.json")
        wo_getresult_request_json = self.read_json(wo_getresult_request_file)
        wo_getresult_json = wo_getresult_obj.configure_data(
            input_json=wo_getresult_request_json, worker_obj=None,
            pre_test_response=wo_submit)
        # submit work order get result request and retrieve response
        response = submit_request_listener(
            env.uri_client, wo_getresult_json,
            env.wo_result_output_json_file_name)
        logger.info("******Received Response*****\n%s\n", response)
        return response