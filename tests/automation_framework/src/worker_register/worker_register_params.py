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
import env
import src.utilities.worker_utilities as wconfig

logger = logging.getLogger(__name__)


class WorkerRegister():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerRegister", "id": 10}
        self.params_obj = {}
        self.details_obj = {}
        self.worker_type_data_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_register"

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
        wconfig.add_json_values(self, input_json, pre_test_response)
        final_json = json.loads(wconfig.to_string(self, detail_obj=True))
        logger.info(" Final json %s \n", final_json)
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
        wconfig.add_json_values(self, input_json, pre_test_response)
        if self.params_obj.get("workerType") == 1:
            self.params_obj["workerType"] = "SGX"
        register_params = {"worker_id": wconfig.get_parameter(self.params_obj, "workerId"),
                           "workerType": wconfig.get_parameter(self.params_obj, "workerType"),
                           "organization_id": wconfig.get_parameter(self.params_obj, "organizationId"),
                           "application_type_id": wconfig.get_parameter(self.params_obj, "applicationTypeId"),
                           "details": input_json["params"].get("details")}
        return register_params
