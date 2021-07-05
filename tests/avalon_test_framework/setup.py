import os
import toml
import pytest
from http_client.http_jrpc_client import HttpJrpcClient

TCFHOME = os.environ.get("TCF_HOME", "../../")


def read_configtoml():
    """
    Read the config file for setting up the automation environment.
    """

    config_path = TCFHOME + '/tests/avalon_test_framework/config/config.toml'
    with open(config_path) as fd:
        config = toml.load(fd)

    # For worker_register, worker_setstatus and worker_update API's
    # avalon currently doesn't allow access when running in direct mode
    # but allows access when running in Proxy mode. Hence the expected
    # error codes are different for proxy mode vs. direct mode.
    if config['proxy_mode']:
        config['expected_error_code'] = 0
    else:
        config['expected_error_code'] = -32601

    config['uri_client'] = HttpJrpcClient("http://avalon-listener:1947")

    return config


def read_error_strings():
    """
    Read the error strings defined in the toml file.
    """
    config_path = TCFHOME + '/tests/avalon_test_framework/config/error_strings.toml'
    with open(config_path) as fd:
        error_string = toml.load(fd)

    return error_string

