# NordVPN Client Implementation TODO

## 1. Immediate Next Steps

1. [!] Fix Critical Test Failures:
   - [!] Fix VPNConfig class methods:
     - [!] Add `from_file` method
     - [!] Add `from_env` method
     - [!] Fix config validation and loading
   - [!] Fix test environment setup:
     - [!] Mock nordvpn command in tests
     - [!] Add proper test credentials
     - [!] Fix async test issues with aiohttp session

2. [!] Fix Code Structure Issues:
   - [!] Fix exception handling in network.py:
     - [!] Fix async context manager in get_public_ip
     - [!] Improve error handling in wait_for_connection
   - [!] Fix subprocess handling:
     - [!] Improve command validation
     - [!] Add proper mocking in tests
   - [!] Fix credential handling:
     - [!] Add proper default values
     - [!] Improve validation messages

3. [!] Everywhere in the code, let's settle on ONE WAY to pass the authentication credentials: the NORD_USER and NORD_PASSSWORD environment variables. Adjust all places. 

## 2. Core Functionality (Highest Priority)

### 2.1. Critical Code Quality Issues
+ [!] Remove hardcoded passwords:
    - [!] test_config_loading.py:83,93 - Password in test arguments
    - [!] test_legacy_api.py:23 - Password in API initialization
    - [!] test_njord_api.py:16,40,73,96,128 - Multiple instances
    - [!] test_validation.py:36 - Hardcoded password assignment

### 2.2. Code Structure Improvements
* [!] Fix Exception Handling:
  - [!] Move cleanup code to `else` blocks in:
    - [!] api/legacy.py
    - [!] api/njord.py
    - [!] core/client.py
    - [!] utils/system.py
  - [!] Abstract `raise` statements to inner functions
  - [!] Replace broad exception catches with specific ones
  - [!] Fix redundant exception objects in logging.exception calls

### 2.3. Type System Improvements
* [!] Fix stub file issues in pycountry.pyi:
  - [!] Remove docstrings (PYI021)
  - [!] Fix function bodies (PYI048)
  - [!] Remove unused TypeVar _DB (PYI018)

### 2.4. Security Improvements
* [!] Improve subprocess security:
  - [!] Check for execution of untrusted input in utils/system.py
* [!] Fix logging:
  - [!] Replace f-string logging with proper formatting in core/client.py

### 2.5. Legacy Code Cleanup
* [ ] Remove legacy components:
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
   - Testing:
     * Avoid test duplication
     * Use proper test fixtures
     * Maintain test isolation
     * Avoid accessing private members in tests
   - Type Annotations:
     * Use proper type hints
     * Follow PYI guidelines for function bodies
     * Keep stub files clean and minimal