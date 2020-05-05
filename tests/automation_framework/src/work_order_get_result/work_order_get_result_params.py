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
import random

from src.utilities.submit_request_utility import \
    submit_getresult_sdk
logger = logging.getLogger(__name__)


class WorkOrderGetResult():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderGetResult",
                       "id": 4}
        self.params_obj = {}
        self.tamper = {"params": {}}

    def add_json_values(self, input_json_temp, tamper, wo_submit):
        #input_request_wo_submit = json.loads(wo_submit)
        for keys in input_json_temp["params"].keys():
            if "workOrderId" in keys:
                if input_json_temp["params"]["workOrderId"] != "":
                    self.set_work_order_id(input_json_temp["params"]
                                           ["workOrderId"])
                else:
                    self.set_work_order_id(wo_submit["params"]["workOrderId"])

            else:
                param = keys
                value = input_json_temp["params"][keys]
                self.set_unknown_parameter(param, value)

    def set_unknown_parameter(self, param, value):
        self.params_obj[param] = value

    def set_work_order_id(self, work_order_id):
        self.params_obj["workOrderId"] = work_order_id

    def set_request_id(self, request_id):
        self.id_obj["id"] = request_id

    def get_params(self):
        return self.params_obj.copy()

    def to_string(self):
        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()

        return json.dumps(json_rpc_request, indent=4)

    def configure_data(self, input_json, worker_obj, pre_test_response):
        '''
        self.set_work_order_id(work_order_id)
        self.set_request_id(request_id)
        input_get_result = json.loads(self.to_string())
        '''
        if input_json is None:
            self.set_request_id(pre_test_response["id"] + 1)

        else:
            pre_test_response = json.loads(pre_test_response)
            self.set_request_id(pre_test_response["id"] + 1)

        logger.info("listen Pre test*****\n%s\n", pre_test_response)
        self.add_json_values(
            input_json, self.tamper, pre_test_response)
        input_get_result = json.loads(self.to_string())
        return input_get_result

    def configure_data_sdk(self, input_json, worker_obj, pre_test_response):
        jrpc_req_id = input_json["id"]
        if "workOrderId" in input_json["params"].keys():
            if input_json["params"]["workOrderId"] == "":
                workorder_id = pre_test_response.get_work_order_id()
                logger.info("workorder_id %s", workorder_id)
            else:
                workorder_id = input_json["params"]["workOrderId"]
                logger.info("workorder_id else %s", workorder_id)
        else:
            workorder_id = None                
        return workorder_id

