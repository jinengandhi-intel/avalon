# Copyright 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import logging
import os
import env
from src.utilities.verification_utils \
    import check_worker_lookup_response
from src.utilities.worker_utilities \
    import ResultStatus, read_config
from src.utilities.verification_utils \
    import check_negative_test_responses
import operator
from src.libs.test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(env.worker_input_file, "worker_lookup.ini")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_lookup_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (check_worker_lookup_response(result_response, operator.gt, 0)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_lookup_workerType_not_unsigned_int(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "WorkType should be an Integer of range 1-3") is
            ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_empty_params(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (check_negative_test_responses(result_response,
                                              "Empty params in the request")
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_jsonrpc_different_version(self):
        

        request_file = os.path.join(
            env.worker_input_file,
            "worker_lookup_jsonrpc_different_version.json")

        response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", response)

        assert (
            check_negative_test_responses(
                response,
                "Improper Json request Missing or Invalid parameter or value")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_withoutid_params(self):
        

        request_file = os.path.join(
            env.worker_input_file,
            "worker_lookup_withoutid_params.json")

        response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", response)

        assert (
            check_negative_test_responses(
                response,
                "Improper Json request Missing or Invalid parameter or value")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_diff_unit_length(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (check_worker_lookup_response(result_response, operator.eq, 0)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_method_field_change(self):
        

        request_file = os.path.join(
            env.worker_input_file,
            "worker_lookup_method_field_change.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", msg_response)

        assert (
            check_negative_test_responses(
                msg_response,
                "Improper Json request Missing or Invalid parameter or value")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_lookup_twice_params(self):
        

        request_file = os.path.join(
            env.worker_input_file,
            "worker_lookup_twice_params.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", msg_response)

        assert (
            check_negative_test_responses(
                msg_response,
                "Duplicate parameter params")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workerlookup_params_unknownparameter(self):
        

        request_file = os.path.join(
            env.worker_input_file,
            "workerlookup_params_unknownparameter.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        logger.info("**********Received Response*********\n%s\n", msg_response)

        assert (
            check_negative_test_responses(
                msg_response,
                "Invalid parameter unknownEncoding")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
