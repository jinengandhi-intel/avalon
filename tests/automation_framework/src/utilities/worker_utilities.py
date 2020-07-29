#!/usr/bin/env python3

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
import yaml
import env
import inspect
import secrets
import random
from enum import IntEnum, unique
from configparser import ConfigParser
import avalon_crypto_utils.crypto_utility as crypto_utils
from ecdsa.util import sigencode_der, sigdecode_der
import copy

"""
status code defined for test case
"""


@unique
class ResultStatus(IntEnum):
    SUCCESS = 0
    FAILURE = 1


@unique
class GetResultWaitTime(IntEnum):
    LOOP_WAIT_TIME = 3


logger = logging.getLogger(__name__)

inputs_params = [
    "workerId",
    "organizationId",
    "applicationTypeId",
    "requesterGeneratedNonce",
    "requesterNonce",
    "requesterId",
    "workOrderId"]


def set_parameter(input_dict, param, value):
    input_dict[param] = value


def get_parameter(input_dict, param):
    if param in input_dict.keys():
        return input_dict[param]


def get_params(class_obj):
    params_copy = class_obj.params_obj.copy()
    if "inData" in params_copy:
        params_copy.pop("inData")
    if "outData" in params_copy:
        params_copy.pop("outData")
    return params_copy


def get_details(class_obj):
    return class_obj.details_obj.copy()


def to_string(class_obj, in_data_check=False, detail_obj=False):
    json_rpc_request = class_obj.id_obj
    json_rpc_request["params"] = get_params(class_obj)
    if in_data_check:
        in_data = get_parameter(class_obj.params_obj, "inData")
        out_data = get_parameter(class_obj.params_obj, "outData")

        if in_data is not None:
            json_rpc_request["params"]["inData"] = in_data

        if out_data is not None:
            json_rpc_request["params"]["outData"] = out_data
    if detail_obj:
        json_rpc_request["params"]["details"] = get_details(class_obj)
    return json.dumps(json_rpc_request, indent=4)


def update_global_params(default_params):
    workerId = secrets.token_hex(32)
    organizationId = secrets.token_hex(32)
    applicationTypeId = secrets.token_hex(32)
    requesterGeneratedNonce = str(random.randint(1, 10 ** 10))
    requesterNonce = secrets.token_hex(16)
    requesterId = secrets.token_hex(32)
    workOrderId = secrets.token_hex(32)
    default_keys = default_params.keys()
    for param in inputs_params:
        if param in default_keys:
            default_params[param] = eval(param)


def read_yaml(caller, response=None, input_data={}):
    config_data = read_config(caller.config_file, "")
    default_params = copy.deepcopy(config_data["params"])
    update_global_params(default_params)

    if response:
        response_key_list = list(response.keys())
        details = response.get("result", {}).get("details", {})
        if input_data != {}:
            input_keys = input_data.keys()
            for key in input_keys:
                if key in ['hashingAlgorithm']:
                    default_params[key] = details[key]
                if key in ['organizationId', 'applicationTypeId']:
                    default_params[key] = response["result"][key]
                if key == "workerEncryptionKey":
                    default_params[key] = \
                            details["workerTypeData"]['encryptionKey']        
                if key == "encryptedSessionKey":
                    if input_data["encryptedSessionKey"] != "":
                        caller.encrypted_session_key = input_data["encryptedSessionKey"]
                    else:
                        caller.encrypted_session_key = \
                            crypto_utils.generate_encrypted_key(
                                caller.session_key,
                                details['workerTypeData']['encryptionKey'])
                if env.test_mode == "listener":
                    if key == "sessionKeyIv":
                        default_params["sessionKeyIv"] = crypto_utils.byte_array_to_hex(
                            caller.session_iv)
                    if key == "workerEncryptionKey":
                        default_params["workerEncryptionKey"] = \
                                crypto_utils.strip_begin_end_public_key(
                                default_params["workerEncryptionKey"])   
        if "workloadId" in input_data.keys():
            default_params["workloadId"] = input_data["workloadId"]
        if hasattr(caller, "encrypted_session_key"):
            if caller.encrypted_session_key and (env.test_mode == "listener"):
                default_params["encryptedSessionKey"] = \
                    crypto_utils.byte_array_to_hex(caller.encrypted_session_key)
    return default_params


def add_json_values(caller, input_json_temp, pre_test_response={}):
    input_json = copy.deepcopy(input_json_temp["params"])
    input_json["id"] = input_json_temp["id"]
    input_param_list = input_json_temp["params"].keys()
    config_yaml = read_yaml(caller, pre_test_response, input_json)

    for key in input_param_list:
        if key == "details":
            details_input_list = input_json["details"].keys()
            details_json = input_json["details"]
            for d_key in details_input_list:
                if d_key == "hashingAlgorithm" and details_json[d_key] == '':
                    value = config_yaml[d_key]
                else:
                    value = details_json[d_key]
                set_parameter(caller.details_obj, d_key, value)
        elif key == "workerServiceId":
            set_parameter(caller.params_obj, "workerServiceId", pre_test_response["params"]["workerId"])
        elif key == "workOrderId":
            if input_json_temp["method"] != "WorkOrderSubmit":
                value = input_json[key] if input_json[key] != "" else pre_test_response["params"]["workOrderId"]
            else:
               value = input_json[key] if input_json[key] != "" else config_yaml[key]
            set_parameter(caller.params_obj, "workOrderId", value)
        elif key == "requesterId":
            if input_json_temp["method"] != "WorkOrderSubmit":
                value = input_json[key] if input_json[key] != "" else pre_test_response["params"]["requesterId"]
            else:
               value = input_json[key] if input_json[key] != "" else config_yaml[key]
            set_parameter(caller.params_obj, "requesterId", value)
        elif (key == "workerId") and (input_json_temp["method"] != "WorkerRegister"):
            if input_json_temp["method"] != "WorkOrderSubmit" and (pre_test_response.get("params") != None):
                value = input_json[key] if input_json[key] != "" else pre_test_response["params"]["workerId"]
            else:
               value = input_json[key] if input_json[key] != "" else pre_test_response[key]
            set_parameter(caller.params_obj, "workerId", value)
        else:
            value = input_json[key] \
                if input_json[key] != "" else config_yaml[key]
            if (key == "workloadId") and (input_json[key] != ""):
                    value = value.encode("UTF-8").hex()
            set_parameter(caller.params_obj, key, value)

        tamper = caller.tamper
        for key in tamper["params"].keys():
            set_parameter(caller.params_obj, key, tamper["params"][key])
    if caller.params_obj.get("workerEncryptionKey") is not None:
        if env.test_mode == "listener":
            caller.params_obj["workerEncryptionKey"] = caller.params_obj["workerEncryptionKey"].encode("UTF-8").hex()
        value = input_json["workerEncryptionKey"] if \
            input_json["workerEncryptionKey"] != "" else \
            caller.params_obj.get("workerEncryptionKey", '')
        caller.params_obj["workerEncryptionKey"] = value
    
    for key in ["inData", "outData"]:
        if key in input_param_list:
            if input_json[key] != "":
                input_json_data = input_json[key]
                add_in_out_data(caller, input_json_data, key)
            else:
                caller.params_obj[key] = ""

    if "encryptedRequestHash" in input_param_list:
        if input_json["encryptedRequestHash"] != "":
            caller.params_obj["encryptedRequestHash"] = \
                input_json["encryptedRequestHash"]
        else:
            caller.params_obj["encryptedRequestHash"] = \
                compute_encrypted_request_hash(caller)
    
    if "workOrderRequestHash" in input_param_list:
        wo_request_hash = caller.sig_obj.calculate_request_hash(pre_test_response["params"])
        final_hash_str = crypto_utils.byte_array_to_base64(wo_request_hash)
        set_parameter(caller.params_obj, "workOrderRequestHash", final_hash_str)
    
    if "requesterSignature" in input_param_list and (input_json_temp["method"] == "WorkOrderReceiptCreate"):
        receipt_requester_signature(caller)

def tamper_request(input_json, tamper_instance, tamper):
    '''Function to tamper the input request at required instances.
       Valid instances used in test framework are :
       force, add, remove.
       force : used by API class definitions primarily to force null values to
               parameter values to replace default values and to add
               unknown parameter key, value pair to request parameters for the
               purpose of testing. code for the same coded in respective api
               classes
       add : can be used to add a parameter and value not in input json,
             also can be used to replace a value for parameter in input json
       remove : deletes the parameter from input json

       The function can be used for other instances also provided the instances
       are used in test framework and also value of tamper defined in test case

       A blank tamper dictionary is required for all test cases, in cases where
       tamper functionality is not required. Example : tamper{"params":{}}'''
    before_sign_keys = []
    after_sign_keys = []
    input_json_temp = json.loads(input_json)

    if tamper_instance in tamper["params"].keys():
        tamper_instance_keys = tamper["params"][tamper_instance].keys()

        for tamper_key in tamper_instance_keys:
            for action_key in (
                    tamper["params"][tamper_instance][tamper_key].keys()):
                if action_key == "add":
                    input_json_temp["params"][tamper_key] = (
                        tamper["params"][tamper_instance][tamper_key]["add"])
                elif action_key == "remove":
                    del input_json_temp["params"][tamper_key]

    tampered_json = json.dumps(input_json_temp)
    return tampered_json


def configure_data(action_obj, input_json, worker_obj, pre_test_response):
    if env.test_mode == "listener":
        configure_data_output = action_obj.configure_data(
            input_json, worker_obj, pre_test_response)
    else:
        configure_data_output = action_obj.configure_data_sdk(
            input_json, worker_obj, pre_test_response)
    return configure_data_output

def config_data_update(input, key, value):
    if key in input.keys():
        if value == "remove":
            del input[key]
        elif isinstance(value, dict):
            for n_k, n_v in value.items():
                if isinstance(n_v, dict):
                    config_data_update(input[key], n_k, n_v)
                else:
                    input[key][n_k] = n_v
        else:
            input[key] = value
        return
    for k, v in input.items():
        if k in ["inData", "outData"]:
            for data_val in v:
                config_data_update(data_val, key, value)
        elif isinstance(v, dict):
            config_data_update(v, key, value)

def read_config(config_file, test_name):
    yaml_file = open(config_file, "r")
    parsed_yaml_file = yaml.load(yaml_file)
    test_config = parsed_yaml_file["Default"]

    if parsed_yaml_file.get(test_name):
        test_items = parsed_yaml_file[test_name]
        for key, value in test_items.items():
            config_data_update(test_config, key, value)

    return test_config

def retrieve_worker_id(pre_test_response):
    worker_id = None
    if env.proxy_mode:
        worker_id = random.choice(pre_test_response[2])
    else:
        if "result" in pre_test_response and \
                "ids" in pre_test_response["result"].keys():
            if pre_test_response["result"]["totalCount"] != 0:
                worker_id = random.choice(
                    pre_test_response["result"]["ids"])
            else:
                logger.error("ERROR: No workers found")
        else:
            logger.error("ERROR: Failed to lookup worker")
    return worker_id

def worker_retrieve_input(caller, input_json, pre_test_response):
    if env.test_mode == "listener":
        pre_test_response["workerId"] = retrieve_worker_id(
        pre_test_response)
        if input_json is not None:
            add_json_values(caller, input_json, pre_test_response)
        else:
            # set_parameter(caller.params_obj, "workerId",
            #                     crypto_utils.strip_begin_end_public_key
            #                     (pre_test_response["workerId"]))
            set_parameter(caller.params_obj, "workerId", pre_test_response["workerId"])
    else:
        worker_id = None
        if input_json is not None:
            if "workerId" in input_json["params"].keys():
                if input_json["params"]["workerId"] != "":
                    worker_id = input_json["params"]["workerId"]
                else:
                    worker_id = retrieve_worker_id(pre_test_response)
        else:
            worker_id = retrieve_worker_id(pre_test_response)
        return worker_id

def workorder_getresult_receipt_input(caller, input_json, pre_test_response):
    if env.test_mode == "listener":
        add_json_values(caller, input_json, pre_test_response)
    else:
        workorder_id = None
        requester_id = None
        if input_json["method"] == "WorkOrderReceiptLookUp":
            if "requesterId" in input_json["params"].keys():
                if input_json["params"]["requesterId"] == "":
                    requester_id = pre_test_response.get_requester_id()
                else:
                    requester_id = input_json["params"]["requesterId"]
            return requester_id
        else:
            if "workOrderId" in input_json["params"].keys():
                if input_json["params"]["workOrderId"] == "":
                    workorder_id = pre_test_response.get_work_order_id()
                else:
                    workorder_id = input_json["params"]["workOrderId"]
            return workorder_id

def compute_signature(caller, rVerKey=False):
    tamper = caller.tamper
    compute_requester_signature(caller, rVerKey)

    input_after_sign = to_string(caller, True)
    tamper_instance = 'after_sign'
    tampered_request = tamper_request(input_after_sign, tamper_instance,
                                        tamper)
    return tampered_request

def compute_requester_signature(caller, rVerKey=False):
    """
    This function will compute requester signature and update the verifying key
    """
    caller.public_key = crypto_utils.get_verifying_key(caller.private_key)
    if rVerKey:
        caller.params_obj["receiptVerificationKey"] = caller.public_key
    else:
        if get_parameter(caller.params_obj, "requesterSignature") is not None:
            signature_result = \
                caller.private_key.sign_digest_deterministic(
                    bytes(caller.final_hash),
                    sigencode=sigencode_der)
            caller.requester_signature = crypto_utils.byte_array_to_base64(
                signature_result)
            if caller.params_obj["requesterSignature"] == "":
                caller.params_obj["requesterSignature"] = \
                    caller.requester_signature
            caller.params_obj["verifyingKey"] = caller.public_key

def compute_encrypted_request_hash(caller):
    """
    This function will compute encrypted request Hash
    :return: encrypted request hash
    """
    first_string = get_parameter(caller.params_obj, "requesterNonce") or ""
    worker_order_id = get_parameter(caller.params_obj, "workOrderId") or ""
    worker_id = get_parameter(caller.params_obj, "workerId") or ""
    workload_id = get_parameter(caller.params_obj, "workloadId") or ""
    requester_id = get_parameter(caller.params_obj, "requesterId") or ""

    first_string += \
        worker_order_id + worker_id + workload_id + requester_id

    concat_hash = first_string.encode("UTF-8")
    hash_1 = crypto_utils.compute_message_hash(concat_hash)

    in_data = get_parameter(caller.params_obj, "inData")
    out_data = get_parameter(caller.params_obj, "outData")

    hash_2 = bytearray()
    if in_data is not None:
        hash_2 = compute_hash_string(in_data)

    hash_3 = bytearray()
    if out_data is not None:
        hash_3 = compute_hash_string(out_data)

    final_string = hash_1 + hash_2 + hash_3
    caller.final_hash = crypto_utils.compute_message_hash(final_string)

    encrypted_request_hash = crypto_utils.byte_array_to_hex(
        crypto_utils.encrypt_data(
            caller.final_hash, caller.session_key,
            caller.session_iv))

    return encrypted_request_hash

def receipt_requester_signature(caller):
    wo_receipt_str = (caller.params_obj["workOrderId"] +
                      caller.params_obj["workerServiceId"] +
                      caller.params_obj["workerId"] +
                      caller.params_obj["requesterId"] +
                      str(caller.params_obj["receiptCreateStatus"]) +
                      caller.params_obj["workOrderRequestHash"] +
                      caller.params_obj["requesterGeneratedNonce"])

    wo_receipt_bytes = bytes(wo_receipt_str, "UTF-8")
    wo_receipt_hash = crypto_utils.compute_message_hash(wo_receipt_bytes)
    status, wo_receipt_sign = caller.sig_obj.generate_signature(
        wo_receipt_hash,
        caller.private_key
    )
    set_parameter(caller.params_obj, "requesterSignature", wo_receipt_sign)

def compute_hash_string(data):
    """
    This function will compute the message hash and encode it in UTF-8
    :param data: Data, as specified by workload
    :return: computed and encoded string
    """
    final_hash_str = ""
    hash_string = ""
    for data_item in data:
        data = ""
        datahash = ""
        e_key = ""
        iv = ""
        if 'dataHash' in data_item:
            datahash = data_item['dataHash']
        if 'data' in data_item:
            data = data_item['data']
        if 'encryptedDataEncryptionKey' in data_item:
            e_key = \
                data_item['encryptedDataEncryptionKey']
        if 'iv' in data_item:
            iv = data_item['iv']
        concat_string = datahash + data + e_key + iv
        hash_string += concat_string

    final_hash_str = crypto_utils.compute_message_hash(
        hash_string.encode("UTF-8"))
    return final_hash_str

def add_in_out_data(caller, input_json_data, key="inData"):
    """
    This function will add inData/outData params to the params_obj
    :param input_json_data: inData/outData for WorkOrderSubmit as per EEA spec
    """
    data = copy.deepcopy(input_json_data)
    caller.params_obj[key] = []

    if key == "inData":
        try:
            data.sort(key=lambda x: x['index'])
        except Exception:
            logger.debug("Sorting Indata based on Index failed \n")

    for item in data:
        data_copy = caller.params_obj[key]
        mod_data_copy = _add_data_item(caller, data_copy, item)
        if mod_data_copy is not None:
            caller.params_obj[key] = mod_data_copy
        else:
            data_copy = caller.params_obj[key]
            data_copy.append(item)
            caller.params_obj[key] = data_copy

def _add_data_item(caller, data_copy, data_item):
    try:
        index = data_item['index']
        data = data_item['data'].encode('UTF-8')
        if 'encryptedDataEncryptionKey' in data_item:
            e_key = \
                data_item['encryptedDataEncryptionKey'].encode('UTF-8')
        else:
            e_key = "null".encode('UTF-8')
        if (not e_key) or (e_key == "null".encode('UTF-8')):
            enc_data = crypto_utils.encrypt_data(
                data, caller.session_key, caller.session_iv)
            base64_enc_data = \
                (crypto_utils.byte_array_to_base64(enc_data))
            if 'dataHash' in data_item:
                if not data_item['dataHash']:
                    dataHash_enc_data = (crypto_utils.byte_array_to_hex(
                        crypto_utils.compute_message_hash(data)))
                else:
                    dataHash_enc_data = (
                        crypto_utils.byte_array_to_hex(
                            crypto_utils.compute_message_hash(
                                data_item['dataHash'])))
            logger.debug("encrypted indata - %s",
                            crypto_utils.byte_array_to_base64(enc_data))
        elif e_key == "-".encode('UTF-8'):
            # Skip encryption and just encode workorder data
            # to base64 format
            base64_enc_data = (crypto_utils.byte_array_to_base64(data))
            if 'dataHash' in data_item:
                if not data_item['dataHash']:
                    dataHash_enc_data = (crypto_utils.byte_array_to_hex(
                        crypto_utils.compute_message_hash(data)))
                else:
                    dataHash_enc_data = (
                        crypto_utils.byte_array_to_hex(
                            crypto_utils.compute_message_hash(
                                data_item['dataHash'])))
        else:
            data_key = None
            data_iv = None
            enc_data = crypto_utils.encrypt_data(data, data_key, data_iv)
            base64_enc_data = \
                (crypto_utils.byte_array_to_base64(enc_data))
            if 'dataHash' in data_item:
                if not data_item['dataHash']:
                    dataHash_enc_data = (crypto_utils.byte_array_to_hex(
                        crypto_utils.compute_message_hash(data)))
                else:
                    dataHash_enc_data = (
                        crypto_utils.byte_array_to_hex(
                            crypto_utils.compute_message_hash(
                                data_item['dataHash'])))
            logger.debug("encrypted indata - %s",
                            crypto_utils.byte_array_to_base64(enc_data))

        enc_indata_item = {'index': index,
                            'dataHash': dataHash_enc_data,
                            'data': base64_enc_data}

        for key in ["encryptedDataEncryptionKey", "iv"]:
            if data_item.get(key) is not None:
                enc_indata_item[key] = data_item[key]
        data_copy.append(enc_indata_item)

        return data_copy
    except Exception as e:
        logger.exception("Exception occured %s, in add_data_item", e)
        return None
