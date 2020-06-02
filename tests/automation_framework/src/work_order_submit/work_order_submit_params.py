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
import globals
import avalon_crypto_utils.crypto.crypto as crypto
import avalon_crypto_utils.crypto_utility as crypto_utils
from src.utilities.tamper_utility import tamper_request
import avalon_crypto_utils.crypto_utility as enclave_helper
import secrets
from avalon_sdk.work_order.work_order_params import WorkOrderParams
import src.utilities.worker_utilities as wconfig

logger = logging.getLogger(__name__)
NO_OF_BYTES = 16


class WorkOrderSubmit():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkOrderSubmit",
                       "id": 3}
        self.params_obj = {}
        self.session_key = self.generate_key()
        self.session_iv = self.generate_iv()
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_submit"
        self.final_hash = ""
        self.private_key = ''
        self.worker_obj = ''
        self.encrypted_session_key = ''

    def add_json_values(self, input_json_temp, pre_test_response,
                        private_key, tamper):

        self.private_key = private_key
        input_params_list = input_json_temp["params"].keys()
        input_json = input_json_temp["params"]

        if "encryptedSessionKey" in input_params_list:
            if input_json["encryptedSessionKey"] != "":
                self.encrypted_session_key = input_json["encryptedSessionKey"]
            else:
                self.encrypted_session_key = (
                    self.generate_encrypted_key(self.session_key,
                        pre_test_response['result']['details']['workerTypeData']['encryptionKey']))

        config_yaml = self.get_default_params(pre_test_response, input_json)
        for c_key, c_value in config_yaml.items():
            if c_key in input_params_list:
                value = input_json[c_key] if input_json[c_key] != "" else c_value
                if (c_key == "workloadId") and (input_json[c_key] != "") :
                    value = value.encode("UTF-8").hex()
                wconfig.set_parameter(self.params_obj, c_key, value)

        if self.params_obj.get("workerEncryptionKey") is not None:
            self.params_obj["workerEncryptionKey"] = self.params_obj.get("workerEncryptionKey", '').encode("UTF-8").hex()

        if "inData" in input_params_list:
            if input_json["inData"] != "":
                input_json_inData = input_json["inData"]
                self.add_in_data(input_json_inData)
            else:
                self.params_obj["inData"] = ""

        if "outData" in input_params_list:
            if input_json["outData"] != "":
                input_json_outData = input_json["outData"]
                self.add_out_data(input_json_outData)
            else:
                self.params_obj["outData"] = ""

        if "encryptedRequestHash" in input_params_list:
            if input_json["encryptedRequestHash"] != "":
                self.params_obj["encryptedRequestHash"] = input_json["encryptedRequestHash"]
            else:
                self.params_obj["encryptedRequestHash"] = self._compute_encrypted_request_hash()

        if "default" in tamper.keys():
            if "params" in tamper["default"].keys():
                for key, value in tamper["default"]["params"]:
                    wconfig.set_parameter(self.params_obj, key, value)

    def _compute_encrypted_request_hash(self):
        first_string = wconfig.get_parameter(self.params_obj, "requesterNonce") or ""
        worker_order_id = wconfig.get_parameter(self.params_obj, "workOrderId") or ""
        worker_id = wconfig.get_parameter(self.params_obj, "workerId") or ""
        workload_id = wconfig.get_parameter(self.params_obj, "workloadId") or ""
        requester_id = wconfig.get_parameter(self.params_obj, "requesterId") or ""

        first_string = first_string + worker_order_id
        first_string = first_string + worker_id
        first_string = first_string + workload_id
        first_string = first_string + requester_id

        concat_hash = bytes(first_string, "UTF-8")
        self.hash_1 = crypto.byte_array_to_base64(
            crypto.compute_message_hash(concat_hash))

        in_data = wconfig.get_parameter(self.params_obj, "inData")
        out_data = wconfig.get_parameter(self.params_obj, "outData")

        self.hash_2 = ""
        if in_data is not None:
            self.hash_2 = self._compute_hash_string(in_data)

        self.hash_3 = ""
        if out_data is not None:
            self.hash_3 = self._compute_hash_string(out_data)

        final_string = self.hash_1 + self.hash_2 + self.hash_3
        self.final_hash = crypto.compute_message_hash(
            bytes(final_string, 'UTF-8'))

        self.encrypted_request_hash = self.byte_array_to_hex_str(
            self.encrypt_data(
                self.final_hash, self.session_key,
                self.session_iv))

        return self.encrypted_request_hash

    def _compute_hash_string(self, data):
        final_hash_str = ""
        hash_string = ""
        for data_item in data:
            data = "".encode('UTF-8')
            datahash = "".encode('UTF-8')
            e_key = "".encode('UTF-8')
            iv = "".encode('UTF-8')
            if 'dataHash' in data_item:
                datahash = data_item['dataHash'].encode('UTF-8')
            if 'data' in data_item:
                data = data_item['data'].encode('UTF-8')
            if 'encryptedDataEncryptionKey' in data_item:
                e_key = \
                    data_item['encryptedDataEncryptionKey'].encode('UTF-8')
            if 'iv' in data_item:
                iv = data_item['iv'].encode('UTF-8')
            hash_string = datahash + data + e_key + iv
            complete_bytes = bytes(hash_string)
            hash = crypto.compute_message_hash(complete_bytes)
            final_hash_str = final_hash_str + crypto.byte_array_to_base64(hash)
        return final_hash_str

    def _compute_requester_signature(self):
        if wconfig.get_parameter(self.params_obj, "requesterSignature") is not None:
            self.public_key = self.private_key.GetPublicKey().Serialize()
            signature_result = self.private_key.SignMessage(self.final_hash)
            self.requester_signature = crypto.byte_array_to_base64(
                signature_result)
            if self.params_obj["requesterSignature"] == "":
                self.params_obj["requesterSignature"] = self.requester_signature
            self.params_obj["verifyingKey"] = self.public_key

    def byte_array_to_hex_str(self, in_byte_array):
        '''
        Converts tuple of bytes to hex string
        '''
        logger.debug("Input Byte Array: %s", in_byte_array)
        hex_str = ''.join(format(i, '02x') for i in in_byte_array)
        logger.debug("Output Byte Array to str: %s", hex_str)
        return hex_str

    def generate_key(self):
        """
        Function to generate symmetric key
        """
        return crypto.SKENC_GenerateKey()

    def generate_iv(self):
        """
        Function to generate random initialization vector
        """
        return crypto.SKENC_GenerateIV()

    def generate_encrypted_key(self, key, encryption_key):
        """
        Function to generate session key for the client
        Parameters:
        - encryption_key is a one-time encryption
          used to encrypt the passed key
        - key that needs to be encrypted
        """
        pub_enc_key = crypto.PKENC_PublicKey(encryption_key)
        return pub_enc_key.EncryptMessage(key)

    def add_in_data(self, input_json_inData):
        if "inData" not in self.params_obj:
            self.params_obj["inData"] = []

        try:
            input_json_inData.sort(key=lambda x: x['index'])
        except Exception:
            logger.debug("Sorting Indata based on Index failed \n")

        for inData_item in input_json_inData:
            in_data_copy = self.params_obj["inData"]
            mod_data_copy = self._add_data_item(in_data_copy, inData_item)
            if mod_data_copy is not None:
                self.params_obj["inData"] = mod_data_copy
            else:
                in_data_copy = self.params_obj["inData"]
                in_data_copy.append(inData_item)
                self.params_obj["inData"] = in_data_copy

    def add_out_data(self, input_json_outData):
        if "outData" not in self.params_obj:
            self.params_obj["outData"] = []

        for outData_item in input_json_outData:
            out_data_copy = self.params_obj["outData"]
            mod_data_copy = self._add_data_item(out_data_copy, outData_item)
            if mod_data_copy is not None:
                self.params_obj["outData"] = mod_data_copy
            else:
                out_data_copy = self.params_obj["outData"]
                out_data_copy.append(outData_item)
                self.params_obj["outData"] = out_data_copy

    def _add_data_item(self, data_copy, data_item):

        try:
            index = data_item['index']
            data = data_item['data'].encode('UTF-8')
            if 'encryptedDataEncryptionKey' in data_item:
                e_key = data_item['encryptedDataEncryptionKey'].encode(
                    'UTF-8')
            else:
                e_key = "null".encode('UTF-8')
            if (not e_key) or (e_key == "null".encode('UTF-8')):
                enc_data = self.encrypt_data(data, self.session_key,
                                             self.session_iv)
                base64_enc_data = (crypto.byte_array_to_base64(enc_data))
                if 'dataHash' in data_item:
                    if not data_item['dataHash']:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data)))
                    else:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data_item['dataHash'])))
                logger.debug("encrypted indata - %s",
                             crypto.byte_array_to_base64(enc_data))
            elif e_key == "-".encode('UTF-8'):
                # Skip encryption and just encode workorder data
                # to base64 format
                base64_enc_data = (crypto.byte_array_to_base64(data))
                if 'dataHash' in data_item:
                    if not data_item['dataHash']:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data)))
                    else:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data_item['dataHash'])))
            else:
                data_key = None
                data_iv = None
                enc_data = self.encrypt_data(data, data_key, data_iv)
                base64_enc_data = (crypto.byte_array_to_base64(enc_data))
                if 'dataHash' in data_item:
                    if not data_item['dataHash']:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data)))
                    else:
                        dataHash_enc_data = (self.byte_array_to_hex_str(
                            crypto.compute_message_hash(data_item['dataHash'])))
                logger.debug("encrypted indata - %s",
                             crypto.byte_array_to_base64(enc_data))

            enc_indata_item = {'index': index,
                               'dataHash': dataHash_enc_data,
                               'data': base64_enc_data,
                               'encryptedDataEncryptionKey':
                                   data_item['encryptedDataEncryptionKey'],
                               'iv': data_item['iv']}
            data_copy.append(enc_indata_item)

            return data_copy
        except Exception:
            return None

    def encrypt_data(self, data, encryption_key, iv):
        """
        Function to encrypt data based on encryption key and iv
        Parameters:
            - data is each item in inData or outData part of workorder request
              as per TCF API 6.1.7 Work Order Data Formats
            - encryption_key is the key
              used to encrypt the data
            - iv is an initialization vector if
              required by the data encryption algorithm.
              The default is all zeros.iv must be a unique
              random number for every
              encryption operation.
        """
        logger.debug("encrypted_session_key: %s", encryption_key)
        val = iv if iv else 0
        encrypted_data = crypto.SKENC_EncryptMessage(encryption_key, val, data)

        return encrypted_data

    def compute_signature(self, tamper):

        self._compute_requester_signature()

        json_rpc_request = self.id_obj
        json_rpc_request["params"] = wconfig.get_params(self)

        input_after_sign = wconfig.to_string(self, True)
        tamper_instance = 'after_sign'
        tampered_request = tamper_request(input_after_sign, tamper_instance,
                                          tamper)
        return tampered_request

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        # private_key of client
        private_key = enclave_helper.generate_signing_keys()
        if input_json is None:
            with open(os.path.join(
                    globals.work_order_input_file,
                    "work_order_success.json"), "r") as file:
                input_json = file.read().rstrip('\n')

            input_json = json.loads(input_json)

        self.add_json_values(input_json, pre_test_response, private_key,
                             globals.wo_submit_tamper)
        input_work_order = self.compute_signature(self.tamper)
        logger.info('Compute Signature complete \n')

        final_json_str = json.loads(input_work_order)
        return final_json_str

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        output = {}
        data = input_json["params"]
        logger.info("JSON object %s \n", input_json)

        config_yaml = self.get_default_params(pre_test_response, data)
        for c_key, c_value in config_yaml.items():
            if c_key in data.keys():
                output[c_key] = data[c_key] if data[c_key] != "" else c_value

        # Convert workloadId to hex
        workload_id = output["workloadId"].encode("UTF-8").hex()
        work_order_id = output.get("workOrderId")
        requesterNonce = output.get("requesterNonce")
        workerEncryptionKey = output.get("workerEncryptionKey")
        logger.info("workload_id %s \n", workload_id)
        logger.info("requester id ---- %s", output["requesterId"])
        logger.info("requester_nonce ---- %s", requesterNonce)

        # Create work order params
        wo_params = WorkOrderParams(
            work_order_id, output["workerId"], workload_id, output["requesterId"],
            self.session_key, self.session_iv, requesterNonce,
            result_uri=" ", notify_uri=" ",
            worker_encryption_key=workerEncryptionKey,
            data_encryption_algorithm=output["dataEncryptionAlgorithm"]
        )

        # Add worker input data
        in_data = input_json["params"]["inData"]
        for rows in in_data:
            for k, v in rows.items():
                if k == "data":
                    dataHash = None
                    encryptedDataEncryptionKey = None
                    if "dataHash" in rows.keys():
                        if rows["dataHash"] != "":
                            dataHash = rows["dataHash"]
                    if "encryptedDataEncryptionKey" in rows.keys():
                        if rows["encryptedDataEncryptionKey"] != "":
                            encryptedDataEncryptionKey = rows["encryptedDataEncryptionKey"]
                    wo_params.add_in_data(rows["data"], dataHash, encryptedDataEncryptionKey)

        # Encrypt work order request hash
        wo_params.add_encrypted_request_hash()

        return wo_params

    def get_default_params(self, pre_response, input_dict):
        d_params = wconfig.read_config(__file__, pre_response)
        try:
            d_params["requesterNonce"] = secrets.token_hex(16)
            d_params["requesterId"]    = secrets.token_hex(32)
            d_params["workerEncryptionKey"] = pre_response.get("result", {}).get("details",
                    {}).get("workerTypeData", {}).get('encryptionKey')
            d_params["workOrderId"] = secrets.token_hex(32)
            if "workloadId" in input_dict.keys():
                d_params["workloadId"] = input_dict["workloadId"]

            if globals.direct_test_mode == "listener":
                d_params["workerEncryptionKey"]  = crypto_utils.strip_begin_end_public_key(d_params["workerEncryptionKey"])
                d_params["sessionKeyIv"]         = self.byte_array_to_hex_str(self.session_iv)
                if self.encrypted_session_key:
                    d_params["encryptedSessionKey"]  = self.byte_array_to_hex_str(self.encrypted_session_key)

        except Exception as e:
            logger.error("Exception Occurred inside get_default_params ", e)
        return d_params
