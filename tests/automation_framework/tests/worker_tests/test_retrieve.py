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
from src.worker_lookup.worker_lookup_params \
    import WorkerLookUp
from src.utilities.verification_utils \
    import check_worker_lookup_response, check_worker_retrieve_response, \
    validate_response_code, check_negative_test_responses
from src.libs.avalon_test_wrapper \
    import submit_request
from src.utilities.worker_utilities \
    import ResultStatus, read_config
from src.libs.test_base import AvalonBase

logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(env.worker_input_file, "worker_retrieve.ini")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_retrieve_success(self):
        test_id = '18273'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_retrieve(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        assert (check_worker_retrieve_response(submit_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_retrieve_empty_params(self):
        test_id = '18274'
        test_data = read_config(self.config_file, test_id)

        request_file = os.path.join(
            env.worker_input_file,
            "worker_retrieve_empty_params.json")

        err_cd = self.test_obj.setup_and_build_request_worker_retrieve(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        assert (
            check_negative_test_responses(
                submit_response,
                "Worker Id not found")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workerretrieve_params_unknownparameter(self):
        test_id = '20591'
        test_data = read_config(self.config_file, test_id)

        request_file = os.path.join(
            env.worker_input_file,
            "workerretrieve_params_unknownparameter.json")

        err_cd = self.test_obj.setup_and_build_request_worker_retrieve(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        assert (
            check_negative_test_responses(
                submit_response,
                "Invalid parameter unknownEncoding")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
