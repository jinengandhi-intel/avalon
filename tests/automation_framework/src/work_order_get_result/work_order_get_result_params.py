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

import json
import logging
import src.utilities.worker_utilities as wconfig
import os
import env

logger = logging.getLogger(__name__)


class WorkOrderGetResult():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderGetResult",
                       "id": 4}
        self.params_obj = {}
        self.tamper = {"params": {}}
        self.config_file = os.path.join(
            env.work_order_input_file, "work_order_get_result.yaml")

    def configure_data(self, input_json, worker_obj, pre_test_response):
        """
        This function should form the json request for WorkOrderGetResult listener request
        :param input_json: input json for WorkOrderGetResult as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: Response received from WorkOrderSubmit request
        :return: Fully formed JSON which can be submitted to listener
        """
        return self.form_workorder_getresult_input(input_json, pre_test_response)

    def configure_data_sdk(self, input_json, worker_obj, pre_test_response):
        """
        This function should form the json request for WorkOrderGetResult SDL request
        :param input_json: input json for WorkOrderGetResult as per EEA spec
        :param worker_obj: worker object
        :param pre_test_response: Response received from WorkOrderSubmit request
        :return: workOrderId present in submit_response
        """
        return self.form_workorder_getresult_input(input_json, pre_test_response)

    def form_workorder_getresult_input(self, input_json, pre_test_response):
        getresult_request = wconfig.workorder_getresult_receipt_input(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            getresult_request = json.loads(wconfig.to_string(self))
        logger.info('*****GetResult Request***** \
                        \n%s\n', getresult_request)
        return getresult_request
