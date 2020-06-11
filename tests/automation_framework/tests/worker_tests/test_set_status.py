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
import globals
from src.utilities.verification_utils \
    import check_worker_lookup_response, check_worker_retrieve_response, \
    validate_response_code
from src.libs.avalon_test_wrapper \
    import read_json, submit_request
from src.utilities.generic_utils import TestStep
from src.libs.test_base import TestBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = TestBase()

    @pytest.mark.worker
    @pytest.mark.listener
    def test_worker_set_status(self):
        test_id = '18268'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 0)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    def test_worker_set_status_unknown_parameter(self):
        test_id = '18269'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_unknown_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    def test_worker_set_status_invalid_parameter(self):
        test_id = '18270'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_invalid_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    @pytest.mark.set1
    def test_worker_set_status_params_status_0(self):
        test_id = '18287'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_params_status_0.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    @pytest.mark.set1
    def test_worker_set_status_params_status_2(self):
        test_id = '18289'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_params_status_2.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 0)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    @pytest.mark.set1
    def test_worker_set_status_params_status_3(self):
        test_id = '18290'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_params_status_3.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 0)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    @pytest.mark.set1
    def test_worker_set_status_params_status_4(self):
        test_id = '18291'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_params_status_4.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 0)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.worker
    @pytest.mark.listener
    @pytest.mark.set1
    def test_worker_set_status_params_status_5(self):
        test_id = '18292'
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_set_status_params_status_5.json")

        err_cd = self.test_obj.setup_and_build_request_worker_status(
            read_json(request_file))

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.worker_lookup_output_json_file_name,
            read_json(request_file))

        logger.info("**********Received Response*********\n%s\n", response)

        assert (validate_response_code(response, 2)
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

