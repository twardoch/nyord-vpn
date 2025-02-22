# NordVPN Client Implementation TODO

## 1. Critical Tasks

### 1.1. Modularization

* [x] Create data/countries.py with country mapping
* [x] Create utils/system.py with command and subprocess handling
* [x] Create utils/network.py with IP and connection handling
* [x] Create utils/security.py with credential and path handling
* [!] Fix njord.py integration:
  + [!] Fix pycountry import issues
  + [x] Fix async/await issues with njord client
  + [x] Add proper error handling
* [!] Move remaining functionality from nyord_vpn.py:
  + [!] Move connection management to core/client.py
  + [!] Move CLI functionality to cli/commands.py
  + [!] Remove nyord_vpn.py when done

### 1.2. Fix Critical Issues

* [x] Fix dependency issues:
  + [x] Add pycountry to project dependencies
  + [x] Add aiohttp to project dependencies
  + [x] Add proper version constraints
* [x] Fix type errors in core/client.py:
  + [x] Fix SecretStr type for password
  + [x] Fix Coroutine call issue
  + [x] Fix log_file parameter issue
* [x] Fix security issues:
  + [x] Fix subprocess security (S603) in legacy.py
  + [x] Replace standard RNG with secrets module
  + [x] Add input validation for shell commands
* [x] Fix error handling:
  + [x] Fix blind exception catches (BLE001)
  + [x] Fix try-except block issues (TRY300, TRY301)
  + [x] Add proper error chaining with `from`

### 1.3. Testing Infrastructure

* [x] Set up proper test environment:
  + [x] Add pytest fixtures for API mocking
  + [x] Add subprocess mocking utilities
  + [x] Add network call mocking
  + [x] Add pytest-asyncio to dependencies
  + [x] Set up test configuration

## 2. Next Tasks

### 2.1. Code Quality

* [!] Reduce complexity in core functions:
  + [!] Split `connect_nordvpn` into smaller functions:
    + [!] Extract server selection logic
    + [!] Extract connection setup
    + [!] Extract status checking
  + [!] Improve error handling patterns:
    + [!] Add error context
    + [!] Add error recovery
    + [!] Add error logging
  + [!] Add proper type hints throughout:
    + [!] Add type hints to API layer
    + [!] Add type hints to core layer
    + [!] Add type hints to utils layer
* [!] Improve code organization:
  + [!] Move constants to config module:
    + [!] Move API URLs
    + [!] Move default values
    + [!] Move error messages
  + [!] Create proper configuration classes:
    + [!] Add API configuration
    + [!] Add client configuration
    + [!] Add logging configuration
  + [!] Add configuration validation:
    + [!] Add path validation
    + [!] Add value validation
    + [!] Add type validation

### 2.2. Testing

* [x] Add unit tests:
  + [x] Test API implementations:
    + [x] Test njord.py
    + [x] Test legacy.py
  + [x] Test utility functions:
    + [x] Test system.py
    + [x] Test network.py
    + [x] Test security.py
  + [x] Test configuration handling:
    + [x] Test config loading
    + [x] Test config validation
    + [x] Test environment variables
* [x] Add integration tests:
  + [x] Test connection flow:
    + [x] Test successful connection
    + [x] Test connection failure
    + [x] Test fallback behavior
  + [x] Test error handling:
    + [x] Test network errors
    + [x] Test subprocess errors
    + [x] Test configuration errors
  + [x] Test configuration loading:
    + [x] Test file loading
    + [x] Test environment loading
    + [x] Test default values

### 2.3. Documentation

* [!] Add API documentation:
  + [!] Document public interfaces:
    + [!] Document API classes
    + [!] Document client class
    + [!] Document utility functions
  + [!] Add usage examples:
    + [!] Add library usage examples
    + [!] Add CLI usage examples
    + [!] Add configuration examples
  + [!] Document error handling:
    + [!] Document error types
    + [!] Document error recovery
    + [!] Document error prevention

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
