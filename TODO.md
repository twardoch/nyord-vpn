# NordVPN Client Implementation TODO

## 1. Core Functionality (Highest Priority)

### 1.1. Simplify and Remove Superfluous Code
* [!] Fix Security Issues:
  + [x] Create secure test credentials configuration
  + [x] Update legacy API tests to use secure credentials
  + [x] Update NjordAPI tests to use secure credentials
  + [x] Update config loading tests to use secure credentials
  + [x] Update connection tests to use secure credentials
  + [x] Update error handling tests to use secure credentials
  + [!] Secure subprocess calls in system utilities
  + [!] Add input validation for command execution
* [!] Fix Package Structure:
  + [x] Add missing __init__.py files to fix namespace package issues
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
  + [!] Fix type annotation issues in client code
  + [!] Ensure mypy runs correctly without custom stubs
* [!] Simplify utilities:
  + [!] Replace custom tempfile handling with stdlib + permission validation
  + [!] Remove unused `generate_secure_token`
  + [!] Consolidate exception classes to minimum necessary set
* [!] Improve Code Structure:
  + [!] Fix exception handling patterns (TRY301 violations)
  + [!] Refactor broad exception catches
  + [!] Clean up private member access in tests

### 1.2. Stabilize Core VPN Functionality
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

### 1.3. Essential Testing
* [!] Core functionality tests:
  + [x] Connection establishment and teardown
  + [!] Error recovery scenarios
  + [!] Configuration validation
* [!] Security tests:
  + [x] Credential handling
  + [!] File permissions
  + [!] Path validation

## 2. Documentation and Polish (After Core Functionality)

### 2.1. User Documentation
* [ ] Add clear installation instructions
* [ ] Document basic usage patterns
* [ ] Provide configuration examples

### 2.2. API Documentation
* [ ] Add docstrings to public interfaces
* [ ] Include usage examples in docstrings
* [ ] Document error handling patterns

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
