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
from src.libs.pre_processing_libs \
    import ResultStatus
from src.libs.verification_libs \
    import check_worker_create_receipt_response, \
    check_worker_retrieve_receipt_response, \
    check_workorder_receipt_lookup_response
import operator
from src.libs.avalon_test_base import AvalonBase
from conftest import env

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_teardown")
class TestClass():
    test_obj = AvalonBase()
    pytestmark = pytest.mark.setup_teardown_data(
        test_obj, "WorkOrderReceiptCreate")

    @pytest.mark.sdk
    @pytest.mark.listener
    def test_work_order_create_receipt_success(self):

        result_response = self.test_obj.run_test(
            env['create_receipt_input_file'])

        assert (check_worker_create_receipt_response(result_response)
                is ResultStatus.SUCCESS.value)


    @pytest.mark.sdk
    @pytest.mark.listener
    @pytest.mark.setup_teardown_data(
        test_obj, "WorkOrderReceiptRetrieve")
    def test_work_order_retrieve_receipt_success(self):

        result_response = self.test_obj.run_test(
            env['retrieve_receipt_input_file'])

        assert (check_worker_retrieve_receipt_response(result_response)
                is ResultStatus.SUCCESS.value)


    @pytest.mark.sdk
    @pytest.mark.listener
    def test_create_work_order_receipt_invalid_requester_id(self):

        result_response = self.test_obj.run_test(
            env['create_receipt_input_file'])

        assert (check_worker_create_receipt_response(result_response)
                is ResultStatus.SUCCESS.value)


    @pytest.mark.sdk
    @pytest.mark.listener
    def test_create_work_order_receipt_hexstr_workorderRequesthash(
            self):

        result_response = self.test_obj.run_test(
            env['create_receipt_input_file'])

        assert (check_worker_create_receipt_response(result_response)
                is ResultStatus.SUCCESS.value)


    @pytest.mark.sdk
    @pytest.mark.listener
    def test_create_work_order_receipt_wrong_rverificationkey(self):

        result_response = self.test_obj.run_test(
            env['create_receipt_input_file'])

        assert (check_worker_create_receipt_response(result_response)
                is ResultStatus.SUCCESS.value)


    @pytest.mark.sdk
    @pytest.mark.listener
    def test_work_order_receipt_lookup_success(self):

        result_response = self.test_obj.run_test(
            env['receipt_lookup_input_file'])

        assert (
            check_workorder_receipt_lookup_response(
                result_response,
                operator.gt,
                0) is ResultStatus.SUCCESS.value)

