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
    import check_worker_lookup_response, check_worker_retrieve_response, \
    validate_response_code
from src.utilities.worker_utilities \
    import ResultStatus, read_config
from src.libs.test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(env.worker_input_file, "worker_setstatus.ini")

    if env.proxy_mode:
        expected_response = 0
    else:
        expected_response = -32601

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_unknown_parameter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_invalid_parameter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_params_status_0(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_2(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_3(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_set_status_params_status_4(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_set_status_params_status_5(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (validate_response_code(result_response, self.expected_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
