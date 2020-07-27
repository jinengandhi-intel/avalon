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
import os
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
        self.config_file = os.path.join(env.worker_input_file, "worker_register.yaml")

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_register_input(input_json, worker_obj, pre_test_response)

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_register_input(input_json, worker_obj, pre_test_response)
    
    def form_worker_register_input(self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
        wconfig.add_json_values(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            final_json = json.loads(wconfig.to_string(self, detail_obj=True))
        else:
            if self.params_obj.get("workerType") == 1:
                self.params_obj["workerType"] = "SGX"
            self.params_obj["details"] = self.details_obj
            final_json = self.params_obj
        logger.info(" Final json %s \n", final_json)
        return final_json
