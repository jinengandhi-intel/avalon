import os
from http_client.http_jrpc_client import HttpJrpcClient

# For proxy_mode, define the blockchain_type to
# ethereum or fabric
blockchain_type = ''

# Define the test mode as listener or sdk
test_mode = "sdk"

# Set it to True or False for running with or
# without blockchain
proxy_mode = False

# For worker_register, worker_setstatus and worker_update API's
# avalon currently doesn't allow access when running in direct mode
# but allows access when running in Proxy mode. Hence the expected
# error codes are different for proxy mode vs. direct mode.
if proxy_mode:
    expected_error_code = 0
else:
    expected_error_code = -32601

##########################################################
# The section below defines all the constants that are used
# throughout the test framework.
##########################################################
TCFHOME = os.environ.get("TCF_HOME", "../../")

# Config files path
tcf_connector_conffile = [TCFHOME + "/sdk/avalon_sdk/tcf_connector.toml"]
tcs_config_conffiles = [TCFHOME + "/config/tcs_config.toml"]
confpaths = ["."]

uri_client = HttpJrpcClient("http://avalon-listener:1947")

uri_client_sdk = "http://avalon-listener:1947"

listener_string = "listener"

# Input file path definition for work order tests
work_order_submit_input_file = os.path.join(
    os.getcwd(), 'data', 'work_order', "work_order_submit.yaml")

work_order_getresult_input_file = os.path.join(
    os.getcwd(), 'data', 'work_order', "work_order_get_result.yaml")


# Input file path definition for worker tests
worker_lookup_input_file = os.path.join(
    os.getcwd(), 'data', 'worker', "worker_lookup.yaml")

worker_retrieve_input_file = os.path.join(
    os.getcwd(), 'data', 'worker', "worker_retrieve.yaml")

worker_register_input_file = os.path.join(
    os.getcwd(), 'data', 'worker', "worker_register.yaml")

worker_update_input_file = os.path.join(
    os.getcwd(), 'data', 'worker', "worker_update.yaml")

worker_setstatus_input_file = os.path.join(
    os.getcwd(), 'data', 'worker', "worker_setstatus.yaml")

# Input file path definition for receipt tests
create_receipt_input_file = os.path.join(
    os.getcwd(), 'data', 'receipt', "work_order_create_receipt.yaml")

retrieve_receipt_input_file = os.path.join(
    os.getcwd(), 'data', 'receipt', "work_order_retrieve_receipt.yaml")

receipt_lookup_input_file = os.path.join(
    os.getcwd(), 'data', 'receipt', "work_order_receipt_lookup.yaml")
