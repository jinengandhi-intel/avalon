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
import avalon_crypto_utils.crypto_utility as crypto_utils
import src.libs.pre_processing_libs as wconfig
from avalon_sdk.work_order.work_order_params import WorkOrderParams
import avalon_crypto_utils.signature as signature
from avalon_sdk.work_order_receipt.work_order_receipt \
    import WorkOrderReceiptRequest
from error_code.error_status import ReceiptCreateStatus


logger = logging.getLogger(__name__)

class AvalonRequest():
    def __init__(self):
        self.params_obj = {}
        self.details_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
           
    def form_workerupdate_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkerUpdate for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerUpdate", "id": 11}
        self.config_file = env.worker_update_input_file
        retrieve_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            update_params = json.loads(
                wconfig.to_string(self, detail_obj=True))
        else:
            details = input_json["params"]["details"]
            update_params = {"worker_id": retrieve_request, "details": details}

        logger.info('*****Worker details Updated with Worker ID***** \
                            \n%s\n', update_params)
        return update_params
            
    def form_workersetstatus_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkerSetStatus for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerSetStatus", "id": 12}
        self.config_file = env.worker_setstatus_input_file
        set_status_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            final_json = json.loads(wconfig.to_string(self))
        else:
            if "status" in input_json["params"].keys():
                status = input_json["params"]["status"]
            final_json = {"worker_id": set_status_request, "status": status}
            logger.info(" Request json %s \n", final_json)
        return final_json
    
    def form_workerretrieve_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkerRetrieve for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerRetrieve", "id": 2}
        self.config_file = env.worker_retrieve_input_file
        retrieve_request = wconfig.worker_retrieve_input(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            retrieve_request = json.loads(wconfig.to_string(self))
        logger.info('*****Worker details Updated with Worker ID***** \
                        \n%s\n', retrieve_request)
        return retrieve_request
    
    def form_workerregister_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkerRegister for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerRegister", "id": 10}
        self.config_file = env.worker_register_input_file
        wconfig.add_json_values(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            final_json = json.loads(wconfig.to_string(self, detail_obj=True))
        else:
            if self.params_obj.get("workerType") == 1:
                self.params_obj["workerType"] = "SGX"
            self.params_obj["details"] = self.details_obj
            final_json = self.params_obj
        logger.info(" Request json %s \n", final_json)
        return final_json
    
    def form_workerlookup_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkerLookup for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerLookUp", "id": 1}
        self.config_file = env.worker_lookup_input_file
        self.worker_dict = {1 : "SGX", 2 : "MPC", 3 : "ZK"}
        if input_json is None:
            worker_value = 1
            wconfig.set_parameter(self.params_obj, "workerType", worker_value)
        else:
            worker_value = input_json["params"].get("workerType")
            wconfig.add_json_values(self, input_json, pre_test_response)

        if env.test_mode == env.listener_string:
            lookup_request = json.loads(wconfig.to_string(self))
        else:
            lookup_request = self.worker_dict.get(worker_value, worker_value)
        logger.info("WorkerLookUp Request: %s", lookup_request)
        return lookup_request
    
    def form_workordersubmit_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkOrderSubmit for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.session_key = crypto_utils.generate_key()
        self.session_iv = crypto_utils.generate_iv()
        self.private_key = crypto_utils.generate_signing_keys()
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderSubmit", "id": 3}
        self.final_hash = ""
        self.encrypted_session_key = ''
        self.config_file = env.work_order_submit_input_file
        logger.info("JSON object %s \n", input_json)
        if input_json is None:
            input_json = wconfig.read_config(self.config_file, "")
            input_json = json.loads(input_json)
        
        wconfig.add_json_values(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            
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
    
    def form_workorderreceiptlookup_request(self, input_json, wo_submit):
        """
        This method forms the request for WorkOrderReceiptLookUp for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderReceiptLookUp", "id": 11}
        self.config_file = env.receipt_lookup_input_file
        receipt_lookup_request = wconfig.workorder_getresult_receipt_input(
            self, input_json, wo_submit)
        if env.test_mode == env.listener_string:
            receipt_lookup_request = json.loads(wconfig.to_string(self))
        logger.info(
            '** Receipt Lookup Request ** \n%s\n',
            receipt_lookup_request)
        return receipt_lookup_request
    
    def form_workorderreceiptcreate_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkOrderReceiptCreate for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderReceiptCreate", "id": 6}
        self.sig_obj = signature.ClientSignature()
        self.SIGNING_ALGORITHM = "SECP256K1"
        self.HASHING_ALGORITHM = "SHA-256"
        self.config_file = env.create_receipt_input_file

        if input_json is None:
            input_json = wconfig.read_config(self.config_file, "")
            input_json = json.loads(input_json)

        logger.info("***Pre test*****\n%s\n", pre_test_response)
        logger.info("***Input json*****\n%s\n", input_json)
        
        self.private_key = crypto_utils.generate_signing_keys()
        
        if env.test_mode == env.listener_string:
            
            wconfig.add_json_values(self, input_json, pre_test_response)
            input_work_order = wconfig.compute_signature(self, True)
            logger.info('''Compute Signature complete \n''')
            wo_create_receipt = json.loads(input_work_order)
        else:

            wo_request = json.loads(pre_test_response.to_jrpc_string(input_json["id"]))
            wo_receipt_request_obj = WorkOrderReceiptRequest()
            wo_create_receipt = wo_receipt_request_obj.create_receipt(
                wo_request,
                ReceiptCreateStatus.PENDING.value,
                self.private_key
            )
        logger.info("Work order create receipt request : {} \n \n ".format(
            json.dumps(wo_create_receipt, indent=4)
        ))
        return wo_create_receipt
    
    def form_workorderreceiptretrieve_request(self, input_json, wo_submit):
        """
        This method forms the request for WorkOrderReceiptRetrieve for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderReceiptRetrieve", "id": 11}
        self.sig_obj = signature.ClientSignature()
        self.SIGNING_ALGORITHM = "SECP256K1"
        self.HASHING_ALGORITHM = "SHA-256"
        self.config_file = env.retrieve_receipt_input_file
        receipt_retrieve_request = wconfig.workorder_getresult_receipt_input(
            self, input_json, wo_submit)
        if env.test_mode == env.listener_string:
            receipt_retrieve_request = json.loads(wconfig.to_string(self))
        logger.info('***** Receipt Retrieve Request ***** \
                        \n%s\n', receipt_retrieve_request)
        return receipt_retrieve_request

    def form_workordergetresult_request(self, input_json, pre_test_response):
        """
        This method forms the request for WorkOrderGetResult for listener and
        sdk as per EEA spec document
        input_json: Input JSON data as per spec
        pre_test_response: response from previous api call
        """
        self.params_obj = {}
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderGetResult", "id": 4}
        self.config_file = env.work_order_getresult_input_file
        getresult_request = wconfig.workorder_getresult_receipt_input(self, input_json, pre_test_response)
        if env.test_mode == env.listener_string:
            getresult_request = json.loads(wconfig.to_string(self))
        logger.info('*****GetResult Request***** \
                        \n%s\n', getresult_request)
        return getresult_request