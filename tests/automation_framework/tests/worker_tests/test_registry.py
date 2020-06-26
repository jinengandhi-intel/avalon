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
    @pytest.mark.worker_register
    @pytest.mark.listener
    @pytest.mark.positive
    def test_worker_register_success(self):
        test_id = '18262'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_register.json")

        err_cd = self.test_obj.setup_and_build_request_lookup(
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
    @pytest.mark.worker_register
    @pytest.mark.listener
    @pytest.mark.negative
    def test_worker_register_unknown_parameter(self):
        test_id = '18263'
        request_file = os.path.join(
            env.worker_input_file,
            "worker_register_unknown_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_lookup(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_workerregister_hashingAlgorithm_KECCAK256(self):
        test_id = '18881'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_hashingAlgorithm_KECCAK_256.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_workerregister_signingAlgorithm_RSAOAEP3072(self):
        test_id = '18883'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_signingAlgorithm_RSA_OAEP_3072.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_dataEncryptionAlgorithm_list(self):
        test_id = '18886'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_dataEncryptionAlgorithm_list.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_workerregister_orgnizationid_32bytes(self):
        test_id = '18892'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_orgnizationid_32bytes.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_workerregister_applicationTypeId_32bytes(self):
        test_id = '18893'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_applicationTypeId_32bytes.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_workOrderPayloadFormats_JSONRPCJWT(self):
        test_id = '18894'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_workOrderPayloadFormats_JSON_RPC_JWT.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_workerId_null(self):
        test_id = '18880'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_workerId_null.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_hashingAlgorithm_alternate(self):
        test_id = '18882'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_hashingAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_signingAlgorithm_alternate(self):
        test_id = '18884'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_signingAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_keyEncryptionAlgorithm_alternate(self):
        test_id = '18885'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_keyEncryptionAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_dataEncryptionAlgorithm_alternate(self):
        test_id = '18887'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_dataEncryptionAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workerregister_workerType_invalid(self):
        test_id = '18888'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_workerType_invalid.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_organizationId_empty(self):
        test_id = '18889'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_organizationId_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_applicationTypeId_empty(self):
        test_id = '18890'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_applicationTypeId_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.positive
    def test_workerregister_proofDataType_empty(self):
        test_id = '18281'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_proofDataType_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_proofDataType_invalid(self):
        test_id = '20362'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_proofDataType_invalid.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.negative
    def test_workerregister_proofDataType_null(self):
        test_id = '20363'
        request_file = os.path.join(
            env.worker_input_file,
            "workerregister_proofDataType_null.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
