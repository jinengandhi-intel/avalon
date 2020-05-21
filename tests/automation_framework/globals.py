import os
from http_client.http_jrpc_client \
    import HttpJrpcClient

TCFHOME = os.environ.get("TCF_HOME", "../../")

uri_client = HttpJrpcClient("http://avalon-listener:1947")

uri_client_sdk = "http://avalon-listener:1947"

work_order_input_file = os.path.join(os.getcwd(), 'data', 'work_order')

worker_input_file = os.path.join(os.getcwd(), 'data', 'worker')

work_order_receipt = os.path.join(os.getcwd(), 'data', 'receipt')

# expected response
check_submit = {"error": {"code": 5}}

# tamper parameters
wo_submit_tamper = {"params": {}}

# request mode - file, string or object
wo_submit_request_mode = "file"

# output filename
wo_submit_output_json_file_name = 'work_order_success'

wo_result_request_mode = "object"

wo_result_tamper = {}

wo_result_output_json_file_name = "work_order_get_result"

worker_request_mode = "file"

worker_lookup_tamper = {"params": {}}

worker_lookup_output_json_file_name = "worker_lookup"

worker_request_id = 0

worker_retrieve_output_json_file_name = "worker_retrieve"

worker_retrieve_tamper = {"params": {}}

worker_status_tamper = {"params": {}}

worker_status_output_json_file_name = 'worker_set_status'

wo_result_output_json_file_name = "worker_get_result"

proxy_worker_registry_contract_address = "0x75a3Fd17E8c5CceAa9121251c359bFe4b9C343C8"

work_order_contract_address = "0xf873133fae1d1f80642c551a6edd5A14f37129c2"

eth_account = "0x7085d4d4c6efea785edfba5880bb62574e115626"

provider = "http://10.66.241.55:22001"

event_provider = "http://10.66.241.55:22011"

blockchain_type = ''

# Direct test mode = listener or client_sdk
direct_test_mode = "sdk"

proxy_mode = False 

# Config file path
conffiles = [TCFHOME + "/sdk/avalon_sdk/tcf_connector.toml"]
confpaths = ["."]

if direct_test_mode == "listener":
    currentPath = os.path.dirname(__file__)
    result_path = os.path.join(currentPath, "results")
    if not os.path.exists(result_path):
        os.mkdir(result_path)
