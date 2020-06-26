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
    import read_json, submit_request
from src.utilities.worker_utilities import ResultStatus
from src.libs.test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_worker_update_success(self):
        test_id = '18265'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_update.json")

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response,-32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_worker_update_unknown_parameter(self):
        test_id = '18266'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_update_unknown_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response,-32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_worker_update_invalid_parameter(self):
        test_id = '18267'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_update_invalid_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.worker_update
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_worker_update_empty_details(self):
        test_id = '18293'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_update_empty_details.json")

        err_cd = self.test_obj.setup_and_build_request_worker_update(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


