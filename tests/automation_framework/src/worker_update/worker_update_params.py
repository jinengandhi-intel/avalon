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
import globals
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

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        worker_obj = worker.SGXWorkerDetails()
        if input_json is not None:
            wconfig.add_json_values(self, input_json, pre_test_response)
        wconfig.set_parameter(self.params_obj, "workerId",
            crypto_utils.strip_begin_end_public_key(pre_test_response["result"]["ids"][0]))

        input_worker_retrieve = json.loads(wconfig.to_string(self, detail_obj=True))
        logger.info('*****Worker details Updated with Worker ID***** \
                           \n%s\n', input_worker_retrieve)
        return input_worker_retrieve

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        if globals.proxy_mode and \
            globals.blockchain_type == "ethereum":
            if "result" in pre_test_response and \
                "ids" in pre_test_response["result"].keys():
                if pre_test_response["result"]["totalCount"] != 0:
                    worker_id = pre_test_response["result"]["ids"]
                    # Filter workers by status(active) field
                    # Return first worker whose status is active
                else:
                    logger.error("No workers found")
            else:
                logger.error("Failed to lookup worker")
        elif globals.proxy_mode and \
            globals.blockchain_type == "fabric":
            worker_id = pre_test_response[2][0]
        else:
            if "result" in pre_test_response and \
                "ids" in pre_test_response["result"].keys():
                if pre_test_response["result"]["totalCount"] != 0:
                    worker_id = pre_test_response["result"]["ids"][0]
                else:
                    logger.error("ERROR: No workers found")
                    worker_id = None
            else:
                logger.error("ERROR: Failed to lookup worker")
                worker_id = None
        details = input_json["params"]["details"]

        update_params = {"worker_id": worker_id, "details": details}

        return update_params

