import pytest
import logging
import os
import globals
import json
from src.libs.avalon_test_wrapper \
    import read_json, submit_request
from src.libs.test_base import TestBase
from src.utilities.verification_utils \
    import verify_test, check_negative_test_responses
from src.utilities.generic_utils import TestStep
from src.utilities.generic_utils import GetResultWaitTime
import time
logger = logging.getLogger(__name__)


class TestClass():
    test_obj = TestBase()

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult
    @pytest.mark.sdk
    def test_workordergetresult(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_getresult.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
            verify_test(
                submit_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_different
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_different(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_different.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid work order Id")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_specialchar
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_specialchar(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_specialchar.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid work order Id")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_null
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_null(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid work order Id")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_nonhexstring
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_nonhexstring(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_nonhexstring.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Work order Id not found in the database. Hence invalid parameter")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_alphabetsonly
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_alphabetsonly(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_alphabetsonly.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid work order Id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_workorderid_withoutquotes
    @pytest.mark.sdk
    def test_workordergetresult_workorderid_withoutquotes(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderid_withoutquotes.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid params")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_emptyparameter
    def test_workordergetresult_emptyparameter(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_emptyparameter.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)

        assert (validate_response_code(submit_response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordergetresult
    @pytest.mark.test_workordergetresult_unknownparameter
    def test_workordergetresult_unknownparameter(self):
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_unknownparameter.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_getresult(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        logger.info("submit_response: \n%s\n", submit_response)


        assert (validate_response_code(submit_response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordergetresult
    @pytest.mark.listener
    @pytest.mark.test_workordergetresult_workorderId_empty
    def test_workordergetresult_workorderId_empty(self):
        test_id = '18729'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordergetresult_workorderId_empty.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", msg_response)

        assert (
                check_negative_test_responses(
                    msg_response,
                    "Invalid work order Id")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
