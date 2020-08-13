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
from src.libs.verification_libs \
    import check_worker_lookup_response
from src.libs.verification_libs \
    import check_negative_test_responses
import operator
from src.libs.pre_processing_libs import ResultStatus
from src.libs.avalon_test_base import AvalonBase
from conftest import env, error_string

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_teardown")
class TestClass():
    test_obj = AvalonBase()
    pytestmark = pytest.mark.setup_teardown_data(
        test_obj, "WorkerLookUp")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_lookup_success(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'])

        assert (check_worker_lookup_response(result_response, operator.gt, 0)
                is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_lookup_workerType_not_unsigned_int(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'])

        assert (
            check_negative_test_responses(
                result_response,
                error_string["invalid_workertype"]) is
            ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_worker_lookup_empty_params(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'])

        assert (
                check_negative_test_responses(
                    result_response,
                    error_string["empty_params"])
                is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_worker_lookup_jsonrpc_different_version(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_invalid_params"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_worker_lookup_withoutid_params(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_invalid_params"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_worker_lookup_diff_unit_length(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'])

        assert (
                check_worker_lookup_response(
                    result_response, operator.eq, 0)
                is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_worker_lookup_method_field_change(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["missing_invalid_params"])
            is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    def test_workerlookup_params_unknownparameter(self):

        result_response = self.test_obj.run_test(
            env['worker_lookup_input_file'],
            direct_avalon_listener=True)

        assert (
            check_negative_test_responses(
                result_response,
                error_string["unknown_params"])
            is ResultStatus.SUCCESS.value)
