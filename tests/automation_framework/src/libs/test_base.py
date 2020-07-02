from src.libs.avalon_test_wrapper \
    import build_request_obj, read_json, submit_request, \
    pre_test_worker_env, pre_test_workorder_env
import logging
import env

from src.libs.listener import ListenerImpl
from src.libs.sdk import SDKImpl

logger = logging.getLogger(__name__)


class AvalonBase():
    def __init__(self):
        self.uri_client = env.uri_client
        self.build_request_output = {}

    def setup_and_build_request_register(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(input_file)
        self.build_request_output.update({'request_obj': request_obj})
        return 0

    def setup_and_build_request_lookup(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
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

    def setup_and_build_request_retrieve(self, input_file):
        pre_test_output = pre_test_worker_env(input_file)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_response=pre_test_output)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def setup_and_build_request_receipt(self, input_file):
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
        result_response = self.getresult(wo_submit)
        request_obj, action_obj = build_request_obj(
            input_file, pre_test_output=pre_test_output,
            pre_test_response=wo_submit)
        self.build_request_output.update(
            {'request_obj': request_obj,
             'pre_test_output': pre_test_output,
             'action_obj': action_obj})
        return 0

    def teardown(self):
        logger.info("**No Teardown Defined**\n%s\n")

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
            if env.test_mode == "listener":
                listener_instance = ListenerImpl()
                response = listener_instance.work_order_get_result(output_obj)
            else:
                sdk_instance = SDKImpl()
                response = sdk_instance.work_order_get_result(output_obj)
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
