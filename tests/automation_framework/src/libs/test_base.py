from src.libs.avalon_test_wrapper \
    import build_request_obj, submit_request, \
    pre_test_worker_env, pre_test_workorder_env
import logging
import env
import os
from src.utilities.worker_utilities \
    import read_config
import inspect
import json
from src.libs.avalon_libs import AvalonImpl

avalon_lib_instance = AvalonImpl()
logger = logging.getLogger(__name__)


class AvalonBase():
    def __init__(self):
        self.uri_client = env.uri_client
        self.build_request_output = {}

    def setup_and_build_request_worker_register(self, input_file):
        """
        Set up the environment required to run the WorkerRegister
        tests, build the request for WorkerRegister and update the
        output to build_request_obj
        :param input_file: test data for WorkerRegister as per EEA spec
        :return: 0
        """
        request_obj, action_obj = build_request_obj(input_file)
        self.build_request_output.update({'request_obj': request_obj})
        return 0

    def setup_and_build_request_worker_lookup(self, input_file):
        """
        Set up's the environment required to run the WorkerLookUp
        tests, build the request for WorkerLookUp and update the
        output to build_request_obj
        :param input_file: test data for WorkerLookUp as per EEA spec
        :return: 0
        """
        request_obj, action_obj = build_request_obj(input_file)
        self.build_request_output.update({'request_obj': request_obj})
        return 0

    def setup_and_build_request_wo_submit(self, input_file):
        """
        Set up's the environment for the WorkOrderSubmit test cases,
        This function submits the WorkerLookUp and WorkerRetrieve
        request before forming WorkOrderSubmit request,
        and it update it's output to build_request_obj
        :param input_file: test data for WorkOrderSubmit as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_wo_getresult(self, input_file):
        """
        Set up's the environment for WorkOrderGetResult test case.
        This function submits the request for worker related functions
        like WorkerLookUp, WorkerRetrieve and submits the WorkOrderSubmit
        request. It also forms the request for WorkOrderGetResult
        request and update the output to build_request_obj
        :param input_file: test data for WorkOrderGetResult as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=wo_submit)
        logger.info("AvalonBase wo_submit %s", wo_submit)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': wo_submit})
        return 0

    def setup_and_build_request_worker_retrieve(self, input_file):
        """
        Set up's the environment for WorkerRetrieve request tests and
        build's the request for WorkerRetrieve, also updates its
        output to build_request_obj
        :param input_file: test data for WorkerRetrieve as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_create_receipt(self, input_file):
        """
        Set Up's the environment for Receipt Create tests and build's the
        request for CreateReceipt and updates its output to build_request_obj
        :param input_file: test data for ReceiptCreate as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)

        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=wo_submit)

        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_receipt_retrieve(self, input_file):
        """
        Set Up's the environment for Receipt Retrieve tests and build's the
        request for ReceiptRetrieve and update's output to build_request_obj
        :param input_file: test data for ReceiptRetrieve as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)
        logger.info("***Pre test output*****\n%s\n", pre_test_output)
        logger.info("***wo_submit*****\n%s\n", wo_submit)
        # submit_request = json.loads(wo_submit)
        result_response = self.getresult(wo_submit, {"error": {"code": 5}})

        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=wo_submit)

        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def reset_status(self, default_data):
        self.setup_and_build_request_worker_status(default_data)

        response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            default_data)

        return response

    def reset_worker(self, default_data):
        self.setup_and_build_request_worker_update(default_data)

        response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            default_data)

        return response

    def teardown(self, config):
        """
        This function should free the resources which are not required
        """
        test_data = read_config(config, "")
        method_name = test_data.get("method")
        if method_name == "WorkerSetStatus":
            reset_status_response = self.reset_status(test_data)
            logger.info("Reset worker status %s \n", reset_status_response)

        if method_name == "WorkerSetStatus" or \
                method_name == "WorkerUpdate":
            reset_worker_response = self.reset_worker(test_data)
            logger.info("Reset worker %s \n", reset_worker_response)

        logger.info("Teardown complete")

    def setup_and_build_request_worker_update(self, input_file):
        """
        Set Up's the environment for WorkerUpdate tests and build's request
        for WorkerUpdate and update the output to build_request_obj
        :param input_file: test data for WorkerUpdate as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_worker_status(self, input_file):
        """
        Set Up's the environment for WorkerStatus tests and build's request
        for WorkerStatus and update the output to build_request_obj
        :param input_file: test data for WorkerUpdate as per EEA spec
        :return: 0
        """
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def getresult(self, output_obj, submit_response={}):
        """
        This function is called to get the result of a workOrder. If a
        workorder is still computing, it calls to getResult api, otherwise
        returns the same result
        :param output_obj: request_obj from build_request_obj
        :param submit_response: response from WorkOrderSubmit request
        :return: If error code is 5 then result from get_result api else output_obj
        """
        if submit_response.get("error", {}).get("code") == 5:
            response = avalon_lib_instance.work_order_get_result(output_obj)
        else:
            response = submit_response
        return response

    def post_json_msg(self, request_file):
        """
        This function should send the request to listener without any modifications
        :param request_file: Input Json File containing inputs for method specified
        :return: Response from listener
        """
        file = open(request_file, "r")
        json_str = file.read()
        file.close()
        logger.info('**********Received Request*********\n%s\n', json_str)
        response = self.uri_client._postmsg(json_str)
        logger.info('**********Received Response*********\n%s\n', response)
        return response

    def avalon_uncomputed(self, test_data=None):

        json_str = json.dumps(test_data, indent=4)
        logger.info(
            '**********Received Request post message*********\n%s\n',
            json_str)
        response = self.uri_client._postmsg(json_str)
        logger.info('**********Received Response*********\n%s\n', response)
        return response

    def avalon_computed(self, test_data):

        submit_response = ""
        method_name = test_data.get("method")
        if "WorkOrderSubmit" in method_name:
            self.setup_and_build_request_wo_submit(
                test_data)
        elif "WorkOrderGetResult" in method_name:
            self.setup_and_build_request_wo_getresult(
                test_data)
        elif "WorkerLookUp" in method_name:
            self.setup_and_build_request_worker_lookup(
                test_data)
        elif "WorkerRetrieve" in method_name:
            self.setup_and_build_request_worker_retrieve(
                test_data)
        elif "WorkerRegister" in method_name:
            self.setup_and_build_request_worker_register(
                test_data)
        elif "WorkerSetStatus" in method_name:
            self.setup_and_build_request_worker_status(
                test_data)
        elif "WorkerUpdate" in method_name:
            self.setup_and_build_request_worker_update(
                test_data)
        elif "WorkOrderReceiptCreate" in method_name:
            self.setup_and_build_request_create_receipt(
                test_data)
        elif "WorkOrderReceiptRetrieve" in method_name:
            self.setup_and_build_request_receipt_retrieve(
                test_data)
        elif "WorkOrderReceiptLookUp" in method_name:
            self.setup_and_build_request_create_receipt(
                test_data)

        submit_response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            test_data)

        if "WorkOrderSubmit" in method_name:
            result_response = self.getresult(
                self.build_request_output['request_obj'],
                submit_response)

            submit_response = result_response

        return submit_response

    def run_test(self, config_file, direct_avalon_listener=None):
        test_name = inspect.stack()[1].function
        test_data = read_config(config_file, test_name)
        submit_response = ""
        if direct_avalon_listener:
            submit_response = self.avalon_uncomputed(test_data)
        else:
            submit_response = self.avalon_computed(test_data)

        return submit_response
