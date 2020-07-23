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

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_inDataDataEncryptionKey_hyphenecho(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_datahash_null(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_null(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requester id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sessionkeyivInDataIv_hexstring(
            self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesternonce_specialcharacters(
            self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid data format for requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_invalid(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_workerEncryptionKey_special_character(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid dataformat for workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_workerencryptionkey_empty(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid dataformat for workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_dataencryptionalgorithm_alternate(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Unsupported dataEncryptionAlgorithm found in the request")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indexindata_50(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_index_orderchange(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_empty(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Indata is empty")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_remove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Indata is empty")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_outdata_empty(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_indata_unknownparametervalue(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for in/out data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_index_negative(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_indatahash_empty(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter index")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_datahash_randomstr(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_data_multipleechoresult(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_echoclient(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indata_alternatetextechoclient(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indata_specialcharacter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    # @pytest.mark.sdk
    def test_workordersubmit_iv_specialcharacterechoclient(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for initialization vector of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_requesterId_paramremove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter requesterId")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_responsetimeout_string(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for responseTimeoutMSecs")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_dataencryptionalgorithm_list(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for dataEncryptionAlgorithm")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadId_twoworkload(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderId_null(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workerId_nullstring(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for Worker id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadId_specialcharacters(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_encrypteddataencryptionkey_nullechoclient(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_dataencryptionalgorithm_listsamealgotwice(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for dataEncryptionAlgorithm")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_encrypteddataencryptionkey_hyphenechoclient(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_encrypteddataencryptionkey_remove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_outdata_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_indata_bothindexremoveDataDatahash(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_indata_oneValidOtherEmptDataDatahash(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for data hash of in data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_indata_singleindexremoveDataDatahash(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing in data parameter data")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index2randomstr(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid Request")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index1randomstr(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid Request")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_emptystring(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work load id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_hexstring(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_workload_nullstring(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Workload cannot be processed by this worker")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderid_increasedhexlength(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderidworkloadid_same(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_data_differentdataheartdisease(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_specialcharacter(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requester id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterNonce_param_empty(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Empty or Invalid data format for requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_requestersignature_differentlength(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for requesterSignature")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indataoutdata_success(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordersubmit_workorderId_remove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for work order id")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_sessionkeyiv_allspecial_characters(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for session key iv")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_differenthexlength(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterId")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_workerEncryptionKey_notdefaulthex(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter workerEncryptionKey")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterNonce_notdefaultlength(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterNonce")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_requesterSignature_no(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_encryptedRequestHash_no(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter encryptedRequestHash")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    def test_workordersubmit_mandatoryfields_remove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid params")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_id_remove(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Server error")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workeridworkloadid_same(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "worker 0xABCD doesn't exists")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_params_unknownparameter(self):

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

    @pytest.mark.listener
    def test_workordersubmit_workerId_notdefaultlength_postmsg(self):

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

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workerId_notdefaultlength(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            check_negative_test_responses(
                result_response,
                "worker "
                "6ba1f459476bc43b65fd554f6b65910a8f551e4bcb"
                "0eee6a96dcebaeb14f2ae923456234564567"
                "doesn't exists")
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_payloadFormat_notJSONRPC(self):

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

    @pytest.mark.listener
    def test_workordersubmit_params_empty(self):

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

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_OutDataDataEncryptionKey_hyphen(self):

        result_response = self.test_obj.run_test(self.config_file)

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_params_twiceechoclient(self):

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

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_dataencryptionalgorithm_list(self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):

            result_response = self.test_obj.run_test(self.config_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workordersubmit_methodname_list(self):
        result_response = self.test_obj.run_test(self.config_file)

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

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerencryptionkey_empty(self):
        with pytest.raises(
                ValueError,
                match="Empty or Invalid dataformat for workerEncryptionKey"):

            result_response = self.test_obj.run_test(self.config_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerEncryptionKey_special_character(self):
        with pytest.raises(ValueError,
                           match="Encrypting Session key failed: "
                                 "Invalid session key or worker encryption key"):
            result_response = self.test_obj.run_test(self.config_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_dataencryptionalgorithm_listsamealgotwice(
            self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):

            result_response = self.test_obj.run_test(self.config_file)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerEncryptionKey_notdefaulthex(self):
        with pytest.raises(TypeError,
                           match="Worker Encryption Key not valid"):

            result_response = self.test_obj.run_test(self.config_file)

        logger.info('\t\t!!! Test completed !!!\n\n')