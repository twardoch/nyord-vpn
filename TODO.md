# NordVPN Client Implementation TODO

## 1. Development Guidelines

1. Before making changes:

   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e '.[dev,test]'
   hatch fmt --unsafe-fixes
   hatch -e test run test
   ```

2. After changes:

   ```bash
   hatch fmt --unsafe-fixes
   hatch -e test run test
   ```

3. When editing TODO.md:

   - Use `- [ ]` for pending tasks
   - Use `- [x]` for completed tasks
   - Use `- [!]` for next priority tasks

4. Code Quality Guidelines:
   - Exception Handling:
     - Move cleanup code to `else` blocks when possible
     - Abstract `raise` statements to inner functions
     - Use specific exception types instead of broad catches
     - Include `match` parameters in pytest.raises()
   - Security:
     - Validate all subprocess inputs
     - Use secure credential management in tests
     - Avoid hardcoded sensitive data
     - Use SecretStr for all password handling
     - Implement proper input validation
   - Testing:
     - Avoid test duplication
     - Use proper test fixtures
     - Maintain test isolation
     - Avoid accessing private members in tests
     - Aim for high test coverage
     - Include both unit and integration tests
   - Type Annotations:
     - Use proper type hints
     - Follow PYI guidelines for function bodies
     - Keep stub files clean and minimal
   - Logging:
     - Use structured logging with loguru
     - Include proper context in log messages
     - Configure appropriate log levels
     - Implement log rotation
     - Redact sensitive data


## 2. Immediate Next Steps

1. [!] HIGHEST PRIORITY: Fix test configuration in conftest.py:
   - [!] Fix test credentials handling:
     - [!] Move TEST_USERNAME and TEST_PASSWORD to environment variables
     - [!] Add proper SecretStr handling for passwords
     - [!] Add validation for test credentials
   - [!] Fix mock_client fixture:
     - [!] Add proper async context management
     - [!] Add proper cleanup
     - [!] Fix mock API responses
   - [!] Fix mock_aiohttp_session fixture:
     - [!] Add proper error responses
     - [!] Add timeout simulation
     - [!] Add network error simulation
   - [!] Fix mock_subprocess fixture:
     - [!] Add proper command validation
     - [!] Add error scenarios
     - [!] Add timeout handling
   - [!] Fix mock_nordvpn_command fixture:
     - [!] Add proper command simulation
     - [!] Add error handling
     - [!] Add status responses

2. [!] Fix failing tests in test_config_loading.py:
   - [!] Fix test_file_loading:
     - [!] Use mock_env_credentials fixture
     - [!] Fix Path resolution for config_dir
     - [!] Verify JSON file handling
   - [!] Fix test_config_validation:
     - [!] Add proper validation for country names using mock_pycountry
     - [!] Add validation for numeric values
     - [!] Improve error messages
   - [!] Fix test_invalid_config_file:
     - [!] Add proper error handling for missing files
     - [!] Add validation for malformed JSON
     - [!] Improve error messages
   - [!] Fix test_invalid_environment:
     - [!] Use mock_env_credentials fixture
     - [!] Add type conversion for numeric values
     - [!] Improve error messages

3. [!] Fix failing connection tests in test_connection.py:
   - [!] Fix test_connect_disconnect:
     - [!] Use mock_client fixture properly
     - [!] Fix status check implementation
     - [!] Add proper cleanup
   - [!] Fix test_connect_with_country:
     - [!] Use mock_pycountry fixture
     - [!] Fix server selection logic
     - [!] Add proper error handling
   - [!] Fix test_connection_failure:
     - [!] Use mock_aiohttp_session for errors
     - [!] Add timeout simulation
     - [!] Add network error handling

4. [!] Fix test configuration issues:
   - [!] Update pyproject.toml:
     - [!] Set asyncio_mode = "strict"
     - [!] Add proper test markers
     - [!] Configure test timeouts
   - [!] Update test fixtures:
     - [!] Add proper async fixture scopes
     - [!] Add proper cleanup
     - [!] Add proper mocking

5. [!] Fix hardcoded passwords in tests (found in multiple files):
   - [!] test_config_loading.py:83,93:
     - [!] Move to environment variables
     - [!] Add proper SecretStr handling
   - [!] test_legacy_api.py:23:
     - [!] Use test fixtures
     - [!] Add proper encryption
   - [!] test_validation.py:36:
     - [!] Use environment variables
     - [!] Add proper validation

6. [!] Fix test issues:
   - [!] Remove duplicate test functions:
     - [!] test_config_loading.py:262 (F811):
       - [!] Merge with existing test
       - [!] Update test cases
     - [!] test_connection.py:178 (F811):
       - [!] Consolidate test cases
       - [!] Update mocks
     - [!] test_errors.py:217 (F811):
       - [!] Merge error handling tests
       - [!] Update assertions
   - [!] Add match parameter in pytest.raises():
     - [!] test_config_loading.py:
       - [!] Add specific error messages
       - [!] Update assertions
     - [!] test_security.py:
       - [!] Add specific error patterns
       - [!] Update error handling

7. [!] Fix private member access in tests:
   - [!] test_validation_integration.py:37:
     - [!] Add public interface
     - [!] Update test approach
   - [!] test_client.py:52:
     - [!] Add proper mocking
     - [!] Use public methods
   - [!] test_legacy_api.py:26,35:
     - [!] Add public interface
     - [!] Update test strategy

8. [!] Fix stub file issues in pycountry.pyi:
   - [!] Remove docstrings (PYI021)
   - [!] Fix function bodies (PYI048)
   - [!] Remove unused TypeVar _DB (PYI018)

9. [!] NEXT TODO: Standardize authentication credentials:
   - [!] Use ONLY NORD_USER and NORD_PASSWORD environment variables
   - [!] Remove all other credential passing methods
   - [!] Update credential file handling to use these variables

10. [ ] Fix exception handling and cleanup in utils/system.py:
    - [ ] Fix multiple TRY300 issues (move cleanup to else blocks)
    - [ ] Fix TRY301 issues (abstract raise statements)
    - [ ] Fix S603 issue (validate subprocess inputs)

11. [ ] Fix broad exception handling:
    - [ ] api/legacy.py (BLE001)
    - [ ] api/njord.py (BLE001)
    - [ ] cli/commands.py (BLE001)
    - [ ] core/client.py (BLE001)
    - [ ] utils/security.py (BLE001)

12. [ ] Fix cleanup code placement:
    - [ ] Move cleanup to else blocks in api/legacy.py
    - [ ] Move cleanup to else blocks in api/njord.py
    - [ ] Move cleanup to else blocks in core/client.py
    - [ ] Move cleanup to else blocks in utils/system.py

## 3. Core Functionality (High Priority)

### 3.1. Code Quality Issues

- [x] Identify all linting errors (completed via hatch fmt)
- [ ] Fix test issues:
  - [ ] Improve pytest.raises() usage:
    - [ ] Add match parameter in test_config_loading.py
    - [ ] Add match parameter in test_security.py

### 3.2. Security Improvements

- [!] Improve credential management:
  - [!] Use keyring for secure credential storage
  - [!] Remove all instances of plaintext password logging
  - [!] Add input validation for environment variables
  - [!] Implement secure token handling
- [!] Enhance subprocess security:
  - [!] Add command injection prevention
  - [!] Validate all command inputs
  - [!] Implement proper error handling for failed commands

### 3.3. Logging Improvements

- [ ] Replace custom logging with loguru:
  - [ ] Remove log_utils.py
  - [ ] Update all logging calls to use loguru
  - [ ] Add structured logging with proper context
- [ ] Fix logging issues:
  - [ ] Replace f-string logging with proper formatting
  - [ ] Fix redundant exception objects in logging.exception calls
  - [ ] Add proper log rotation configuration
  - [ ] Implement log level configuration via environment variables

### 3.4. Test Coverage Improvements

- [ ] Increase test coverage:
  - [ ] Add tests for utils/network.py
  - [ ] Add tests for utils/retry.py
  - [ ] Add tests for utils/security.py
  - [ ] Add tests for utils/system.py
- [ ] Improve test quality:
  - [ ] Add integration tests for VPN connection
  - [ ] Add error handling tests
  - [ ] Add configuration validation tests
  - [ ] Add security-related tests

### 3.5. Type System Improvements

- [!] Fix stub file issues in pycountry.pyi:
  - [!] Remove docstrings (PYI021)
  - [!] Fix function bodies (PYI048)
  - [!] Remove unused TypeVar _DB (PYI018)

### 3.6. Legacy Code Cleanup

- [ ] Remove legacy components:
  - [ ] Delete `oldsh` directory after verifying functionality
  - [ ] Remove `nyord_vpn.py` after verifying all functionality is in `cli/commands.py`

