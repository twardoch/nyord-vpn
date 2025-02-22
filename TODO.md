# NordVPN Client Implementation TODO

## 1. Immediate Next Steps

1. Fix critical security violations:
   - [ ] system.py:84 - Add input validation for subprocess calls
   - [ ] Remove all hardcoded passwords from tests

2. Fix exception handling:
   - [ ] Fix TRY300 violations in legacy.py and njord.py
   - [ ] Fix BLE001 violations in legacy.py and njord.py
   - [ ] Fix remaining TRY300/BLE001 in other files

3. Improve test quality:
   - [ ] Remove test duplication (F811 violations)
   - [ ] Add match parameters to pytest.raises()
   - [ ] Fix private member access in tests

## 2. Core Functionality (Highest Priority)

### 2.1. Critical Code Quality Issues
* [!] Fix Security Violations:
  + [!] Fix S603 (Subprocess security):
    - [!] system.py:84 - Check for execution of untrusted input
  + [!] Remove hardcoded passwords:
    - [!] test_config_loading.py:83,93 - Password in test arguments
    - [!] test_legacy_api.py:23 - Password in API initialization
    - [!] test_njord_api.py:16,40,73,96,128 - Multiple instances
    - [!] test_validation.py:36 - Hardcoded password assignment

* [!] Fix Exception Handling:
  + [!] Fix TRY300 (Move to else blocks):
    - [!] legacy.py:134,165 - Connection handling
    - [!] njord.py:161,187,208 - Server and status handling
    - [!] client.py:142,154,167,180 - Core operations
    - [!] system.py:24,47,96 - System operations
    - [!] security.py:35,110 - Security operations
  + [!] Fix BLE001 (Blind exception catches):
    - [!] legacy.py:137,168,217 - API operations
    - [!] njord.py:164,169,188,209,226 - Multiple catches
    - [!] commands.py:195 - Command handling
    - [!] security.py:88 - Security operations

* [!] Fix Complex Functions:
  + [!] njord.py:43 - Refactor get_recommended_server (complexity: 12 > 10)

### 2.2. Test Quality Improvements
* [!] Fix Test Architecture:
  + [!] Remove test duplication (F811):
    - [!] test_config_loading.py:262 - test_config_precedence
    - [!] test_connection.py:178 - test_connection_failure
    - [!] test_errors.py:217 - test_network_errors
  + [!] Fix private member access (SLF001):
    - [!] test_validation_integration.py:37 - _get_servers
    - [!] test_client.py:52 - _connect
    - [!] test_legacy_api.py:26,35 - _get_servers
    - [!] test_njord_api.py - Multiple private accesses
  + [!] Improve exception testing:
    - [!] test_config_loading.py:314,321,328 - Add match parameters
    - [!] test_security.py:32 - Specify OSError cases

### 2.3. Type System Improvements
* [!] Fix stub file issues:
  + [!] pycountry.pyi - Remove docstrings (PYI021)
  + [!] pycountry.pyi - Fix function bodies (PYI048)
  + [!] Remove unused TypeVar _DB (PYI018)

### 2.4. Simplify and Remove Superfluous Code
* [x] Fix Security Issues:
  + [x] Create secure test credentials configuration
  + [x] Update legacy API tests to use secure credentials
  + [x] Update NjordAPI tests to use secure credentials
  + [x] Update config loading tests to use secure credentials
  + [x] Update connection tests to use secure credentials
  + [x] Update error handling tests to use secure credentials
  + [x] Secure subprocess calls in system utilities:
    - [x] Add command validation
    - [x] Add permission checks
    - [x] Implement process isolation
    - [x] Add output safety measures
  + [x] Add input validation:
    - [x] Create validation module
    - [x] Add country name/code validation
    - [x] Add credentials validation
    - [x] Add hostname validation
    - [x] Add command path validation
    - [x] Add environment variable validation
    - [x] Update LegacyAPI to use validation
    - [x] Update NjordAPI to use validation
    - [x] Add comprehensive validation tests
* [!] Fix Code Quality Issues (Based on Latest Tests):
  + [x] Fix TRY301 violations
  + [!] Fix TRY300 violations (Move statements to else blocks):
    - [!] Fix in legacy.py (Lines 134, 165)
    - [!] Fix in njord.py (Lines 161, 187, 208)
    - [!] Fix in client.py (Lines 142, 154, 167, 180)
    - [!] Fix in system.py (Lines 24, 47, 96)
    - [!] Fix in security.py (Lines 35, 110)
  + [!] Fix BLE001 violations (Blind exception catches):
    - [!] Fix in legacy.py (Lines 137, 168, 217)
    - [!] Fix in njord.py (Lines 164, 169, 188, 209, 226)
    - [!] Fix in commands.py (Line 195)
    - [!] Fix in security.py (Line 88)
  + [!] Fix S603 violations (Subprocess security):
    - [!] Fix in system.py (Line 84)
* [!] Fix Complex Functions:
  + [!] Refactor `get_recommended_server` in njord.py (complexity: 12 > 10)
* [!] Test Quality Improvements:
  + [!] Fix test duplication issues:
    - [!] test_config_loading.py (Line 262)
    - [!] test_connection.py (Line 178)
    - [!] test_errors.py (Line 217)
  + [!] Fix test security:
    - [!] Remove hardcoded passwords (test_config_loading.py, test_legacy_api.py, test_njord_api.py)
    - [!] Fix broad exception catches (test_config_loading.py Lines 314, 321, 328)
  + [!] Fix private member access:
    - [!] test_validation_integration.py (Line 37)
    - [!] test_client.py (Line 52)
    - [!] test_legacy_api.py (Lines 26, 35)
    - [!] test_njord_api.py (Multiple lines)
* [!] Fix Package Structure:
  + [x] Add missing __init__.py files
  + [!] Clean up package imports
  + [!] Verify package installation works correctly
* [!] Replace logging system:
  + [!] Remove custom logging in `log_utils.py`
  + [!] Implement loguru with basic configuration
  + [!] Add secure log rotation and level configuration
* [!] Remove legacy components:
  + [!] Delete `oldsh` directory
  + [!] Remove `nyord_vpn.py` after verifying all functionality is in `cli/commands.py`
* [!] Clean up type handling:
  + [x] Remove `types/pycountry.pyi`
  + [!] Fix type annotation issues in client code:
    - [!] Fix PYI036 violations in client.py
    - [!] Fix PYI021 violations in pycountry.pyi
    - [!] Fix PYI048 violations in pycountry.pyi
  + [!] Ensure mypy runs correctly without custom stubs
* [!] Simplify utilities:
  + [!] Replace custom tempfile handling with stdlib + permission validation
  + [!] Remove unused `generate_secure_token`
  + [!] Consolidate exception classes to minimum necessary set
* [!] Improve Code Structure:
  + [!] Fix exception handling patterns (TRY301 violations)
  + [!] Refactor broad exception catches
  + [!] Clean up private member access in tests

### 2.5. Stabilize Core VPN Functionality
* [!] Focus on NjordAPI:
  + [!] KEEP LegacyAPI implementation!!! But don't spend much effort in perfectioning it. 
  + [!] Enhance NjordAPI error handling and recovery
  + [!] Add comprehensive tests for NjordAPI
* [!] Improve configuration:
  + [x] Consolidate settings in `VPNConfig` class
  + [!] Add pydantic validators for all config parameters
  + [!] Move file permission validation to config loading
* [!] Enhance error handling:
  + [!] Implement proper connection timeout handling
  + [!] Add credential validation
  + [!] Add network reachability checks

### 2.6. Essential Testing
* [!] Core functionality tests:
  + [x] Connection establishment and teardown
  + [!] Error recovery scenarios
  + [!] Configuration validation
* [!] Security tests:
  + [x] Credential handling
  + [!] File permissions
  + [!] Path validation
* [!] Test Quality Improvements:
  + [!] Fix test duplication issues:
    - [!] Resolve F811 violations in test_config_loading.py
    - [!] Resolve F811 violations in test_connection.py
    - [!] Resolve F811 violations in test_errors.py
  + [!] Improve test specificity:
    - [!] Add match parameters to pytest.raises() calls
    - [!] Replace broad exception catches with specific ones
  + [!] Fix test security issues:
    - [!] Remove hardcoded passwords from tests
    - [!] Implement proper test credential management
  + [!] Clean up test architecture:
    - [!] Fix private member access in tests
    - [!] Implement proper test fixtures
    - [!] Add proper test isolation

## 3. Documentation and Polish (After Core Functionality)

### 3.1. User Documentation
* [ ] Add clear installation instructions
* [ ] Document basic usage patterns
* [ ] Provide configuration examples

### 3.2. API Documentation
* [ ] Add docstrings to public interfaces
* [ ] Include usage examples in docstrings
* [ ] Document error handling patterns

### 3.3. Code Quality Improvements
* [!] Fix Complex Functions:
  + [!] Refactor `get_recommended_server` in njord.py (complexity: 12 > 10)
  + [!] Simplify exception handling in client.py
  + [!] Clean up subprocess calls in system.py
* [!] Improve Type Safety:
  + [!] Fix all PYI036 violations in client.py
  + [!] Clean up pycountry.pyi stubs
  + [!] Add proper type hints for exception handling
* [!] Enhance Test Quality:
  + [!] Add proper test isolation
  + [!] Implement comprehensive test fixtures
  + [!] Remove all hardcoded test credentials

## 4. Development Guidelines

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
     * Use proper type hints in `__aexit__`
     * Keep stub files clean and minimal
     * Follow PYI guidelines for function bodies