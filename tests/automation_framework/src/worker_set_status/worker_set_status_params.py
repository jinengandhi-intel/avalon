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
import avalon_crypto_utils.crypto_utility as crypto_utils
import src.utilities.worker_utilities as wconfig
import env
import os

logger = logging.getLogger(__name__)


class WorkerSetStatus():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerSetStatus", "id": 12}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_set_status"
        self.config_file = os.path.join(env.worker_input_file, "worker_setstatus.yaml")

    def configure_data(
            self, input_json, worker_obj, lookup_response):
        return self.form_set_status_input(input_json, worker_obj, lookup_response)

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_set_status_input(input_json, worker_obj, pre_test_response)

    def form_set_status_input(self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
        set_status_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            final_json = json.loads(wconfig.to_string(self))
        else:
            if "status" in input_json["params"].keys():
                status = input_json["params"]["status"]
            final_json = {"worker_id": set_status_request, "status": status}
        logger.info(" Final json %s \n", final_json)
        return final_json
            
