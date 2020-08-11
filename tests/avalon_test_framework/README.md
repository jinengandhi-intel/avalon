This is a test framework client intended to execute automated tests. The intention is to run tests in direct/ proxy invocation models. This is to validate the response of worker, work order and work order receipts APIs as per Enterprise Ethereum Alliance Off-Chain Trusted Compute Specification v1.1.

**Steps to execute automation test framework:**

1. Build Avalon: Refer to the [BUILD.MD](https://github.com/hyperledger/avalon/blob/master/BUILD.md)

2. Open a Docker container shell using following command: 

    ```bash
    docker exec -it avalon-shell bash
    ```

3. Running automation tests in Listener/SDK/Proxy Mode(Ethereum/Fabric) using markers.

    Listener mode:
    
    Change the test_mode to "listener" in config.toml present inside avalon_test_framework\config folder and run pytest command:
    
    ```bash
    cd $TCF_HOME/tests/avalon_test_framework
    pytest -m listener
    ```
    
    Direct SDK mode:
    
    Change the test_mode to "sdk" in config.toml present inside avalon_test_framework\config folder and run pytest command: 
    
    ```bash
    cd $TCF_HOME/tests/avalon_test_framework
    pytest -m sdk
    ```

    Ethereum or Fabric Proxy mode:
    
    Change the test_mode to "sdk" in config.toml and the blockchain_type to "ethereum" or "fabric" present inside avalon_test_framework\config folder, then run the pytest command:
    
    ```bash
    cd $TCF_HOME/tests/avalon_test_framework
    pytest -m sdk
    ```

4. To run single test:
    ```bash
    cd $TCF_HOME/tests/automation_framework
    pytest -k "test_workordersumit_success"
    ```

5. To run all the tests from specific APIs (e.g Worker Setstatus/Worker Register/Workorder Submit)
    ```bash
    pytest -m sdk tests/worker_tests/test_set_status.py
    pytest -m sdk tests/worker_tests/test_registry.py
    pytest -m sdk tests/work_order_tests/test_submit.py
    ```