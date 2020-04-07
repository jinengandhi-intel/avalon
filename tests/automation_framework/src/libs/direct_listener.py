import os
import logging
import json
from src.worker_lookup.worker_lookup_params \
    import WorkerLookUp
from src.libs import constants
from src.utilities.submit_request_utility import \
    submit_request_listener
from src.worker_retrieve.worker_retrieve_params \
    import WorkerRetrieve
from src.work_order_submit.work_order_submit_params \
    import WorkOrderSubmit
import globals
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
            globals.uri_client, test_final_json,
            constants.worker_lookup_output_json_file_name)
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
            globals.uri_client, input_worker_retrieve,
            constants.worker_retrieve_output_json_file_name)
        logger.info('*****Worker retrieve response***** \
                                       \n%s\n', retrieve_response)
        # if globals.blockchain != "":
        #    worker_obj.load_worker(
        #        json.loads(retrieve_response[4]))
        # else:
        #    worker_obj.load_worker(
        #        retrieve_response["result"]["details"])
        worker_obj.load_worker(retrieve_response['result']['details'])

        return worker_obj

    def work_order_submit(self, worker_obj):
        submit_obj = WorkOrderSubmit()
        submit_request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_success.json")
        submit_request_json = self.read_json(submit_request_file)
        submit_json = submit_obj.configure_data(
            input_json=submit_request_json, worker_obj=worker_obj,
            pre_test_response=None)
        submit_response = submit_request_listener(
            globals.uri_client, submit_json,
            constants.wo_submit_output_json_file_name)
        input_work_order_submit = submit_obj.compute_signature(
            constants.wo_submit_tamper)
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return input_work_order_submit
