# TODO

Do it! Remember, keep it simple, effective, eyes on the goal! 



- [x] **Development Process**
  1. Create/update virtual environment:
     ```bash
     rm -rf .venv
     uv venv
     source .venv/bin/activate
     uv pip install -e ".[dev,test]"
     ```
  2. Run formatting and tests:
     ```bash
     hatch fmt --unsafe-fixes
     hatch fmt --unsafe-fixes
     sudo hatch -e test run test
     ```

## 1. Immediate Priorities

- [!] **Security Fixes**
  - *API Calls*:
    - [!] Add timeouts to all requests calls (S113)
      - [!] legacy.py:84,109,201,214
      - [!] njord.py API calls
    - [!] Use full paths for subprocess calls (S607)
      - [!] legacy.py:47,116,157,186,189
    - [!] Validate subprocess inputs (S603)
      - [!] legacy.py subprocess calls
  - *Test Security*:
    - [!] Remove hardcoded passwords (S106)
      - [!] test_config_loading.py:102,112
      - [!] test_legacy_api.py:23
      - [!] test_validation.py:36

- [!] **Test Improvements**
  - *Test Structure*:
    - [!] Fix duplicate test functions (F811)
      - [!] test_connection.py:178
      - [!] test_errors.py:217
    - [!] Add match parameter to pytest.raises() (PT011)
      - [!] test_config_loading.py:297,304,311
      - [!] test_security.py:33
    - [!] Fix private member access (SLF001)
      - [!] test_validation_integration.py:37
      - [!] test_client.py:52
      - [!] test_legacy_api.py:26,35

- [!] **Code Quality**
  - *Error Handling*:
    - [!] Fix blind exception catches (BLE001)
      - [!] legacy.py:205
      - [!] njord.py:64
      - [!] main.py:105
      - [!] client.py:209,243
    - [!] Move cleanup to else blocks (TRY300)
      - [!] legacy.py:190
      - [!] njord.py:45,55
      - [!] client.py:190
    - [!] Abstract raise statements (TRY301)
      - [!] njord.py:34,42
  - *Code Structure*:
    - [!] Fix boolean argument issues (FBT001,FBT002)
      - [!] main.py:13,30
      - [!] client.py:49
    - [!] Fix unnecessary elif blocks (RET505)
      - [!] factory.py:34

## 2. Core Implementation

- [x] **Legacy API (Shell Script Port)**
  - *Core Functionality*:
    - [x] Port server selection from shell script
    - [x] Implement OpenVPN config download and caching
    - [x] Add simple process management (start/kill)
    - [x] Add basic status check via IP lookup
  - *Error Handling*:
    - [x] Add basic error classes
    - [x] Implement simple retry with tenacity
    - [x] Add clear error messages using loguru

- [x] **Njord API Integration**
  - *Core Integration*:
    - [x] Clean up njord client implementation
    - [x] Remove async patterns
    - [x] Simplify status checking
    - [x] Remove complex retry logic
  - *Error Handling*:
    - [x] Map njord errors to our error classes
    - [x] Add loguru logging

## 3. Client Interface

- [x] **Base Client**
  - *API*:
    - [x] Define common interface for both implementations
    - [x] Add country selection
    - [x] Add simple credential management (env vars only)
    - [x] Add basic status methods
  - *Implementation*:
    - [x] Add API selection (njord vs legacy)
    - [x] Add simple factory method
    - [x] Add basic type hints

## 4. CLI Implementation

- [x] **Basic Commands**
  - *Core Commands*:
    - [x] `connect [country]`
    - [x] `disconnect`
    - [x] `status`
    - [x] `list-countries`
  - *Options*:
    - [x] `--api` selection (njord/legacy)
    - [x] `--verbose` for debug logging

## 5. Testing & Documentation

- [!] **Core Tests**
  - *Unit Tests*:
    - [!] Legacy API core functions
    - [!] Njord API wrapper
    - [!] Client interface
    - [!] CLI commands
  - *Integration Tests*:
    - [!] Connection flow
    - [!] Error handling
    - [!] API selection

- [x] **Documentation**
  - *Core Docs*:
    - [x] Installation guide
    - [x] API usage examples
    - [x] CLI usage guide
    - [x] Environment variables
  - *Development*:
    - [!] Architecture overview
    - [!] Contributing guide

Remember: Focus on reliability and simplicity over features. Keep both APIs working independently with a common interface.

