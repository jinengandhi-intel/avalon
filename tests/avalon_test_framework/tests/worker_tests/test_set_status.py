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
import env
from src.libs.verification_libs \
    import validate_response_code
from src.libs.pre_processing_libs \
    import ResultStatus
from src.libs.avalon_test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_success(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_unknown_parameter(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_invalid_parameter(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_params_status_0(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_2(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_3(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_4(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_params_status_5(self):

        result_response = self.test_obj.run_test(env.worker_setstatus_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

        self.test_obj.teardown(env.worker_setstatus_input_file)

        logger.info('\t\t!!! Test completed !!!\n\n')
