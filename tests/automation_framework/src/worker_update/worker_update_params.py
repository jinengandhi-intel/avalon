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
import avalon_sdk.worker.worker_details as worker
import avalon_crypto_utils.crypto_utility as crypto_utils
import src.utilities.worker_utilities as wconfig

logger = logging.getLogger(__name__)


class WorkerUpdate():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerUpdate", "id": 11}
        self.params_obj = {}
        self.details_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_update"
        self.config_file = os.path.join(env.worker_input_file, "worker_update.ini")

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_lookup_input(input_json, pre_test_response)

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_lookup_input(input_json, pre_test_response)
    
    def form_worker_lookup_input(self, input_json, pre_test_response):
        retrieve_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            update_params = json.loads(
                wconfig.to_string(self, detail_obj=True))
        else:
            details = input_json["params"]["details"]
            update_params = {"worker_id": retrieve_request, "details": details}

        logger.info('*****Worker details Updated with Worker ID***** \
                            \n%s\n', update_params)
        return update_params
