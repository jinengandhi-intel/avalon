import os
from http_client.http_jrpc_client import HttpJrpcClient

TCFHOME = os.environ.get("TCF_HOME", "../../")

uri_client = HttpJrpcClient("http://avalon-listener:1947")

uri_client_sdk = "http://avalon-listener:1947"

work_order_input_file = os.path.join(os.getcwd(), 'data', 'work_order')

worker_input_file = os.path.join(os.getcwd(), 'data', 'worker')

work_order_receipt = os.path.join(os.getcwd(), 'data', 'receipt')

# output filename
wo_submit_output_json_file_name = 'work_order_submit'

worker_lookup_output_json_file_name = "worker_lookup"

worker_retrieve_output_json_file_name = "worker_retrieve"

worker_register_output_json_file_name = "worker_register"

worker_setstatus_output_json_file_name = "worker_setstatus"

worker_update_output_json_file_name = "worker_update"

wo_result_output_json_file_name = "work_order_getresult"

wo_create_receipt_output_json_file_name = "work_order_create_receipt"

wo_retrieve_receipt_output_json_file_name = "work_order_retrieve_receipt"

wo_receipt_lookup_output_json_file_name = "work_order_receipt_lookup"

blockchain_type = ''

# Direct test mode = listener or client_sdk
test_mode = "sdk"

proxy_mode = False

# Config file path
conffiles = [TCFHOME + "/sdk/avalon_sdk/tcf_connector.toml"]
confpaths = ["."]

if test_mode == "listener":
    currentPath = os.path.dirname(__file__)
    result_path = os.path.join(currentPath, "results")
    if not os.path.exists(result_path):
        os.mkdir(result_path)

if proxy_mode:
    expected_error_code = 0
else:
    expected_error_code = -32601

