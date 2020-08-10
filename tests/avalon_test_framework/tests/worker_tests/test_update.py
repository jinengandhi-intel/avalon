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
import env
from src.libs.verification_libs \
    import validate_response_code
from src.libs.pre_processing_libs \
    import ResultStatus
from src.libs.avalon_test_base import AvalonBase

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_teardown")
class TestClass():
    test_obj = AvalonBase()
    pytestmark = pytest.mark.setup_teardown_data(
        test_obj, "WorkerUpdate")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_update_success(self):

        result_response = self.test_obj.run_test(env.worker_update_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_update_unknown_parameter(self):

        result_response = self.test_obj.run_test(env.worker_update_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_update_invalid_parameter(self):

        result_response = self.test_obj.run_test(env.worker_update_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_update_empty_details(self):

        result_response = self.test_obj.run_test(env.worker_update_input_file)

        assert (
            validate_response_code(
                result_response,
                env.expected_error_code) is ResultStatus.SUCCESS.value)
