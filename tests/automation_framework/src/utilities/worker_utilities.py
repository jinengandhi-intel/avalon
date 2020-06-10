import json
import logging
import yaml
import globals
import inspect
import secrets
import random
logger = logging.getLogger(__name__)

globals_params = ["workerId", "organizationId", "applicationTypeId", "requesterGeneratedNonce"]


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
    for param in globals_params:
        if param in default_keys:
            default_params[param] = eval(param)


def read_config(calling_path, response=None, input_data={}):
    config_file = calling_path.replace(".py", ".yaml")
    test_mode = globals.direct_test_mode
    file_contents = open(config_file, "r")
    default_params = yaml.load(file_contents)["{}_config".format(test_mode)]
    update_global_params(default_params)
    file_contents.close()

    if response:
        if 'workerId' in response.keys():
            default_params["workerId"] = response['workerId']
        if "details" in input_data.keys():
            details = response.get("result", {}).get("details", {})
            if (globals.direct_test_mode == "listener") and input_data:
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
