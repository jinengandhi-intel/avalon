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

inputs_params = ["workerId", "organizationId", "applicationTypeId", "requesterGeneratedNonce"]


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
    default_keys = default_params.keys()
    for param in inputs_params:
        if param in default_keys:
            default_params[param] = eval(param)


def read_config(calling_path, response=None, input_data={}):
    config_file = calling_path.replace(".py", ".yaml")
    test_mode = env.test_mode
    file_contents = open(config_file, "r")
    default_params = yaml.load(file_contents)["{}_config".format(test_mode)]
    update_global_params(default_params)
    file_contents.close()

    if response:
        if 'workerId' in response.keys():
            default_params["workerId"] = response['workerId']
        if "details" in input_data.keys():
            details = response.get("result", {}).get("details", {})
            if (env.test_mode == "listener") and input_data:
                input_keys = input_data.keys()
                for key in ['hashingAlgorithm']:
                    if key in input_keys:
                        default_params[key] = details[key]
                for key in ['organizationId', 'applicationTypeId']:
                    if key in input_keys:
                        default_params[key] = response["result"][key]
                if "workerEncryptionKey" in input_keys:
                    default_params[key] = details["workerTypeData"]['encryptionKey']

    return default_params


def add_json_values(caller, input_json_temp, pre_test_response):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    config_path = module.__file__

    input_json  = input_json_temp["params"]
    input_json["id"] = input_json_temp["id"]
    input_param_list = input_json_temp["params"].keys()

    config_yaml = read_config(config_path, pre_test_response, input_json)
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
        else:
            value = input_json[key] if input_json[key] != "" else config_yaml[key]
        set_parameter(caller.params_obj, key, value)
    tamper = caller.tamper
    for key in tamper["params"].keys():
        set_parameter(caller.params_obj, key, tamper["params"][key])


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
