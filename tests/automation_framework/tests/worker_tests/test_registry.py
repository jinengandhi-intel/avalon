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
    @pytest.mark.worker_register
    @pytest.mark.test_worker_register
    @pytest.mark.listener
    def test_worker_register(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_register.json")

        err_cd = self.test_obj.setup_and_build_request_lookup(
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
    @pytest.mark.worker_register
    @pytest.mark.test_worker_register_unknown_parameter
    @pytest.mark.listener
    def test_worker_register_unknown_parameter(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "worker_register_unknown_parameter.json")

        err_cd = self.test_obj.setup_and_build_request_lookup(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_hashingAlgorithm_KECCAK256
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_hashingAlgorithm_KECCAK256(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_hashingAlgorithm_KECCAK_256.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_signingAlgorithm_RSAOAEP3072
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_signingAlgorithm_RSAOAEP3072(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_signingAlgorithm_RSA_OAEP_3072.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_dataEncryptionAlgorithm_list
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_dataEncryptionAlgorithm_list(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_dataEncryptionAlgorithm_list.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_orgnizationid_32bytes
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_orgnizationid_32bytes(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_orgnizationid_32bytes.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_applicationTypeId_32bytes
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_applicationTypeId_32bytes(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_applicationTypeId_32bytes.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_workOrderPayloadFormats_JSONRPCJWT
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_workOrderPayloadFormats_JSONRPCJWT(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_workOrderPayloadFormats_JSON_RPC_JWT.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_workerId_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_workerId_null(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_workerId_null.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_hashingAlgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_hashingAlgorithm_alternate(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_hashingAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_signingAlgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_signingAlgorithm_alternate(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_signingAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_keyEncryptionAlgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_keyEncryptionAlgorithm_alternate(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_keyEncryptionAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_dataEncryptionAlgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_dataEncryptionAlgorithm_alternate(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_dataEncryptionAlgorithm_alternate.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_workerType_invalid
    @pytest.mark.listener
    def test_workerregister_workerType_invalid(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_workerType_invalid.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_organizationId_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_organizationId_empty(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_organizationId_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_applicationTypeId_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_applicationTypeId_empty(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_applicationTypeId_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_proofDataType_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_empty(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_proofDataType_empty.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_proofDataType_invalid
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_invalid(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_proofDataType_invalid.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
    @pytest.mark.workerregister
    @pytest.mark.test_workerregister_proofDataType_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workerregister_proofDataType_null(self):
        request_file = os.path.join(
            globals.worker_input_file,
            "workerregister_proofDataType_null.json")

        err_cd = self.test_obj.setup_and_build_request_register(
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
