import os
import env
import logging
import json

from src.utilities.submit_request_utility import \
    worker_lookup_sdk, \
    worker_retrieve_sdk, workorder_receiptcreate_sdk, \
    workorder_submit_sdk, workorder_getresult_sdk, \
    submit_request_listener
from src.libs.avalon_request import AvalonRequest
import src.utilities.worker_utilities as wconfig
import avalon_sdk.worker.worker_details as worker

logger = logging.getLogger(__name__)


class AvalonImpl():
    action_obj = AvalonRequest()

    def worker_lookup(self):
        """
        Submit's WorkerLookup request to listener/sdk
        Config need to be set in env.py
        :return: lookup_response - response returned from WorkerLookUp Request
        """
        configure_data_output = wconfig.configure_data(
            self.action_obj,
            input_json=None,
            method_name="WorkerLookUp",
            pre_test_response=None)
        if env.test_mode == env.listener_string:
            lookup_response = submit_request_listener(
                env.uri_client, configure_data_output)
        else:
            lookup_response = worker_lookup_sdk(configure_data_output)
        logger.info("Worker Lookup : {}\n ".format(
            json.dumps(lookup_response, indent=4)
        ))
        return lookup_response

    def worker_retrieve(self, lookup_response):
        """
        Submit WorkerRetrieve request to listener/sdk
        Config need to be set in env.py
        :param lookup_response: Response received from worker_lookup
        :return: Details of worker present in lookup_response
        """
        worker_obj = worker.SGXWorkerDetails()
        configure_data_output = wconfig.configure_data(
            self.action_obj, input_json=None,
            pre_test_response=lookup_response,
            method_name="WorkerRetrieve")
        logger.info('*****Worker details Updated with Worker ID***** \
                                       \n%s\n', configure_data_output)
        if env.test_mode == env.listener_string:
            retrieve_response = submit_request_listener(
                env.uri_client, configure_data_output)
            worker_obj.load_worker(retrieve_response['result']['details'])
            retrieve_response['workerId'] = \
                configure_data_output["params"]["workerId"]
        else:
            retrieve_response = worker_retrieve_sdk(configure_data_output)

        logger.info("Worker Retrieved : {%s}\n ", retrieve_response)
        return retrieve_response

    def work_order_submit(self, response_output):
        """
        Submit's the WorkOrderSubmit request and form the input params
        needed to verify the work order details
        Config need to be set in env.py
        :param response_output: Request to be sent
        :return: Returns the response received from WorkOrderSubmit request
        """

        submit_request_json = wconfig.read_config(
            env.work_order_submit_input_file, "test_id")

        configure_data_output = wconfig.configure_data(
            self.action_obj, input_json=submit_request_json,
            pre_test_response=response_output,
            method_name="WorkOrderSubmit")

        if env.test_mode == env.listener_string:
            submit_response = submit_request_listener(
                env.uri_client, configure_data_output)
            input_work_order_submit = wconfig.compute_signature(
                self.action_obj)
            json_obj = json.loads(input_work_order_submit)
            json_obj["sessionKey"] = self.action_obj.session_key
            json_obj["sessionKeyIv"] = self.action_obj.session_iv
            json_obj["requesterNonce"] = \
                self.action_obj.params_obj["requesterNonce"]
        else:
            submit_response = workorder_submit_sdk(configure_data_output)
            json_obj = configure_data_output
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return json_obj

    def work_order_get_result(self, wo_submit):
        """
        Submit's WorkOrderGetResult request to listener/sdk
        Config need to be set in env.py
        :param wo_submit:
        :return:
        """

        wo_getresult_request_json = wconfig.read_config(
            env.work_order_getresult_input_file, "")

        configure_data_output = wconfig.configure_data(
            self.action_obj, input_json=wo_getresult_request_json,
            method_name="WorkOrderGetResult",
            pre_test_response=wo_submit)

        # submit work order get result request and retrieve response

        if env.test_mode == env.listener_string:
            get_result_response = submit_request_listener(
                env.uri_client, configure_data_output)
        else:
            get_result_response = workorder_getresult_sdk(
                configure_data_output, wo_getresult_request_json)
        logger.info("Work order get result : {}\n ".format(
            json.dumps(get_result_response, indent=4)
        ))
        return get_result_response

    def work_order_create_receipt(self, wo_submit):
        """
        Submit the WorkOrderCreateReceipt for sdk
        Config needed to be set in env.py
        :param wo_submit: Response received from WorkOrderSubmit request
        :return: Response received from creating receipt
        """

        receipt_request_json = wconfig.read_config(
            env.create_receipt_input_file, "test_config")

        configure_data_output = wconfig.configure_data(
            self.action_obj,
            input_json=receipt_request_json,
            pre_test_response=wo_submit,
            method_name="WorkOrderReceiptCreate")

        if env.test_mode == env.listener_string:
            receipt_create_response = submit_request_listener(
                env.uri_client, configure_data_output)
        else:
            receipt_create_response = workorder_receiptcreate_sdk(
                configure_data_output, receipt_request_json)
        logger.info("***Receipt created***\n%s\n", receipt_create_response)
        logger.info("***Receipt request***\n%s\n", configure_data_output)

        return configure_data_output
