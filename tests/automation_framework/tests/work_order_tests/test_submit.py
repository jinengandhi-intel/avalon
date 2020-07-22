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
from src.libs.avalon_test_wrapper \
    import submit_request
from src.libs.test_base import AvalonBase
from src.utilities.verification_utils \
    import verify_test, check_negative_test_responses
from src.utilities.worker_utilities \
    import ResultStatus, read_config
logger = logging.getLogger(__name__)


class TestClass():
    test_obj = AvalonBase()
    config_file = os.path.join(
        env.work_order_input_file, "work_order_submit.ini")

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.p1
    @pytest.mark.positive
    def test_workordersubmit_success(self):
        test_id = '18697'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_inDataDataEncryptionKey_hyphenecho(self):
        test_id = '18783'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_datahash_null(self):
        test_id = '18713'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_requesterId_null(self):
        test_id = '18739'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requester id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_sessionkeyivInDataIv_hexstring(
            self):
        test_id = '18738'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_requesternonce_specialcharacters(
            self):
        test_id = '18736'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid data format for requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workloadid_invalid(self):
        test_id = '18807'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_methodname_list(self):
        test_id = '18797'

        test_data = read_config(self.config_file, test_id)

        # err_cd = \
        #    self.test_obj.setup_and_build_request_wo_submit(
        #        test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            test_data,
            env.wo_submit_output_json_file_name,
            test_data)

        # result_response = self.test_obj.getresult(
        #     self.test_obj.build_request_output['request_obj'])

        assert (
            check_negative_test_responses(
                submit_response,
                "Invalid Request")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workerEncryptionKey_special_character(self):
        test_id = '18732'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid dataformat for workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_sdk_workerEncryptionKey_special_character(self):
        with pytest.raises(ValueError,
                           match="Encrypting Session key failed: "
                           "Invalid session key or worker encryption key"):
            test_id = '21228'

            test_data = read_config(self.config_file, test_id)

            self.test_obj.setup_and_build_request_wo_submit(
                test_data)

            submit_response = submit_request(
                self.test_obj.uri_client,
                self.test_obj.build_request_output['request_obj'],
                env.wo_submit_output_json_file_name,
                test_data)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workerencryptionkey_empty(self):
        test_id = '18705'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid dataformat for workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_sdk_workerencryptionkey_empty(self):
        with pytest.raises(
                ValueError,
                match="Empty or Invalid dataformat for workerEncryptionKey"):
            test_id = '21229'
            test_data = read_config(self.config_file, test_id)

            self.test_obj.setup_and_build_request_wo_submit(
                test_data)

            submit_response = submit_request(
                self.test_obj.uri_client,
                self.test_obj.build_request_output['request_obj'],
                env.wo_submit_output_json_file_name,
                test_data)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk_1
    @pytest.mark.negative
    def test_workordersubmit_dataencryptionalgorithm_alternate(self):
        test_id = '18706'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Unsupported dataEncryptionAlgorithm found in the request")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    def test_workordersubmit_indexindata_50(self):
        test_id = '18707'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_index_orderchange(self):
        test_id = '18708'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk_1
    @pytest.mark.negative
    def test_workordersubmit_indata_empty(self):
        test_id = '18765'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Indata is empty")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk_1
    @pytest.mark.negative
    def test_workordersubmit_indata_remove(self):
        test_id = '18766'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter inData")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_outdata_empty(self):
        test_id = '18711'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_indata_unknownparametervalue(self):
        test_id = '18768'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for in/out data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_index_negative(self):
        test_id = '18769'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_indatahash_empty(self):
        test_id = '18712'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter index")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_datahash_randomstr(self):
        test_id = '18772'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_data_multipleechoresult(self):
        test_id = '18774'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_echoclient(self):
        test_id = '18808'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_indata_alternatetextechoclient(self):
        test_id = '18809'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_indata_specialcharacter(self):
        test_id = '18810'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    # @pytest.mark.sdk
    def test_workordersubmit_iv_specialcharacterechoclient(self):
        test_id = '18786'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for initialization vector of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_requesterId_paramremove(self):
        test_id = '18733'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter requesterId")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_responsetimeout_string(self):
        test_id = '18798'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for responseTimeoutMSecs")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_dataencryptionalgorithm_list(self):
        test_id = '18793'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for dataEncryptionAlgorithm")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_sdk_dataencryptionalgorithm_list(self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):
            test_id = '21231'
            test_data = read_config(self.config_file, test_id)

            self.test_obj.setup_and_build_request_wo_submit(
                test_data)

            submit_response = submit_request(
                self.test_obj.uri_client,
                self.test_obj.build_request_output['request_obj'],
                env.wo_submit_output_json_file_name,
                test_data)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.positive
    def test_workordersubmit_workloadId_twoworkload(self):
        test_id = '18805'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.p1
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_workorderId_null(self):
        test_id = '18717'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_workerId_nullstring(self):
        test_id = '18718'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for Worker id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_workloadId_specialcharacters(self):
        test_id = '18730'

        test_data = read_config(self.config_file, test_id)
        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.positive
    def test_workordersubmit_encrypteddataencryptionkey_nullechoclient(self):
        test_id = '18785'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_dataencryptionalgorithm_listsamealgotwice(self):
        test_id = '18788'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for dataEncryptionAlgorithm")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_sdk_dataencryptionalgorithm_listsamealgotwice(
            self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):
            test_id = '21230'
            test_data = read_config(self.config_file, test_id)

            self.test_obj.setup_and_build_request_wo_submit(
                test_data)

            submit_response = submit_request(
                self.test_obj.uri_client,
                self.test_obj.build_request_output['request_obj'],
                env.wo_submit_output_json_file_name,
                test_data)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.set1
    @pytest.mark.positive
    def test_workordersubmit_encrypteddataencryptionkey_hyphenechoclient(self):
        test_id = '20366'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.set1
    @pytest.mark.negative
    def test_workordersubmit_encrypteddataencryptionkey_remove(self):
        test_id = '18754'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_outdata_success(self):
        test_id = '18710'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_indata_bothindexremoveDataDatahash(self):
        test_id = '18714'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_indata_oneValidOtherEmptDataDatahash(self):
        test_id = '18715'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_indata_singleindexremoveDataDatahash(self):
        test_id = '18716'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk_1
    @pytest.mark.negative
    def test_workordersubmit_indata_index2randomstr(self):
        test_id = '18719'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid Request")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk_1
    @pytest.mark.negative
    def test_workordersubmit_indata_index1randomstr(self):
        test_id = '18720'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid Request")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workloadid_emptystring(self):
        test_id = '18722'

        test_data = read_config(self.config_file, test_id)
        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work load id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workloadid_hexstring(self):
        test_id = '18723'

        test_data = read_config(self.config_file, test_id)
        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workload_nullstring(self):
        test_id = '18726'

        test_data = read_config(self.config_file, test_id)
        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workorderid_increasedhexlength(self):
        test_id = '18727'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workorderidworkloadid_same(self):
        test_id = '18728'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_data_differentdataheartdisease(self):
        test_id = '18731'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_requesterId_specialcharacter(self):
        test_id = '18734'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requester id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_requesterNonce_param_empty(self):
        test_id = '18735'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid data format for requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_requestersignature_differentlength(self):
        test_id = '18492'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requesterSignature")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_indataoutdata_success(self):
        test_id = '18703'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workorderId_remove(self):
        test_id = '18725'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_sessionkeyiv_allspecial_characters(self):
        test_id = '18737'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for session key iv")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_requesterId_differenthexlength(self):
        test_id = '18742'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterId")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workerEncryptionKey_notdefaulthex(self):
        test_id = '18743'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_sdk_workerEncryptionKey_notdefaulthex(self):
        with pytest.raises(TypeError,
                           match="Worker Encryption Key not valid"):
            test_id = '18743'
            test_data = read_config(self.config_file, test_id)

            self.test_obj.setup_and_build_request_wo_submit(
                test_data)

            submit_response = submit_request(
                self.test_obj.uri_client,
                self.test_obj.build_request_output['request_obj'],
                env.wo_submit_output_json_file_name,
                test_data)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_requesterNonce_notdefaultlength(self):
        test_id = '18745'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.positive
    def test_workordersubmit_requesterSignature_no(self):
        test_id = '18613'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_encryptedRequestHash_no(self):
        test_id = '18777'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter encryptedRequestHash")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.negative
    def test_workordersubmit_mandatoryfields_remove(self):
        test_id = '18781'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid params")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_id_remove(self):
        test_id = '18787'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "Server error")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workeridworkloadid_same(self):
        test_id = '18794'

        test_data = read_config(self.config_file, test_id)
        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "worker 0xABCD doesn't exists")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_params_unknownparameter(self):
        test_id = '18700'

        request_file = os.path.join(
            env.work_order_input_file,
            "workordersubmit_params_unknownparameter.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        assert (
            check_negative_test_responses(
                msg_response,
                "Invalid parameter unknownEncoding")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_workerId_notdefaultlength_postmsg(self):
        test_id = '20365'

        request_file = os.path.join(
            env.work_order_input_file,
            "workordersubmit_workerId_notdefaultlength_postmsg.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        assert (
            check_negative_test_responses(
                msg_response,
                "worker "
                "6ba1f459476bc43b65fd554f6b65910a8f551e4bcb0"
                "eee6a96dcebaeb14f2ae923456234564567 "
                "doesn't exists")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_workerId_notdefaultlength(self):
        test_id = '18741'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            check_negative_test_responses(
                result_response,
                "worker "
                "6ba1f459476bc43b65fd554f6b65910a8f551e4bcb"
                "0eee6a96dcebaeb14f2ae923456234564567"
                "doesn't exists")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.negative
    def test_workordersubmit_payloadFormat_notJSONRPC(self):
        test_id = '18750'

        request_file = os.path.join(
            env.work_order_input_file,
            "workordersubmit_payloadFormat_notJSONRPC.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        assert (
            check_negative_test_responses(
                msg_response,
                "Invalid payload format")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_params_empty(self):
        test_id = '18762'

        request_file = os.path.join(
            env.work_order_input_file,
            "workordersubmit_params_empty.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        assert (
            check_negative_test_responses(
                msg_response,
                "Invalid parameter params")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.fabric
    @pytest.mark.ethereum
    @pytest.mark.positive
    def test_workordersubmit_OutDataDataEncryptionKey_hyphen(self):
        test_id = '18784'

        test_data = read_config(self.config_file, test_id)

        self.test_obj.setup_and_build_request_wo_submit(
            test_data)

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            env.wo_submit_output_json_file_name,
            test_data)

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'],
            submit_response)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.listener
    @pytest.mark.negative
    def test_workordersubmit_params_twiceechoclient(self):
        test_id = '18791'

        request_file = os.path.join(
            env.work_order_input_file,
            "workordersubmit_params_twiceechoclient.json")

        msg_response = self.test_obj.post_json_msg(request_file)

        assert (
            check_negative_test_responses(
                msg_response,
                "Duplicate parameter params")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
