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
from src.libs import constants
from src.libs.avalon_test_wrapper \
    import read_json, submit_request
from src.libs.test_base import TestBase
from src.utilities.verification_utils \
    import verify_test, check_negative_test_responses
from src.utilities.generic_utils import TestStep
logger = logging.getLogger(__name__)


class TestClass():
    test_obj = TestBase()

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_success
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.p1
    def test_work_order_success(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_success.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_inData_DataEncryptionKey_hyphen_echo
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_inData_DataEncryptionKey_hyphen_echo(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_inData_DataEncryptionKey_hyphen_echo.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_data_datahash_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_data_datahash_null(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_data_datahash_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_submit_requesterId_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_submit_requesterId_null(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_requester_id_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_submit_sessionkeyiv_and_iv_indata_hex_string
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_submit_sessionkeyiv_and_iv_indata_hex_string(
            self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_iv_indata_hex_string.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_get_result
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_get_result(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_get_result.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_verify_signature
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_verify_signature(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_verify_signature.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_submit_requesterNonce_all_special_characters
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_submit_requesterNonce_all_special_characters(
            self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_submit_requesterNonce_all_special_characters.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_alternate_worker_signing_algorithm
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_alternate_worker_signing_algorithm(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_alternate_worker_signing_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_alternate_hashing_algorithm
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_alternate_hashing_algorithm(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_alternate_hashing_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_without_requester_private_key
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_without_requester_private_key(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_without_requester_private_key.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_submit_twice_params
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_submit_twice_params(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_submit_twice_params.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_Submit_invalid_parameter_Workloadid
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_Submit_invalid_parameter_Workloadid(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_Submit_invalid_parameter_Workloadid.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Invalid workload id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_methodename_list
    @pytest.mark.listener
    def test_work_order_methodename_list(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_methodename_list.json")

        # err_cd = \
        #    self.test_obj.setup_and_build_request_wo_submit(
        #        read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            read_json(request_file),
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        # result_response = self.test_obj.getresult(
        #     self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid Request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_signing_wrong
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_signing_wrong(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_signing_wrong.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid Request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_workerEncryptionKey_special_character
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_workerEncryptionKey_special_character(self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_workerEncryptionKey_special_character.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid Request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_worker_encryption_key
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_worker_encryption_key (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_worker_encryption_key.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_alternate_dataEncryption_algorithm
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_alternate_dataEncryption_algorithm (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_alternate_dataEncryption_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Unsupported dataEncryptionAlgorithm found in the request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_50_index_indata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_50_index_indata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_50_index_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_changing_order_index
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_changing_order_index (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_changing_order_index.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_index0_indata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_index0_indata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_index0_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_empty_indata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_empty_indata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_empty_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Indata is empty")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_no_indata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_no_indata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_no_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing parameter inData")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_empty_indata_outdata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_empty_indata_outdata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_empty_indata_outdata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Indata is empty")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')



    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_indata_unknown_parameter_value
    @pytest.mark.listener
    # @pytest.mark.sdk (AttributeError: 'dict' object has no attribute 'to_jrpc_string)
    def test_work_order_with_indata_unknown_parameter_value (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_indata_unknown_parameter_value.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        # submit_response = submit_request(
        #     self.test_obj.uri_client,
        #     read_json(request_file),
        #     constants.wo_submit_output_json_file_name,
        #     read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        # result_response = self.test_obj.getresult(
        #     self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Server error")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_negative_index
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_negative_index (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_negative_index.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_empty_indata_hash
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_with_empty_indata_hash (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_empty_indata_hash.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_data_datahash_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_data_datahash_null (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_data_datahash_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_datahash_random_str
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_datahash_random_str (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_datahash_random_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_multiple_data_echoresult
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_multiple_data_echoresult (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_multiple_data_echoresult.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_echoclient
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_echoclient (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_echoclient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_diff_text_data_indata_echoClient
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_diff_text_data_indata_echoClient (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_diff_text_data_indata_echoClient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_specialcharacter_data_single_index_indata
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_specialcharacter_data_single_index_indata (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_specialcharacter_data_single_index_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_special_char_iv_echoresult
    @pytest.mark.listener
    # @pytest.mark.sdk
    def test_work_order_special_char_iv_echoresult (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_special_char_iv_echoresult.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for initialization vector of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_submit_requesterId_param_remove
    @pytest.mark.listener
    def test_work_order_submit_requesterId_param_remove (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_submit_requesterId_param_remove.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing parameter requesterId")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.work_order_submit
    @pytest.mark.test_work_order_with_response_timeout_str
    @pytest.mark.listener
    def test_work_order_with_response_timeout_str (self):
        request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_with_response_timeout_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            constants.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for responseTimeoutMSecs")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')