import utility.logger as plogger
import pytest
import json
import os
import sys
import logging
import config.config as pconfig
from setup import read_configtoml

logger = logging.getLogger(__name__)
sys.path.append(os.getcwd())

env = read_configtoml()


@pytest.fixture(scope="session", autouse=True)
def setup_config(args=None):
    """ Fixture to setup initial config for pytest session. """

    # parse out the configuration file first
    try:
        config = pconfig.parse_configuration_files(
            [env['tcs_config_conffiles']], [env['confpaths']])
        config_json_str = json.dumps(config, indent=4)
    except pconfig.ConfigurationException as e:
        logger.error(str(e))
        sys.exit(-1)

    plogger.setup_loggers(config.get("Logging", {}))
    sys.stdout = plogger.stream_to_logger((logging.getLogger("STDOUT"),
                                           logging.DEBUG))
    sys.stderr = plogger.stream_to_logger((logging.getLogger("STDERR"),
                                           logging.WARN))

    logger.info("configuration for the session: %s", config)


@pytest.fixture(scope="function")
def setup_teardown(request):
    marker = request.node.get_closest_marker("setup_teardown_data")
    method_name = None
    if marker is None:
        # Handle missing marker in some way...
        test_obj = None
        exit(0)
    else:
        use_fixture = True
        test_obj = marker.args[0]
        method_name = marker.args[1]
        if len(marker.args) == 3:
            use_fixture = marker.args[2]
        if use_fixture:
            pre_test_output = None
            if "WorkerLookUp" in method_name or \
                    "WorkerRegister" in method_name:
                logger.info("No Setup Required for %s test", method_name)
            elif "WorkerRetrieve" in method_name or \
                    "WorkerSetStatus" in method_name or \
                    "WorkerUpdate" in method_name:
                logger.info("Running Setup for %s tests", method_name)
                pre_test_output = test_obj.pre_test_worker_env(method_name)
            elif "WorkOrderSubmit" in method_name:
                logger.info("Running Setup for WorkOrderSubmit tests")
                pre_test_output = test_obj.pre_test_worker_env(method_name)
            elif "WorkOrderGetResult" in method_name or\
                    "WorkOrderReceiptCreate" in method_name:
                logger.info("Running Setup for %s tests", method_name)
                pre_test_output = test_obj.pre_test_worker_env(method_name)
                wo_submit = test_obj.pre_test_workorder_env(
                    method_name, pre_test_output)
                test_obj.setup_output.update(
                    {'pre_test_workorder_output': wo_submit})

            test_obj.setup_output.update(
                {'pre_test_output': pre_test_output})

    yield
    logger.info("Test teardown")
    test_obj.teardown(method_name)
