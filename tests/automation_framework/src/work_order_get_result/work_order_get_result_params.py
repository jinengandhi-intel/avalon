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

logger = logging.getLogger(__name__)


class WorkOrderGetResult():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderGetResult",
                       "id": 4}
        self.params_obj = {}
        self.tamper = {"params": {}}

    def add_json_values(self, input_json_temp, tamper, wo_submit):
        params = input_json_temp["params"]
        for keys in params.keys():
            if "workOrderId" in keys:
                value = params["workOrderId"] \
                    if params["workOrderId"] != '' \
                    else wo_submit["params"]["workOrderId"]
                wconfig.set_parameter(self.params_obj, "workOrderId", value)
            else:
                wconfig.set_parameter(
                    self.params_obj, keys, input_json_temp["params"][keys])

    def configure_data(self, input_json, worker_obj, pre_test_response):
        wconfig.set_parameter(self.id_obj, "id", (pre_test_response["id"] + 1))

        logger.info("listen Pre test*****\n%s\n", pre_test_response)
        self.add_json_values(
            input_json, self.tamper, pre_test_response)
        input_get_result = json.loads(wconfig.to_string(self))
        return input_get_result

    def configure_data_sdk(self, input_json, worker_obj, pre_test_response):
        jrpc_req_id = input_json["id"]
        workorder_id = None
        if "workOrderId" in input_json["params"].keys():
            if input_json["params"]["workOrderId"] == "":
                workorder_id = pre_test_response.get_work_order_id()
            else:
                workorder_id = input_json["params"]["workOrderId"]
            logger.info("workorder_id %s", workorder_id)
        return workorder_id
