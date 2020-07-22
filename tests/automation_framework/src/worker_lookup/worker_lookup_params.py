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
WORKER_TYPE = "workerType"
ID = "id"


class WorkerLookUp():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerLookUp", "id": 1}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_lookup"

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        if input_json is None:
            wconfig.set_parameter(self.params_obj, WORKER_TYPE, 1)
        else:
            wconfig.add_json_values(self, input_json, pre_test_response)
        final_json = json.loads(wconfig.to_string(self))
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):

        if input_json is None:
            worker_type = 'SGX'
        else:
            try:
                worker_value = input_json["params"]["workerType"]
                if worker_value == 1:
                    worker_type = 'SGX'
                elif worker_value == 2:
                    worker_type = 'MPC'
                elif worker_value == 3:
                    worker_type = 'ZK'
                else:
                    worker_type = worker_value
            except LookupError:
                worker_type = ""

        return worker_type
