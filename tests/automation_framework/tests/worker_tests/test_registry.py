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
    config_file = os.path.join(env.worker_input_file, "worker_register.ini")

    @pytest.mark.listener
    def test_worker_register_success(self):
        test_id = '18262'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_worker_register_unknown_parameter(self):
        test_id = '18263'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_hashingAlgorithm_KECCAK256(self):
        test_id = '18881'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_signingAlgorithm_RSAOAEP3072(self):
        test_id = '18883'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_dataEncryptionAlgorithm_list(self):
        test_id = '18886'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_orgnizationid_32bytes(self):
        test_id = '18892'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_applicationTypeId_32bytes(self):
        test_id = '18893'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_workOrderPayloadFormats_JSONRPCJWT(self):
        test_id = '18894'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_workerId_null(self):
        test_id = '18880'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_hashingAlgorithm_alternate(self):
        test_id = '18882'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_signingAlgorithm_alternate(self):
        test_id = '18884'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_keyEncryptionAlgorithm_alternate(self):
        test_id = '18885'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_dataEncryptionAlgorithm_alternate(self):
        test_id = '18887'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workerregister_workerType_invalid(self):
        test_id = '18888'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_organizationId_empty(self):
        test_id = '18889'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_applicationTypeId_empty(self):
        test_id = '18890'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_empty(self):
        test_id = '21238'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_invalid(self):
        test_id = '20362'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_null(self):
        test_id = '20363'
        test_data = read_config(self.config_file, test_id)

        err_cd = self.test_obj.setup_and_build_request_worker_register(
            test_data)

        response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.worker_lookup_output_json_file_name,
            test_data)

        assert (validate_response_code(response, -32601)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
