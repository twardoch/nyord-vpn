# NordVPN Client Implementation TODO

## 1. Critical Tasks

### 1.1. Modularization
- [!] Move functionality from nyord_vpn.py to proper modules:
  - [!] Move server discovery to api/njord.py:
    - [!] Extract `get_nordvpn_server` and `get_nordvpn_country_id`
    - [!] Move country mapping to data/countries.py
    - [!] Add proper error handling
  - [!] Move system utilities to utils/system.py:
    - [!] Extract `check_command` with proper typing
    - [!] Extract `run_subprocess_safely` with security fixes
    - [!] Add logging and error handling
  - [!] Move network utilities to utils/network.py:
    - [!] Extract `get_public_ip` with retry logic
    - [!] Extract `wait_for_connection` with timeouts
    - [!] Add proper error handling
  - [!] Move security utilities to utils/security.py:
    - [!] Extract credential handling
    - [!] Extract path validation
    - [!] Add proper secrets management

### 1.2. Fix Critical Issues
- [!] Fix type errors in core/client.py:
  - [!] Fix SecretStr type for password
  - [!] Fix Coroutine call issue
  - [!] Fix log_file parameter issue
- [!] Fix security issues:
  - [!] Fix subprocess security (S603) in legacy.py
  - [!] Replace standard RNG with secrets module
  - [!] Add input validation for shell commands
- [!] Fix error handling:
  - [!] Fix blind exception catches (BLE001)
  - [!] Fix try-except block issues (TRY300, TRY301)
  - [!] Add proper error chaining with `from`

### 1.3. Testing Infrastructure
- [!] Set up proper test environment:
  - [!] Add pytest fixtures for API mocking
  - [!] Add subprocess mocking utilities
  - [!] Add network call mocking
  - [!] Set up test configuration

## 2. Next Tasks

### 2.1. Code Quality
- [ ] Reduce complexity in core functions:
  - [ ] Split `connect_nordvpn` into smaller functions
  - [ ] Improve error handling patterns
  - [ ] Add proper type hints throughout
- [ ] Improve code organization:
  - [ ] Move constants to config module
  - [ ] Create proper configuration classes
  - [ ] Add configuration validation

### 2.2. Testing
- [ ] Add unit tests:
  - [ ] Test API implementations
  - [ ] Test utility functions
  - [ ] Test configuration handling
- [ ] Add integration tests:
  - [ ] Test connection flow
  - [ ] Test error handling
  - [ ] Test configuration loading

### 2.3. Documentation
- [ ] Add API documentation:
  - [ ] Document public interfaces
  - [ ] Add usage examples
  - [ ] Document error handling
- [ ] Add development guide:
  - [ ] Document test setup
  - [ ] Document contribution workflow
  - [ ] Add architecture overview

## 3. Development Guidelines

1. Before making changes:
   ```bash
   uv venv; source .venv/bin/activate; uv pip install -e '.[dev,test]'; hatch fmt --unsafe-fixes; hatch test
   ```

2. After changes:
   ```bash
   hatch fmt --unsafe-fixes; hatch test
   ```

3. When editing TODO.md:
   - Use `- [ ]` for pending tasks
   - Use `- [x]` for completed tasks
   - Use `- [!]` for next priority tasks 