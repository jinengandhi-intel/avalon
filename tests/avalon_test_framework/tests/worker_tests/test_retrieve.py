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
    import check_worker_retrieve_response, \
    check_negative_test_responses
from src.libs.pre_processing_libs \
    import ResultStatus
from src.libs.avalon_test_base import AvalonBase
from src.libs.pre_processing_libs \
    import read_config

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_teardown")
class TestClass():
    test_obj = AvalonBase()
    pytestmark = pytest.mark.setup_teardown_data(
        test_obj, "WorkerRetrieve")

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_retrieve_success(self):

        result_response = self.test_obj.run_test(env.worker_retrieve_input_file)

        assert (check_worker_retrieve_response(result_response)
                is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.proxy
    def test_worker_retrieve_empty_params(self):

        result_response = self.test_obj.run_test(env.worker_retrieve_input_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid data format for Worker id")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.listener
    def test_workerretrieve_params_unknownparameter(self):

        result_response = self.test_obj.run_test(env.worker_retrieve_input_file)

        assert (
            check_negative_test_responses(
                result_response,
                "Invalid parameter unknownEncoding")
            is ResultStatus.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')
