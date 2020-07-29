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
import os
import env
import avalon_crypto_utils.crypto_utility as crypto_utils
from src.utilities.worker_utilities import tamper_request
import secrets
from avalon_sdk.work_order.work_order_params import WorkOrderParams
import src.utilities.worker_utilities as wconfig
import copy

logger = logging.getLogger(__name__)
NO_OF_BYTES = 16


class WorkOrderSubmit():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderSubmit",
                       "id": 3}
        self.params_obj = {}
        self.session_key = crypto_utils.generate_key()
        self.session_iv = crypto_utils.generate_iv()
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_submit"
        self.final_hash = ""
        self.private_key = ''
        self.worker_obj = ''
        self.encrypted_session_key = ''
        self.config_file = os.path.join(
            env.work_order_input_file, "work_order_submit.yaml")

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        return self.form_workordersubmit_input(input_json, worker_obj, pre_test_response)
        
    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        return self.form_workordersubmit_input(input_json, worker_obj, pre_test_response)
    
    def form_workordersubmit_input(self, input_json, worker_obj, pre_test_response):
        self.private_key = crypto_utils.generate_signing_keys()
        logger.info("JSON object %s \n", input_json)
        if input_json is None:
            input_json = wconfig.read_config(self.config_file, "")
            input_json = json.loads(input_json)
        
        wconfig.add_json_values(self, input_json, pre_test_response)
        if env.test_mode == "listener":
            
            input_work_order = wconfig.compute_signature(self)
            logger.info('Compute Signature complete \n')
            wo_params = json.loads(input_work_order)
        else:

            # Create work order params
            wo_params = WorkOrderParams(
                self.params_obj.get("workOrderId"),
                self.params_obj.get("workerId"),
                self.params_obj.get("workloadId"),
                self.params_obj.get("requesterId"),
                self.session_key,
                self.session_iv,
                self.params_obj.get("requesterNonce"),
                result_uri=" ",
                notify_uri=" ",
                worker_encryption_key=self.params_obj.get("workerEncryptionKey"),
                data_encryption_algorithm=self.params_obj["dataEncryptionAlgorithm"])

            # Add worker input data
            for key in ["inData", "outData"]:
                data = input_json["params"].get(key, [])
                for rows in data:
                    for k, v in rows.items():
                        if k == "data":
                            dataHash = None
                            encryptedDataEncryptionKey = None
                            if "dataHash" in rows.keys():
                                if rows["dataHash"] != "":
                                    dataHash = rows["dataHash"]
                            if "encryptedDataEncryptionKey" in rows.keys():
                                if rows["encryptedDataEncryptionKey"] != "":
                                    encryptedDataEncryptionKey = \
                                        rows["encryptedDataEncryptionKey"]
                    if key == "inData":
                        wo_params.add_in_data(rows["data"], dataHash, encryptedDataEncryptionKey)
                    else:
                        wo_params.add_out_data(rows["data"], dataHash, encryptedDataEncryptionKey)

            # Encrypt work order request hash
            wo_params.add_encrypted_request_hash()
        return wo_params

