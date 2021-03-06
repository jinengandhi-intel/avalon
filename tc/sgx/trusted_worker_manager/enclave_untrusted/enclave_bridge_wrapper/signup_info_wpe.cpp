/* Copyright 2020 Intel Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "tcf_error.h"
#include "swig_utils.h"

#include "signup_wpe.h"
#include "signup_info_wpe.h"

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
SignupInfo* SignupInfoWPE::DeserializeSignupInfo(
   const std::string&  serialized_signup_info) {

   SignupInfo* signup_info = new SignupInfoWPE();
    tcf_err_t result = signup_info->DeserializeSignupInfo(
        serialized_signup_info);
    return signup_info;
}  // SignupInfoWPE::DeserializeSignupInfo

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
std::string SignupInfoWPE::GenerateNonce(size_t nonce_size) {
    tcf_err_t presult;

    std::string nonce;
    SignupDataWPE signup_data_wpe;
    presult = signup_data_wpe.GenerateNonce(nonce, nonce_size);
    ThrowTCFError(presult);

    return nonce;
}  // SignupInfoWPE::GenerateNonce

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
std::map<std::string, std::string> SignupInfoWPE::CreateEnclaveData(
    const std::string& in_ext_data,
    const std::string& in_ext_data_signature,
    const std::string& in_kme_attestation) {
    tcf_err_t presult;
    // Create some buffers for receiving the output parameters
    // CreateEnclaveData will resize appropriately
    StringArray public_enclave_data(0);
    Base64EncodedString enclave_quote;

    SignupDataWPE signup_data_wpe;
    // sealed data is not generated in case of WPE
    presult = signup_data_wpe.CreateEnclaveData(
        in_ext_data, in_ext_data_signature, in_kme_attestation,
        public_enclave_data, enclave_quote);

    ThrowTCFError(presult);

    // Parse the json and save the verifying and encryption keys
    std::string verifying_key;
    std::string encryption_key;
    std::string encryption_key_signature;

    presult = SignupInfo::DeserializePublicEnclaveData(
        public_enclave_data.str(),
        verifying_key,
        encryption_key,
        encryption_key_signature);
    ThrowTCFError(presult);

    // Save the information
    std::map<std::string, std::string> result;
    result["verifying_key"] = verifying_key;
    result["encryption_key"] = encryption_key;
    result["encryption_key_signature"] = encryption_key_signature;
    // sealing of enclave data is not done in WPE, hence keeping it empty
    result["sealed_enclave_data"] = "";
    result["enclave_quote"] = enclave_quote;

    return result;
}  // SignupInfoWPE::CreateEnclaveData

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
size_t SignupInfoWPE::VerifyEnclaveInfo(
    const std::string& enclave_info,
    const std::string& mr_enclave,
    const std::string& ext_data) {

    SignupDataWPE signup_data_wpe;
    tcf_err_t result = signup_data_wpe.VerifyEnclaveInfo(
        enclave_info, mr_enclave, ext_data);
    return (size_t) result;
}  // SignupInfoWPE::VerifyEnclaveInfo
