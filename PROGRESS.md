# Progress Report

## Overview

This progress report tracks the refactoring of the nyord-vpn codebase.

The primary focus of the refactoring effort is to:

1. Improve code quality and maintainability
2. Enhance error handling and user feedback
3. Strengthen security with better validation and randomization
4. Update the API interface for better usability
5. Add comprehensive documentation and testing

Current status: Completed initial refactoring of API and core modules, with focus shifting to improving error handling, fixing test failures, and breaking down complex methods.

## Completed Tasks

- [x] Add module docstrings to all files
- [x] Rename `ConnectionError` to `VPNConnectionError`
- [x] Make boolean parameters keyword-only
- [x] Move main blocks to test files
- [x] API Module refactoring
  - [x] Make `api.py` the central API interface with `NordVPNAPI` class
  - [x] Implement `find_best_server` method with v2 API support and v1 fallback
  - [x] Add deprecation notices and clean up `v1_*.py` files
  - [x] Fix linting issues and improve type hints in `v2_servers.py`
- [x] Core Module initial clean-up
  - [x] Add deprecation warnings to `api.py` and `base.py`
  - [x] Fix boolean positional arguments
- [x] Network Module - `vpn_commands.py`
  - [x] Create `OpenVPNConfig` dataclass with proper validation
  - [x] Implement `get_openvpn_command` function with proper validation
- [x] Network Module - `server.py`
  - [x] Replace random module with secrets module for secure randomization
  - [x] Fix type compatibility issues:
    - [x] Fix Technology type in server_technologies creation
    - [x] Fix parameter type in _select_diverse_servers function 
    - [x] Fix return type in get_country_info function
  - [x] Address security issues in subprocess calls by enhancing hostname validation
  - [x] Add comprehensive type hints for return types, parameters and variables
- [x] Core Module
  - [x] Refactor `client.py` to use the new `NordVPNAPI` class
  - [x] Update `tests/test_server_manager.py` to use `NordVPNAPI` instead of `NordVPNAPIClient`

## Current Tasks

### High Priority

#### Core Module - `client.py`

- [x] Minimize output messages when `--verbose` is not used
  - [x] Update logging configuration to respect the verbose flag
  - [x] Modify command outputs to show minimalistic format (IPADDRESS: VPNSERVERNAME or IPADDRESS: -)
  - [x] Implement helper method for generating minimal output
  - [x] Ensure verbose mode properly enables detailed logging

- [x] Improve error handling and user feedback
  - [x] Add more detailed error messages with troubleshooting steps
  - [x] Implement proper exception handling with specific exception types
  - [x] Add recovery suggestions in error messages
- [ ] Break down complex methods into smaller helper functions
  - [ ] Refactor the `go()` method into smaller functions for each step
  - [ ] Extract connection validation logic into separate functions
  - [ ] Create helper functions for environment variable handling
- [ ] Fix boolean arguments and other linting issues
  - [ ] Make all boolean parameters keyword-only arguments
  - [ ] Fix type annotations for better static analysis
  - [ ] Add proper validation for function parameters

#### Tests

- [ ] Fix test failures
  - [ ] Fix test_openvpn_tcp_validation failure in ServerManager class
  - [ ] Fix test_fetch_all, test_get_servers_by_country, and test_get_servers_by_group failures related to server relationships
  - [ ] Fix test_get_servers test failure related to locations relationship
  - [ ] Fix test_server_filtering failure related to mock implementation
- [ ] Fix import errors in integration tests
  - [ ] Update imports in tests to use `nyord_vpn.exceptions` instead of `nyord_vpn.core.exceptions`
  - [ ] Update class references from `VPNClient` to `Client`
- [ ] Update test fixtures to include missing fields:
  - [ ] Add `type` field to Group model in test fixtures
  - [ ] Add `server_count` field to Country and City models in test fixtures
- [ ] Fix model validation errors:
  - [ ] Update model validation to handle missing fields gracefully
  - [ ] Add default values for optional fields in model definitions

### Medium Priority

#### Network Module - `vpn.py`

- [ ] Make boolean arguments keyword-only
- [ ] Add comprehensive type hints for all functions and methods
- [ ] Implement retry logic for connection attempts with tenacity
- [ ] Break down complex methods:
  - [ ] Split `setup_connection()` into smaller focused functions
  - [ ] Refactor `connect()` method to improve readability
  - [ ] Extract IP validation logic into a utility function
- [ ] Replace random.uniform with secrets.SystemRandom().uniform for better security
- [ ] Improve error handling with specific exception types and recovery mechanisms

#### Utils Module - `templates.py`

- [ ] Fix security vulnerabilities in subprocess calls (S603, S607)
- [ ] Replace datetime.now() and datetime.fromtimestamp() with timezone-aware versions (DTZ005, DTZ006)
- [ ] Fix exception handling issues:
  - [ ] Replace long error messages with proper exception classes (TRY003)
  - [ ] Use `raise ... from err` consistently (B904)
  - [ ] Move try/except out of loops for better performance (PERF203)
  - [ ] Use `else` blocks appropriately after try/except (TRY300)

### Lower Priority

#### Utils Module - `utils.py`

- [ ] Replace os.path functions with pathlib equivalents (PTH110, PTH118, PTH123)
- [ ] Fix security vulnerability in subprocess call (S603)
- [ ] Fix error handling to use `else` blocks appropriately (TRY300)
- [ ] Implement atomic file operations for state management

#### Main Module - `__main__.py`

- [ ] Update CLI class to use the updated Client API
  - [ ] Replace any usage of deprecated classes/methods with their updated counterparts
  - [ ] Update command-line arguments to match new API structure
  - [ ] Ensure all commands use the new Client implementation
- [ ] Improve error handling and user feedback
  - [ ] Add specific error handling for common user errors
  - [ ] Provide clear, actionable error messages with recovery steps
  - [ ] Add verbose output mode for troubleshooting

## Next Steps

The following immediate next steps have been identified based on test failures and prioritized tasks:

1. **Implement minimalistic output format when --verbose is not used**
   - Modify the logging configuration to only show debug/info logs when --verbose is enabled
   - Update Client.go(), Client.bye(), and Client.info() methods to use the minimalistic output format
   - Create a helper function to generate the minimalistic output string in the format "IPADDRESS: VPNSERVERNAME" or "IPADDRESS: -"
   - Test the output with and without the --verbose flag to verify correct behavior

2. **Fix the OpenVPN TCP validation issue in server_manager.py**
   - The `_is_valid_server()` method is incorrectly returning `True` for servers without OpenVPN TCP support
   - Update the logic to properly check for the presence of OpenVPN TCP in the technologies list
   - Add additional logging to help diagnose why the check is failing

3. **Fix model relationship issues in test fixtures**
   - Update sample fixtures to properly include relationships:
     - Add server-to-group relationships in sample_server fixture
     - Add server-to-location relationships in sample_server fixture
     - Add proper type field to Group model in test fixtures
   - Modify fixture functions to ensure relationships are properly established

4. **Fix import errors in integration tests**
   - Update import statements:
     - Change `from nyord_vpn.core.exceptions import ...` to `from nyord_vpn.exceptions import ...`
     - Replace references to `VPNClient` with `Client`
   - Fix mock setup in test_server_manager.py to correctly simulate API response structure

5. **Refactor the Client.go() method into smaller functions**
   - Extract server selection logic into a separate method
   - Create a dedicated method for connection validation
   - Implement retry logic with proper error handling
   - Add detailed error messages with troubleshooting steps for common failures

By addressing these issues, we will improve test reliability and code quality, which will provide a solid foundation for further refactoring work.

### Implementation Plan for Fixing Test Failures

1. **Update the `_is_valid_server()` method in server.py**

   ```python
   def _is_valid_server(self, server: dict) -> bool:
       """Check if a server is valid for OpenVPN TCP connection."""
       # Add debug logging for technologies to diagnose the issue
       if self.verbose:
           technologies = server.get("technologies", [])
           self.logger.debug(f"Server technologies: {technologies}")
           
       # Continue with existing validation logic...
       # Fix the OpenVPN TCP check:
       has_openvpn_tcp = False
       for tech in server.get("technologies", []):
           if isinstance(tech, dict) and "name" in tech:
               tech_name = tech.get("name", "")
               if "OpenVPN TCP" in tech_name:
                   has_openvpn_tcp = True
                   break
       
       if not has_openvpn_tcp:
           if self.verbose:
               self.logger.debug(f"Server {server.get('hostname')} does not support OpenVPN TCP")
           return False
       
       return True
   ```

2. **Update test fixtures for proper relationships**

   ```python
   @pytest.fixture
   def sample_server(sample_group, sample_location, sample_technology):
       """Create a sample server with proper relationships."""
       return {
           "id": 1,
           "name": "us1234.nordvpn.com",
           "station": "us1234",
           "hostname": "us1234.nordvpn.com",
           "status": "online",
           "load": 45,
           "groups": [{"id": 1, "pivot": {"server_id": 1, "group_id": 1}}],
           "locations": [{"id": 1, "pivot": {"server_id": 1, "location_id": 1}}],
           "technologies": [sample_technology],
           # Other fields...
       }
   ```

3. **Fix import errors in integration tests**

   ```python
   # Update imports in affected test files
   from nyord_vpn.exceptions import VPNError, VPNConnectionError
   from nyord_vpn.core.client import Client  # Use Client instead of VPNClient
   ```

4. **Fix mock setup in test_server_manager.py**

   ```python
   # Update the mock to match the actual return structure of the NordVPNAPI.get_servers() method
   mock_api_client.get_servers.return_value = (
       [
           {
               "hostname": "tcp1.nordvpn.com",
               "status": "online",
               "load": 50,
               "country": {"code": "US", "name": "United States"},
               "technologies": [
                   {"id": 5, "name": "OpenVPN TCP", "status": "online"},
               ],
           },
           # More sample servers...
       ],
       [], [], [], []  # Empty lists for groups, services, locations, technologies
   )
   ```
