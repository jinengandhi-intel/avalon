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
import globals

logger = logging.getLogger(__name__)


class WorkerSetStatus():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerSetStatus", "id": 12}
        self.params_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_set_status"

    def configure_data(
            self, input_json, worker_obj, lookup_response):
        logger.info(" Request json %s \n", input_json)
        lookup_response["workerId"] = lookup_response["result"]["ids"][0]
        wconfig.add_json_values(self, input_json, lookup_response)
        final_json = json.loads(wconfig.to_string(self))
        logger.info(" Final json %s \n", final_json)
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
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
        if "status" in input_json["params"].keys():
            status = input_json["params"]["status"]
        set_status_params = {"worker_id": worker_id, "status": status}
        return set_status_params

