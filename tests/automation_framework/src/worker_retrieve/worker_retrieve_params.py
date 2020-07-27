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
import random
import os
import avalon_crypto_utils.crypto_utility as crypto_utils
import src.utilities.worker_utilities as wconfig

logger = logging.getLogger(__name__)


class WorkerRetrieve():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerRetrieve", "id": 2}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_retrieve"
        self.config_file = os.path.join(env.worker_input_file, "worker_retrieve.yaml")

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_retrieve_input(input_json, pre_test_response)


    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_worker_retrieve_input(input_json, pre_test_response)
    

    def form_worker_retrieve_input(self, input_json, pre_test_response):
        retrieve_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            retrieve_request = json.loads(wconfig.to_string(self))
        logger.info('*****Worker details Updated with Worker ID***** \
                        \n%s\n', retrieve_request)
        return retrieve_request
