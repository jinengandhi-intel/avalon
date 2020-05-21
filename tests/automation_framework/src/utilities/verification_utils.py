import json
import logging
import avalon_crypto_utils.signature as signature
import avalon_crypto_utils.crypto_utility as enclave_helper
import globals
from error_code.error_status import SignatureStatus
from error_code.error_status import WorkOrderStatus
from src.utilities.generic_utils import TestStep

logger = logging.getLogger(__name__)


def validate_response_code(response, expected_res):
    """ Function to validate work order response.
        Input Parameters : response, check_result
        Returns : err_cd"""
    # check expected key of test case
    check_result = {"error": {"code": 5}}
    check_result_key = list(check_result.keys())[0]
    # check response code
    if check_result_key in response:
        if "code" in check_result[check_result_key].keys():
            if "code" in response[check_result_key].keys():
                if (response[check_result_key]["code"] ==
                        expected_res):
                    err_cd = 0
                    if expected_res == 0:
                        logger.info('SUCCESS: Worker API response "%s"!!',
                                    response[check_result_key]["message"])
                    elif expected_res == 2:
                        logger.info(
                            'Invalid parameter format in response "%s".',
                            response[check_result_key]["message"])
                    elif expected_res == 5:
                        logger.info('SUCCESS: WorkOrderSubmit response'
                                    ' key error and status (%s)!!\
                                 \n', check_result[check_result_key]["code"])
                else:
                    err_cd = 1
                    logger.info(
                        'ERROR: Response did not contain expected code '
                        '%s.\n', check_result[check_result_key]["code"])
            else:
                err_cd = 1
                logger.info('ERROR: Response did not contain expected \
                         code %s. \n', check_result[check_result_key]["code"])
    else:
        check_get_result = '''{"result": {"workOrderId": "", "workloadId": "",
                        "workerId": "", "requesterId": "", "workerNonce": "",
                               "workerSignature": "", "outData": ""}}'''

        check_result = json.loads(check_get_result)

        check_result_key = list(check_result.keys())[0]

        if check_result_key == "result":
            if (set(check_result["result"].keys()).issubset
               (response["result"].keys())):

                # Expected Keys : check_result["result"].keys()
                # Actual Keys : response["result"].keys()
                err_cd = 0
                logger.info('SUCCESS: WorkOrderGetResult '
                            'response has keys as expected!!')
            else:
                err_cd = 1
                logger.info('ERROR: Response did not contain keys \
                as expected in for test case. ')
        else:
            err_cd = 0
            logger.info('No validation performed for the expected result \
            in validate response. ')

    return err_cd


def is_valid_params(request_elements, keys_count=None):
    """
    Fucntion to check the number of parameters in submit requests.
    """
    if keys_count:
        request_keys = sum(keys_count(elem) for elem in request_elements)
    return request_keys


def verify_work_order_signature(response, worker_obj):
    verify_key = worker_obj['result']['details']['workerTypeData']['verificationKey']

    try:
        verify_obj = signature.ClientSignature()
        sig_bool = verify_obj.verify_signature(response, verify_key)

        if sig_bool is SignatureStatus.PASSED:
            err_cd = 0
            logger.info('Success: Work Order Signature Verified.')
        else:
            err_cd = 1
            logger.info('ERROR: Work Order Signature Verification Failed')
    except Exception:
        err_cd = 1
        logger.error('ERROR: Failed to analyze Signature Verification')

    return err_cd


def decrypt_work_order_response(response, session_key, session_iv):
    decrypted_data = ""
    try:
        decrypted_data = enclave_helper.decrypted_response(response,
                                                           session_key,
                                                           session_iv)
        err_cd = 0
        logger.info('Success: Work Order Response Decrypted.\n\n')
    except Exception:
        err_cd = 1
        logger.info('ERROR: Decryption failed %s \
                           where expected. \n', decrypted_data)
        logger.info('ERROR: Work Order Response Decryption Failed')

    return err_cd, decrypted_data


def verify_test(response, expected_res, worker_obj, work_order_obj):

    session_key = work_order_obj.session_key
    session_iv = work_order_obj.session_iv

    verify_wo_signature_err = verify_work_order_signature(response['result'],
                                                          worker_obj)

    assert (verify_wo_signature_err is TestStep.SUCCESS.value)

    decrypt_wo_response_err = decrypt_work_order_response(response['result'],
                                                          session_key,
                                                          session_iv)[0]

    assert (decrypt_wo_response_err is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    validate_response_code_err = validate_response_code(
        response, expected_res)

    assert (validate_response_code_err is TestStep.SUCCESS.value)

    return TestStep.SUCCESS.value


def check_worker_lookup_response(response, operator, value):

    ''' if globals.blockchain_type == "ethereum":
        if operator(response[0], value):
            err_cd = 0
        else:
            err_cd = 1
    else:'''
    if operator(response["result"]["totalCount"], value):
        err_cd = 0
    else:
        err_cd = 1
    return err_cd


def check_worker_retrieve_response(response):

    ''' if globals.blockchain_type == "ethereum":
        if response[0] == 1:
            err_cd = 0
        else:
            err_cd = 1
    else:'''
    if response["result"]["workerType"] == 1:
        err_cd = 0
    else:
        err_cd = 1

    return err_cd


def check_worker_create_receipt_response(response):

    if globals.blockchain_type == "ethereum":
        if response[0] == 1:
            err_cd = 0
        else:
            err_cd = 1
    else:
        if response["error"]["code"] == 0:
            err_cd = 0
        else:
            err_cd = 1

    return err_cd


def check_worker_retrieve_receipt_response(response):
    if globals.blockchain_type == "ethereum":
        if response[0] == 1:
            err_cd = 0
        else:
            err_cd = 1
    else:
        if response["result"]["receiptCurrentStatus"] == 2:
            err_cd = 0
        else:
            err_cd = 1

    return err_cd


def check_negative_test_responses(response, expected_res):

    if expected_res == "Invalid data format for session key iv":
        if response["error"]["message"] == "Invalid data format for session key iv":
            return TestStep.SUCCESS.value

    if expected_res == "CreateWorkloadProcessor function returned null":
        if response["error"]["message"] == "CreateWorkloadProcessor function returned null":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid Request":
        if response["error"]["message"] == "Invalid Request":
            return TestStep.SUCCESS.value

    if expected_res == "Indata is empty":
        if response["error"]["message"] == "Indata is empty":
            return TestStep.SUCCESS.value

    if expected_res == "Server error":
        if response["error"]["message"] == "Server error":
            return TestStep.SUCCESS.value

    if expected_res == "Missing parameter requesterId":
        if response["error"]["message"] == "Missing parameter requesterId":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for responseTimeoutMSecs":
        if response["error"]["message"] == "Invalid data format for responseTimeoutMSecs":
            return TestStep.SUCCESS.value

    if expected_res == "Missing parameter inData":
        if response["error"]["message"] == "Missing parameter inData":
            return TestStep.SUCCESS.value

    if expected_res == "Unsupported dataEncryptionAlgorithm found in the request":
        if response["error"]["message"] == "Unsupported dataEncryptionAlgorithm found in the request":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for initialization vector of in data":
        if response["error"]["message"] == "Invalid data format for initialization vector of in data":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid workload id":
        if response["error"]["message"] == "Invalid workload id":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for data hash of in data":
        if response["error"]["message"] == "Invalid data format for data hash of in data":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for requester id":
        if response["error"]["message"] == "Invalid data format for requester id":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid work order Id":
        if response["error"]["message"] == "Invalid work order Id":
            return TestStep.SUCCESS.value

    if expected_res == "Work order Id not found in the database. Hence invalid parameter":
        if response["error"]["message"] == "Work order Id not found in the database. Hence invalid parameter":
            return TestStep.SUCCESS.value

    if expected_res == "Worker Id not found in the database. Hence invalid parameter":
        if response["error"]["message"] == "Worker Id not found in the database. Hence invalid parameter":
            return TestStep.SUCCESS.value

    if expected_res == "Missing in data parameter data":
        if response["error"]["message"] == "Missing in data parameter data":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for work order id":
        if response["error"]["message"] == "Invalid data format for work order id" or\
            ( response["error"]["message"] == "Server error" and
              response["error"]["data"]["message"] == "'workOrderId'"):
            return TestStep.SUCCESS.value

    if expected_res == "Missing parameter encryptedRequestHash":
        if response["error"]["message"] == "Missing parameter encryptedRequestHash":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for requesterSignature":
        if response["error"]["message"] == "Invalid data format for requesterSignature":
            return TestStep.SUCCESS.value

    if expected_res == "Crypto Error (deserializeECDSAPublicKey): Could not deserialize public ECDSA key":
        if response["error"]["message"] == "Crypto Error (deserializeECDSAPublicKey): Could not deserialize public ECDSA key":
            return TestStep.SUCCESS.value  

    if expected_res == "Invalid data format for requesterNonce":
        if response["error"]["message"] == "Invalid data format for requesterNonce":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for worker encryption key":
        if response["error"]["message"] == "Invalid data format for worker encryption key":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for work load id":
        if response["error"]["message"] == "Invalid data format for work load id":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for in/out data":
        if response["error"]["message"] == "Invalid data format for in/out data":
            return TestStep.SUCCESS.value

    if expected_res == "Invalid data format for Worker id":
        if response["error"]["message"] == "Invalid data format for Worker id":
            return TestStep.SUCCESS.value
      
