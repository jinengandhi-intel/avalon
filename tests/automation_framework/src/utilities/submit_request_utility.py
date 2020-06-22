import logging
import json
import time
import os
import config.config as pconfig
import globals
from avalon_sdk.connector.direct.jrpc.jrpc_worker_registry import \
    JRPCWorkerRegistryImpl
from avalon_sdk.connector.direct.jrpc.jrpc_work_order import \
    JRPCWorkOrderImpl
from avalon_sdk.worker.worker_details import \
    WorkerType, WorkerStatus
from avalon_sdk.connector.direct.jrpc.jrpc_work_order_receipt \
    import JRPCWorkOrderReceiptImpl
from avalon_sdk.connector.blockchains.fabric.fabric_worker_registry \
    import FabricWorkerRegistryImpl
from avalon_sdk.connector.blockchains.fabric.fabric_work_order \
    import FabricWorkOrderImpl
from avalon_sdk.connector.blockchains.ethereum.ethereum_worker_registry \
    import EthereumWorkerRegistryImpl
from avalon_sdk.connector.blockchains.ethereum.ethereum_work_order \
    import EthereumWorkOrderProxyImpl
import avalon_sdk.worker.worker_details as worker_details
logger = logging.getLogger(__name__)
TCFHOME = os.environ.get("TCF_HOME", "../../")


def config_file_read():
    config = pconfig.parse_configuration_files(
        globals.conffiles, globals.confpaths)
    logger.info(" URI client %s \n", config["tcf"]["json_rpc_uri"])
    config["tcf"]["json_rpc_uri"] = globals.uri_client_sdk
    return config


def _create_worker_registry_instance(blockchain_type, config):
    # create worker registry instance for direct/proxy model
    if globals.proxy_mode and blockchain_type == 'fabric':
        return FabricWorkerRegistryImpl(config)
    elif globals.proxy_mode and blockchain_type == 'ethereum':
        return EthereumWorkerRegistryImpl(config)
    else:
        logger.info("Direct SDK code path\n")
        return JRPCWorkerRegistryImpl(config)


def _create_work_order_instance(blockchain_type, config):
    # create work order instance for direct/proxy model
    if globals.proxy_mode and blockchain_type == 'fabric':
        return FabricWorkOrderImpl(config)
    elif globals.proxy_mode and blockchain_type == 'ethereum':
        return EthereumWorkOrderProxyImpl(config)
    else:
        logger.info("Direct SDK code path\n")
        return JRPCWorkOrderImpl(config)


def _create_work_order_receipt_instance(blockchain_type, config):
    # create work order receipt instance for direct/proxy model
    if globals.proxy_mode and blockchain_type == 'fabric':
        return None
    elif globals.proxy_mode and blockchain_type == 'ethereum':
        # TODO need to implement
        return None
    else:
        logger.info("Direct SDK code path\n")
        return JRPCWorkOrderReceiptImpl(config)


def submit_request_listener(
        uri_client, input_json_str, output_json_file_name):
    logger.info("Listener code path\n")
    req_time = time.strftime("%Y%m%d_%H%M%S")
    request_method = input_json_str["method"]
    input_json_str = json.dumps(input_json_str)
    # write request to file
    signed_input_file = ('./results/' + output_json_file_name + '_' + req_time
                         + '_request.json')
    with open(signed_input_file, 'w') as req_file:
        req_file.write(json.dumps(input_json_str, ensure_ascii=False))

    logger.info("in submit listener %s", input_json_str)
    if request_method == "WorkOrderGetResult":
        logger.info("- Validating WorkOrderGetResult Response-")
        response = {}

        response_timeout_start = time.time()
        response_timeout_multiplier = ((6000 / 3600) + 6) * 3
        while "result" not in response:
            if "error" in response:
                if response["error"]["code"] != 5:
                    logger.info('WorkOrderGetResult - '
                                'Response received with error code. ')
                    err_cd = 1
                    break

            response_timeout_end = time.time()
            if ((response_timeout_end - response_timeout_start) >
                    response_timeout_multiplier):
                logger.info('ERROR: WorkOrderGetResult response is not \
                                            received within expected time.')
                break
            response = uri_client._postmsg(input_json_str)
    else:
        logger.info('**********Received Request*********\n%s\n', input_json_str)
        response = uri_client._postmsg(input_json_str)
        logger.info('**********Received Response*********\n%s\n', response)

    # write response to file
    response_output_file = ('./results/' + output_json_file_name + '_'
                            + req_time + '_response.json')
    with open(response_output_file, 'w') as resp_file:
        resp_file.write(json.dumps(response, ensure_ascii=False))

    return response


def workorder_submit_sdk(wo_params, input_json_obj=None):
    logger.info("WorkOrderSubmit SDK code path\n")
    if input_json_obj is None:
        req_id = 3
    else:
        req_id = input_json_obj["id"]
    config = config_file_read()
    work_order = _create_work_order_instance(globals.blockchain_type, config)
    logger.info(" work order id %s \n", wo_params.get_work_order_id())
    logger.info(" worker id %s \n", wo_params.get_worker_id())
    logger.info(" Requester ID %s \n", wo_params.get_requester_id())
    logger.info(" To string %s \n", wo_params.to_string())

    logger.info(" worker id %s \n", wo_params.get_worker_id())
    logger.info("Work order submit request : %s, \n \n ",
                wo_params.to_jrpc_string(req_id))
    response = work_order.work_order_submit(
        wo_params.get_work_order_id(),
        wo_params.get_worker_id(),
        wo_params.get_requester_id(),
        wo_params.to_string(),
        id=req_id
    )
    if globals.proxy_mode and (type(response) != dict):
        response = {}
    response["workOrderId"] = wo_params.get_work_order_id()
    logger.info('**********Received Response*********\n%s\n', response)
    return response


def worker_lookup_sdk(worker_type, input_json=None):
    logger.info("WorkerLookUp SDK code path\n")
    if input_json is None:
        jrpc_req_id = 3
    else:
        jrpc_req_id = input_json["id"]
    config = config_file_read()
    worker_dict = {'SGX': WorkerType.TEE_SGX,
                   'MPC': WorkerType.MPC, 'ZK': WorkerType.ZK}
    worker_registry = _create_worker_registry_instance(globals.blockchain_type, config)
    if globals.blockchain_type == "ethereum":
        if worker_type in worker_dict.keys():
            worker = WorkerType.TEE_SGX
        else:
            worker = worker_type
        worker_lookup_response = worker_registry.worker_lookup(
            worker,
            config["WorkerConfig"]["OrganizationId"],
            config["WorkerConfig"]["ApplicationTypeId"],
            jrpc_req_id
        )
    else:
        worker_lookup_response = worker_registry.worker_lookup(
        worker_type=worker_dict.get(worker_type, worker_type), id=jrpc_req_id)
    logger.info("\n Worker lookup response: {}\n".format(
        json.dumps(worker_lookup_response, indent=4)
    ))

    return worker_lookup_response


def worker_register_sdk(register_params, input_json):
    logger.info("WorkerRegister SDK code path\n")
    jrpc_req_id = input_json["id"]
    if input_json is None:
        jrpc_req_id = 3
    else:
        jrpc_req_id = input_json["id"]

    worker_dict = {'SGX': WorkerType.TEE_SGX,
                   'MPC': WorkerType.MPC, 'ZK': WorkerType.ZK}
    config = config_file_read()
    worker_registry = _create_worker_registry_instance(globals.blockchain_type, config)
    if globals.proxy_mode and (globals.blockchain_type == "ethereum"):
        worker_register_result = worker_registry.worker_register(
            register_params["worker_id"],
            worker_dict[register_params["workerType"]],
            register_params["organization_id"],
            register_params["application_type_id"],
            register_params["details"])
    else:
        worker_register_result = worker_registry.worker_register(
            register_params["worker_id"],
            worker_dict[register_params["workerType"]],
            register_params["organization_id"],
            register_params["application_type_id"],
            register_params["details"], jrpc_req_id)
    logger.info("\n Worker register response: {}\n".format(
        json.dumps(worker_register_result, indent=4)))
    return worker_register_result


def worker_setstatus_sdk(set_status_params, input_json):
    logger.info("WorkerSetStatus SDK code path\n")
    logger.info("Worker status params %s \n", set_status_params)
    if input_json is None:
        jrpc_req_id = 3
    else:
        jrpc_req_id = input_json["id"]
    status_dict = {1: WorkerStatus.ACTIVE, 2: WorkerStatus.OFF_LINE,
                   3: WorkerStatus.DECOMMISSIONED,
                   4: WorkerStatus.COMPROMISED}
    config = config_file_read()
    worker_registry = _create_worker_registry_instance(globals.blockchain_type, config)
    if globals.proxy_mode and (globals.blockchain_type == "ethereum"):
        worker_setstatus_result = worker_registry.worker_set_status(
            set_status_params["worker_id"],
            status_dict[set_status_params["status"]])
    else:
        worker_setstatus_result = worker_registry.worker_set_status(
            set_status_params["worker_id"],
            status_dict[set_status_params["status"]], jrpc_req_id)
    if globals.blockchain_type == "fabric":
        result = worker_setstatus_result
        worker_setstatus_result = {}
        worker_setstatus_result["error"] = {"code" : result.value, "message" : ""}
    logger.info("\n Worker setstatus response: {}\n".format(
        json.dumps(worker_setstatus_result, indent=4)))
    return worker_setstatus_result


def worker_retrieve_sdk(worker_id, input_json=None):
    logger.info("WorkerRetrieve SDK code path\n")
    worker_obj = worker_details.SGXWorkerDetails()
    if input_json is None:
        jrpc_req_id = 11
    else:
        jrpc_req_id = input_json["id"]
    config = config_file_read()
    worker_registry = _create_worker_registry_instance(globals.blockchain_type, config)
    if globals.proxy_mode and globals.blockchain_type == 'ethereum':
        for w_id in worker_id:
            worker = worker_registry\
                .worker_retrieve(w_id, jrpc_req_id)
            if worker["result"]["status"] == \
                WorkerStatus.ACTIVE.value:
                worker_retrieve_result = worker
                worker_id = w_id
                break
        logger.info("\n Worker ID\n%s\n", worker_id)
        logger.info("\n Worker retrieve response: {}\n".format(
            json.dumps(worker_retrieve_result, indent=4)))
    else:
        worker_retrieve_result = worker_registry.worker_retrieve(
            worker_id, jrpc_req_id)
        logger.info("\n Worker retrieve response: {}\n".format(
            json.dumps(worker_retrieve_result, indent=4)))

        if "error" in worker_retrieve_result:
            logger.error("Unable to retrieve worker details\n")
            return worker_retrieve_result
    if globals.proxy_mode and globals.blockchain_type == 'fabric':
        response = worker_retrieve_result
        worker_obj.load_worker(json.loads(response[4]))
        worker_retrieve_result = {}
        result = {"workerType" : response[1],
                  "organizationId" : response[2],
                  "applicationTypeId" : response[3],
                  "details" : json.loads(response[4])}
        worker_retrieve_result["result"] = result
    worker_obj.worker_id = worker_id
    worker_retrieve_result["workerId"] = worker_id
    logger.info("\n Worker ID\n%s\n", worker_id)

    return worker_retrieve_result


def worker_update_sdk(update_params, input_json=None):
    logger.info("WorkerUpdate SDK code path\n")
    logger.info("Worker update params %s \n", update_params)
    worker_obj = worker_details.SGXWorkerDetails()
    # update_params = json.loads(update_params)
    if input_json is None:
        jrpc_req_id = 11
    else:
        jrpc_req_id = input_json["id"]
    config = config_file_read()
    worker_registry = _create_worker_registry_instance(globals.blockchain_type, config)
    if globals.proxy_mode and (globals.blockchain_type == "ethereum"):
        worker_update_result = worker_registry.worker_update(
            update_params["worker_id"],
            update_params["details"])
    else:
        worker_update_result = worker_registry.worker_update(
            update_params["worker_id"],
            update_params["details"], jrpc_req_id)
    logger.info("\n Worker update response: {}\n".format(
        json.dumps(worker_update_result, indent=4)))
    return worker_update_result


def workorder_receiptcreate_sdk(wo_create_receipt, input_json):
    logger.info("WorkerReceiptCreate SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = config_file_read()
    # Create receipt
    wo_receipt = _create_work_order_receipt_instance(globals.blockchain_type, config)
    # Submit work order create receipt jrpc request
    wo_receipt_resp = wo_receipt.work_order_receipt_create(
        wo_create_receipt["workOrderId"],
        wo_create_receipt["workerServiceId"],
        wo_create_receipt["workerId"],
        wo_create_receipt["requesterId"],
        wo_create_receipt["receiptCreateStatus"],
        wo_create_receipt["workOrderRequestHash"],
        wo_create_receipt["requesterGeneratedNonce"],
        wo_create_receipt["requesterSignature"],
        wo_create_receipt["signatureRules"],
        wo_create_receipt["receiptVerificationKey"],
        jrpc_req_id
    )
    logger.info("Work order create receipt response : {} \n \n ".format(
        wo_receipt_resp
    ))
    return wo_receipt_resp

def workorder_receiptretrieve_sdk(workorderId, input_json):
    logger.info("ReceiptRetrieve SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = config_file_read()
    # Create receipt
    wo_receipt = _create_work_order_receipt_instance(globals.blockchain_type, config)

    wo_receipt_resp = wo_receipt.work_order_receipt_retrieve(
        workorderId, jrpc_req_id)

    logger.info("Work order retrieve receipt response : {} \n \n ".format(
        wo_receipt_resp
    ))

    # Retrieve last update to receipt by passing 0xFFFFFFFF
    jrpc_req_id += 1
    receipt_update_retrieve = \
        wo_receipt.work_order_receipt_update_retrieve(
            workorderId,
            None,
            1 << 32,
            id=jrpc_req_id)
    logger.info("\n Last update to receipt receipt is:\n {}".format(
        json.dumps(receipt_update_retrieve, indent=4)
    ))

    return receipt_update_retrieve

def workorder_getresult_sdk(workorderId, input_json):
    logger.info("WorkOderGetResult SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = config_file_read()
    work_order = _create_work_order_instance(globals.blockchain_type, config)
    logger.info("----- Validating WorkOrderGetResult Response ------")


    get_result_res = work_order.work_order_get_result(
        workorderId, jrpc_req_id)
    logger.info("******Received Response*****\n%s\n", get_result_res)

    return get_result_res


def workorder_receiptlookup_sdk(requesterId, input_json):
    logger.info("ReceiptRetrieve SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = config_file_read()

    wo_receipt = _create_work_order_receipt_instance(globals.blockchain_type, config)

    wo_receipt_resp = wo_receipt.work_order_receipt_lookup(
        requester_id=requesterId, id=jrpc_req_id)

    logger.info("Work order receipt lookup response : {} \n \n ".format(
        wo_receipt_resp
    ))
    return wo_receipt_resp
