# NordVPN Client Implementation TODO

## 1. Development Guidelines

1. Before making changes:

   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e '.[dev,test]'
   hatch fmt --unsafe-fixes  # CRITICAL: This identifies code quality issues
   sudo hatch -e test run test # WE HAVE TO USE sudo
   ```

2. After changes:

   ```bash
   hatch fmt --unsafe-fixes  # CRITICAL: Run this twice to ensure all fixes are applied
   hatch fmt --unsafe-fixes
   sudo hatch -e test run test # WE HAVE TO USE sudo
   ```

3. When editing TODO.md:

   - Use `- [ ]` for pending tasks
   - Use `- [x]` for completed tasks
   - Use `- [!]` for next priority tasks
   - Update priorities based on formatting check results
   - Add error codes (e.g., PYI021, BLE001) to tasks for tracking

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

1. [!] HIGHEST PRIORITY: Fix test execution environment:
   - [!] Fix package installation issues with uv
   - [!] Verify test command execution with sudo
   - [!] Ensure proper virtual environment activation
   - [!] Validate test dependencies installation

2. [!] HIGHEST PRIORITY: Fix stub file issues in pycountry.pyi:
   - [!] Remove docstrings (PYI021) - Found in formatting results
   - [!] Fix function bodies (PYI048) - Found in formatting results
   - [!] Remove unused TypeVar _DB (PYI018) - Found in formatting results

3. [!] Fix hardcoded passwords in tests:
   - [!] test_config_loading.py:83,93 (S106):
     - [!] Move to environment variables
     - [!] Add proper SecretStr handling
   - [!] test_legacy_api.py:23 (S106):
     - [!] Use test fixtures
     - [!] Add proper encryption
   - [!] test_validation.py:36 (S105):
     - [!] Use environment variables
     - [!] Add proper validation

4. [!] Fix test issues:
   - [!] Remove duplicate test functions:
     - [!] test_config_loading.py:262 (F811)
     - [!] test_connection.py:178 (F811)
     - [!] test_errors.py:217 (F811)
   - [!] Add match parameter in pytest.raises():
     - [!] test_config_loading.py (PT011)
     - [!] test_security.py (PT011)

5. [!] Fix private member access in tests:
   - [!] test_validation_integration.py:37 (SLF001)
   - [!] test_client.py:52 (SLF001)
   - [!] test_legacy_api.py:26,35 (SLF001)

6. [!] Fix exception handling and cleanup in utils/system.py:
   - [!] Fix multiple TRY300 issues (move cleanup to else blocks)
   - [!] Fix TRY301 issues (abstract raise statements)
   - [!] Fix S603 issue (validate subprocess inputs)

7. [!] Fix broad exception handling (BLE001):
   - [!] api/legacy.py
   - [!] api/njord.py
   - [!] cli/commands.py
   - [!] core/client.py
   - [!] utils/security.py

8. [!] Fix cleanup code placement (TRY300):
   - [!] Move cleanup to else blocks in api/legacy.py
   - [!] Move cleanup to else blocks in api/njord.py
   - [!] Move cleanup to else blocks in core/client.py
   - [!] Move cleanup to else blocks in utils/system.py

9. [!] Fix newly discovered issues:
   - [!] Fix SIM117 in test_security.py (use single with statement)
   - [!] Fix FBT003 in test_validation.py (boolean positional value)
   - [!] Fix RET506 in utils/security.py (unnecessary else after raise)

## 3. Core Functionality (High Priority)

### 3.1. Code Quality Issues

- [x] Identify all linting errors (completed via hatch fmt)
- [x] Run initial formatting checks
- [!] Fix test issues:
  - [!] Improve pytest.raises() usage:
    - [!] Add match parameter in test_config_loading.py
    - [!] Add match parameter in test_security.py

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

