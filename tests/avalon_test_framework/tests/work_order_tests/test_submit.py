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
from src.libs.avalon_test_base import AvalonBase
from src.libs.verification_libs \
    import verify_test, check_negative_test_responses
from src.libs.pre_processing_libs \
    import ResultStatus
from conftest import env, error_string

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_teardown")
class TestClass():
    test_obj = AvalonBase()
    pytestmark = pytest.mark.setup_teardown_data(
        test_obj, "WorkOrderSubmit")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_success(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_inDataDataEncryptionKey_hyphenecho(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_datahash_null(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_datahash"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_null(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_requesterid"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sessionkeyivInDataIv_hexstring(
            self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesternonce_specialcharacters(
            self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_requesternonce"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_invalid(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_notsupported_workload"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_workerEncryptionKey_special_character(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workerencryptionkey"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_workerencryptionkey_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workerencryptionkey"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_dataencryptionalgorithm_alternate(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Unsupported dataEncryptionAlgorithm found in the request")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indexindata_50(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_index_orderchange(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["empty_indata"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_remove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["empty_indata"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_outdata_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_indata_unknownparametervalue(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_indata_outdata"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_index_negative(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_indatahash_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_indata_index"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_datahash_randomstr(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_datahash"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_data_multipleechoresult(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_echoclient(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indata_alternatetextechoclient(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indata_specialcharacter(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_iv_specialcharacterechoclient(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_indata_iv"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_requesterId_paramremove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_requesterid"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_responsetimeout_string(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_responsetimeout"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_dataencryptionalgorithm_list(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_dataencryptionalgorithm"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadId_twoworkload(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderId_null(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_worklorderid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workerId_nullstring(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workerid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadId_specialcharacters(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_notsupported_workload"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_encrypteddataencryptionkey_nullechoclient(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_dataencryptionalgorithm_listsamealgotwice(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_dataencryptionalgorithm"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_encrypteddataencryptionkey_hyphenechoclient(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_encrypteddataencryptionkey_remove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_outdata_success(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_indata_bothindexremoveDataDatahash(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["mising_indata_data"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_oneValidOtherEmptDataDatahash(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_datahash"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_indata_singleindexremoveDataDatahash(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["mising_indata_data"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index2randomstr(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index1randomstr(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_emptystring(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workloadid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workloadid_hexstring(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_notsupported_workload"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_workload_nullstring(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_notsupported_workload"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderid_increasedhexlength(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_worklorderid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workorderidworkloadid_same(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_worklorderid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_data_differentdataheartdisease(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_specialcharacter(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_requesterid"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterNonce_param_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_requesternonce"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_requestersignature_differentlength(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_requestersignature"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_indataoutdata_success(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.sdk
    @pytest.mark.proxy
    @pytest.mark.listener
    def test_workordersubmit_workorderId_remove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_worklorderid_dataformat"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_sessionkeyiv_allspecial_characters(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for session key iv")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterId_differenthexlength(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterId")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_workerEncryptionKey_notdefaulthex(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workerencryptionkey"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_requesterNonce_notdefaultlength(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter requesterNonce")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_requesterSignature_no(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_encryptedRequestHash_no(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Missing parameter encryptedRequestHash")
            is ResultStatus.SUCCESS.value)

    def test_workordersubmit_mandatoryfields_remove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid params")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_id_remove(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_invalid_params"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workeridworkloadid_same(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                "worker 0xABCD doesn't exists")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_params_unknownparameter(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["unknown_params"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_workerId_notdefaultlength_postmsg(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_doesnot_exist"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_workerId_notdefaultlength(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["worker_doesnot_exist"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_payloadFormat_notJSONRPC(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_payload"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workordersubmit_params_empty(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                "Server error")
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_OutDataDataEncryptionKey_hyphen(self):

        result_response = self.test_obj.run_test(
            env['work_order_submit_input_file'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.setup_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_dataencryptionalgorithm_list(self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):

            result_response = self.test_obj.run_test(
                env['work_order_submit_input_file'])

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerencryptionkey_empty(self):
        with pytest.raises(
                ValueError,
                match=error_string["invalid_workerencryptionkey"]):

            result_response = self.test_obj.run_test(
                env['work_order_submit_input_file'])

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerEncryptionKey_special_character(self):
        with pytest.raises(ValueError,
                           match="Encrypting Session key failed: "
                                 "Invalid session key or worker encryption key"):
            result_response = self.test_obj.run_test(
                env['work_order_submit_input_file'])

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_dataencryptionalgorithm_listsamealgotwice(
            self):
        with pytest.raises(
                ValueError,
                match="Data Encryption Algorithm is not String"):

            result_response = self.test_obj.run_test(
                env['work_order_submit_input_file'])

    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_workordersubmit_sdk_workerEncryptionKey_notdefaulthex(self):
        with pytest.raises(TypeError,
                           match="Worker Encryption Key not valid"):

            result_response = self.test_obj.run_test(
                env['work_order_submit_input_file'])
