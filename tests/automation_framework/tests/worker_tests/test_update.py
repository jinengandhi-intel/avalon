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
from src.libs.avalon_test_wrapper \
    import submit_request
from src.utilities.worker_utilities \
    import ResultStatus, read_config
from src.libs.test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(env.worker_input_file, "worker_update.ini")

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_worker_update_success(self):
        test_id = '18265'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        logger.info("**********Received Response*********\n%s\n", response)
        if env.proxy_mode:
            response_code = 0
        else:
            response_code = -32601

        assert (validate_response_code(response, response_code)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_worker_update_unknown_parameter(self):
        test_id = '18266'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        logger.info("**********Received Response*********\n%s\n", response)

        if env.proxy_mode:
            response_code = 0
        else:
            response_code = -32601

        assert (validate_response_code(response, response_code)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_worker_update_invalid_parameter(self):
        test_id = '18267'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        logger.info("**********Received Response*********\n%s\n", response)

        if env.proxy_mode:
            response_code = 0
        else:
            response_code = -32601

        assert (validate_response_code(response, response_code)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_worker_update_empty_details(self):
        test_id = '18293'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        logger.info("**********Received Response*********\n%s\n", response)

        if env.proxy_mode:
            response_code = 0
        else:
            response_code = -32601

        assert (validate_response_code(response, response_code)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


