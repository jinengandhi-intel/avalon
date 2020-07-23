import pytest
import logging
import os
import env
from src.libs.test_base import AvalonBase
from src.utilities.verification_utils \
    import verify_test, check_negative_test_responses,\
    validate_response_code
from src.utilities.worker_utilities \
    import ResultStatus, GetResultWaitTime, read_config
logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(
        env.work_order_input_file, "work_order_get_result.ini")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordergetresult_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_different(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_specialchar(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_null(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_nonhexstring(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Work order Id not found in the database. "
                "Hence invalid parameter")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_alphabetsonly(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_workorderid_withoutquotes(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_emptyparameter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, 2)
                is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordergetresult_unknownparameter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, 2)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordergetresult_workorderId_empty(self):

        request_file = os.path.join(
            env.work_order_input_file,
            "workordergetresult_workorderId_empty.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", msg_response)

        assert (
            check_negative_test_responses(
                msg_response,
                "Invalid work order Id")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
