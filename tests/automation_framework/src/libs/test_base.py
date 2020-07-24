from src.libs.avalon_test_wrapper \
    import build_request_obj, submit_request, \
    pre_test_worker_env, pre_test_workorder_env
import logging
import env
import os
from src.utilities.worker_utilities \
    import read_config
import inspect
from src.libs.avalon_libs import AvalonImpl
from src.utilities.worker_utilities \
    import ResultStatus, read_config

avalon_lib_instance = AvalonImpl()
logger = logging.getLogger(__name__)


class AvalonBase():
    def __init__(self):
        self.uri_client = env.uri_client
        self.build_request_output = {}
        self.output_json_file_name = ""

    def setup_and_build_request_worker_register(self, input_file):
        request_obj, action_obj = build_request_obj(input_file)
        self.build_request_output.update({'request_obj': request_obj})
        return 0

    def setup_and_build_request_worker_lookup(self, input_file):
        request_obj, action_obj = build_request_obj(input_file)
        self.build_request_output.update({'request_obj': request_obj})
        return 0

    def setup_and_build_request_wo_submit(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_wo_getresult(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_output=pre_test_output,
            pre_test_response=wo_submit)
        logger.info("AvalonBase wo_submit %s", wo_submit)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': wo_submit})
        return 0

    def setup_and_build_request_worker_retrieve(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_create_receipt(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_output=pre_test_output,
            pre_test_response=wo_submit)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_receipt_retrieve(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        wo_submit = pre_test_workorder_env(input_file, pre_test_output)
        logger.info("***Pre test output*****\n%s\n", pre_test_output)
        logger.info("***wo_submit*****\n%s\n", wo_submit)
        # submit_request = json.loads(wo_submit)
        result_response = self.getresult(wo_submit, {"error": {"code": 5}})
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_output=pre_test_output,
            pre_test_response=wo_submit)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def reset_status(self):
        default_data = read_config(
            os.path.join(env.worker_input_file, "worker_setstatus.ini"),
            "DEFAULT")

        self.setup_and_build_request_worker_status(default_data)

        response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            default_data)

        return response

    def reset_worker(self):
        default_data = read_config(
            os.path.join(env.worker_input_file, "worker_update.ini"),
            "DEFAULT")

        self.setup_and_build_request_worker_update(default_data)

        response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            default_data)

        return response

    def teardown(self, method_name):
        if method_name == "WorkerSetStatus":
            reset_status_response = self.reset_status()
            logger.info("Reset worker status %s \n", reset_status_response)

        if method_name == "WorkerSetStatus" or \
                method_name == "WorkerUpdate":
            reset_worker_response = self.reset_worker()
            logger.info("Reset worker %s \n", reset_worker_response)

        logger.info("Teardown complete")

    def setup_and_build_request_worker_update(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_worker_status(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def getresult(self, output_obj, submit_response={}):
        if submit_response.get("error", {}).get("code") == 5:
            response = avalon_lib_instance.work_order_get_result(output_obj)
        else:
            response = submit_response
        return response

    def post_json_msg(self, request_file):
        file = open(request_file, "r")
        json_str = file.read()
        file.close()
        logger.info('**********Received Request*********\n%s\n', json_str)
        response = self.uri_client._postmsg(json_str)
        logger.info('**********Received Response*********\n%s\n', response)
        return response

    def run_test(self, config_file):
        test_name = inspect.stack()[1].function
        test_data = read_config(config_file, test_name)
        result_response = ""

        if "work_order_submit" in config_file:
            self.setup_and_build_request_wo_submit(
                test_data)
            self.output_json_file_name = \
                env.wo_submit_output_json_file_name
        elif "work_order_get_result" in config_file:
            self.setup_and_build_request_wo_getresult(
                test_data)
            self.output_json_file_name = \
                env.wo_result_output_json_file_name
        elif "worker_lookup" in config_file:
            self.setup_and_build_request_worker_lookup(
                test_data)
            self.output_json_file_name = \
                env.worker_lookup_output_json_file_name
        elif "worker_retrieve" in config_file:
            self.setup_and_build_request_worker_retrieve(
                test_data)
            self.output_json_file_name = \
                env.worker_retrieve_output_json_file_name
        elif "worker_register" in config_file:
            self.setup_and_build_request_worker_register(
                test_data)
            self.output_json_file_name = \
                env.worker_register_output_json_file_name
        elif "worker_setstatus" in config_file:
            self.setup_and_build_request_worker_status(
                test_data)
            self.output_json_file_name = \
                env.worker_setstatus_output_json_file_name
        elif "worker_update" in config_file:
            self.setup_and_build_request_worker_update(
                test_data)
            self.output_json_file_name = \
                env.worker_update_output_json_file_name

        submit_response = submit_request(
            self.uri_client,
            self.build_request_output['request_obj'],
            self.output_json_file_name,
            test_data)

        if "work_order_submit" in config_file:
            result_response = self.getresult(
                self.build_request_output['request_obj'],
                submit_response)

            submit_response = result_response

        return submit_response
