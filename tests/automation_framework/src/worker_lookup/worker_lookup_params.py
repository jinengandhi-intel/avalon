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
WORKER_TYPE = "workerType"


class WorkerLookUp():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerLookUp", "id": 1}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_lookup"
        self.config_file = os.path.join(env.worker_input_file, "worker_lookup.yaml")
        self.worker_dict = {1 : "SGX", 2 : "MPC", 3 : "ZK"}

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_lookup_input(input_json, pre_test_response)

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_lookup_input(input_json, pre_test_response)
    
    def form_worker_lookup_input(self, input_json, pre_test_response):
        if input_json is None:
            worker_value = 1
            wconfig.set_parameter(self.params_obj, "workerType", worker_value)
        else:
            worker_value = input_json["params"].get("workerType")
            wconfig.add_json_values(self, input_json, pre_test_response)

        if env.test_mode == "listener":
            lookup_request = json.loads(wconfig.to_string(self))
        else:
            lookup_request = self.worker_dict.get(worker_value, worker_value)
        logger.info("WorkerLookUp Request: %s", lookup_request)
        return lookup_request
