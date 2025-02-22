# NordVPN Client Implementation TODO

## 1. Immediate Next Steps

1. [!] Everywhere in the code, let's settle on ONE WAY to pass the authentication credentials: the NORD_USER and NORD_PASSSWORD environment variables. Adjust all places:
   - [!] Fix hardcoded passwords in tests:
     - [!] test_config_loading.py:83,93
     - [!] test_legacy_api.py:23
     - [!] test_validation.py:36
   - [!] Use SecretStr consistently for password handling:
     - [!] api/legacy.py
     - [!] api/njord.py
     - [!] core/client.py

2. [!] Fix Code Structure Issues:
   - [!] Fix subprocess handling:
     - [!] Improve command validation in utils/system.py:139 (S603)
     - [!] Fix error handling and cleanup in utils/system.py
   - [!] Fix credential handling:
     - [!] Add proper default values
     - [!] Improve validation messages
   - [!] Fix exception handling:
     - [!] Move cleanup code to `else` blocks in:
       - [!] api/legacy.py (multiple locations)
       - [!] api/njord.py (multiple locations)
       - [!] core/client.py
       - [!] utils/system.py
     - [!] Replace broad exception catches with specific ones:
       - [!] api/legacy.py (BLE001)
       - [!] api/njord.py (BLE001)
       - [!] cli/commands.py (BLE001)
       - [!] core/client.py (BLE001)
       - [!] utils/security.py (BLE001)

## 2. Core Functionality (High Priority)

### 2.1. Code Quality Issues
- [!] Fix test issues:
  - [!] Remove duplicate test functions:
    - [!] test_config_loading.py:262 (F811)
    - [!] test_connection.py:178 (F811)
    - [!] test_errors.py:217 (F811)
  - [!] Improve pytest.raises() usage:
    - [!] Add match parameter in test_config_loading.py
    - [!] Add match parameter in test_security.py
  - [!] Fix private member access in tests:
    - [!] test_validation_integration.py:37
    - [!] test_client.py:52
    - [!] test_legacy_api.py:26,35

### 2.2. Security Improvements
- [!] Improve credential management:
  - [!] Use keyring for secure credential storage
  - [!] Remove all instances of plaintext password logging
  - [!] Add input validation for environment variables
  - [!] Implement secure token handling
- [!] Enhance subprocess security:
  - [!] Add command injection prevention
  - [!] Validate all command inputs
  - [!] Implement proper error handling for failed commands
- [!] Improve error messages:
  - [!] Remove sensitive data from error messages
  - [!] Add proper redaction for logs containing credentials

### 2.3. Type System Improvements
- [!] Fix stub file issues in pycountry.pyi:
  - [!] Remove docstrings (PYI021)
  - [!] Fix function bodies (PYI048)
  - [!] Remove unused TypeVar _DB (PYI018)

### 2.4. Legacy Code Cleanup
- [ ] Remove legacy components:
  - [ ] Delete `oldsh` directory after verifying functionality
  - [ ] Remove `nyord_vpn.py` after verifying all functionality is in `cli/commands.py`

## 3. Development Guidelines

1. Before making changes:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e '.[dev,test]'
   hatch fmt --unsafe-fixes
   hatch test
   ```

2. After changes:
   ```bash
   hatch fmt --unsafe-fixes
   hatch test
   ```

3. When editing TODO.md:
   - Use `- [ ]` for pending tasks
   - Use `- [x]` for completed tasks
   - Use `- [!]` for next priority tasks 

4. Code Quality Guidelines:
   - Exception Handling:
     * Move cleanup code to `else` blocks when possible
     * Abstract `raise` statements to inner functions
     * Use specific exception types instead of broad catches
     * Include `match` parameters in pytest.raises()
   - Security:
     * Validate all subprocess inputs
     * Use secure credential management in tests
     * Avoid hardcoded sensitive data
     * Use SecretStr for all password handling
     * Implement proper input validation
   - Testing:
     * Avoid test duplication
     * Use proper test fixtures
     * Maintain test isolation
     * Avoid accessing private members in tests
   - Type Annotations:
     * Use proper type hints
     * Follow PYI guidelines for function bodies
     * Keep stub files clean and minimal