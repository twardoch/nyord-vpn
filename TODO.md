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
    - [x] Add simple process management
    - [x] Add basic status check via IP lookup
  - *Error Handling*:
    - [x] Add basic error classes
    - [x] Implement simple retry with tenacity
    - [x] Add clear error messages using loguru
  - *Country Management*:
    - [ ] Add stored country list
      - [ ] Include all available countries
      - [ ] Map to NordVPN country IDs
      - [ ] Add region information
    - [ ] Add live country fetching
      - [ ] Fetch from API endpoint
      - [ ] Compare with stored list
      - [ ] Update stored list if needed
  - *Fixes Needed*:
    - [ ] Fix incomplete country list in legacy API
    - [ ] Improve server response error handling
    - [ ] Add more verbose connection logging
    - [ ] Add random country selection for default connect

- [x] **Njord API Integration**
  - *Core Integration*:
    - [x] Clean up njord client implementation
    - [x] Remove async patterns
    - [x] Simplify status checking
    - [x] Remove complex retry logic
  - *Error Handling*:
    - [x] Map njord errors to our error classes
    - [x] Add loguru logging
  - *Country Management*:
    - [ ] Add stored country list
      - [ ] Include all available countries
      - [ ] Map to API country codes
      - [ ] Add region information
    - [ ] Add live country fetching
      - [ ] Fetch from API endpoint
      - [ ] Compare with stored list
      - [ ] Update stored list if needed
  - *Fixes Needed*:
    - [ ] Fix status command JSON parsing error
    - [ ] Fix connect command JSON parsing error
    - [ ] Add more verbose connection logging
    - [ ] Add random country selection for default connect

## 3. Client Interface

- [x] **Base Client**
  - *API*:
    - [x] Define common interface
    - [x] Add country selection
    - [x] Add simple credential management
    - [x] Add basic status methods
  - *Implementation*:
    - [x] Add API selection
    - [x] Add simple factory method
    - [x] Add basic type hints
  - *Country Handling*:
    - [ ] Integrate pycountry for proper country code handling
      - [ ] Add support for alpha2 codes (de, pl, etc.)
      - [ ] Add support for country names
      - [ ] Update list-countries to show both formats
      - [ ] Validate country codes/names in connect command
    - [ ] Implement random country selection
      - [ ] Add weighted selection based on server count
      - [ ] Add region-based selection (EU, Americas, etc.)
      - [ ] Add favorite/recent countries

## 4. CLI Implementation

- [x] **Basic Commands**
  - *Core Commands*:
    - [x] Basic command structure
  - *Options*:
    - [x] API selection
    - [x] Verbose logging
  - *Country Commands*:
    - [ ] Add `--countries` command
      - [ ] Fast access to stored country list
      - [ ] Show in `de "Germany"` format
      - [ ] Make this the default country list command
    - [ ] Add `--countries-live` command
      - [ ] Fetch from current API
      - [ ] Show loading progress
      - [ ] Compare with stored list
  - *Improvements Needed*:
    - [ ] Enhanced Verbose Mode
      - [ ] Show target server before connecting
      - [ ] Show connection progress
      - [ ] Show OpenVPN configuration details
      - [ ] Show detailed error information
    - [ ] Better Country Handling
      - [ ] Show both short/long country codes
      - [ ] Support connecting with either format
      - [ ] Add country search/filter
    - [ ] Connection Flow
      - [ ] Add random country support
      - [ ] Show connection attempt details
      - [ ] Better error messages for common issues

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
  - *New Test Cases*:
    - [ ] Country code handling
    - [ ] Random country selection
    - [ ] Verbose mode output
    - [ ] Common error scenarios

## 6. Development Guidelines

1. **Code Style**:
   - [x] Use type hints
   - [x] Keep functions small and focused
   - [x] Use loguru for logging
   - [x] Follow PEP 8

2. **Error Handling**:
   - [x] Use custom error classes
   - [x] Keep error messages clear
   - [x] Use tenacity for retries
   - [x] Log errors with loguru
   - [ ] Improve error messages for common issues
   - [ ] Add more context to error logs

3. **Testing**:
   - [!] Write tests as you implement
   - [!] Mock external services
   - [!] Test both APIs
   - [!] Test error conditions

4. **Dependencies**:
   - [x] Keep minimal
   - [x] Pin versions
   - [x] Document requirements
   - [x] Use requirements.txt

## 7. Code Quality Improvements

- [!] **Security Fixes**
  - *API Calls*:
    - [ ] Add timeouts to all requests calls
    - [ ] Add proper error handling for timeouts
    - [ ] Add retry logic for network errors
  - *Process Management*:
    - [ ] Validate all subprocess inputs
    - [ ] Use full paths for executables
    - [ ] Add proper error handling for process failures
  - *Test Security*:
    - [ ] Remove hardcoded passwords from tests
    - [ ] Add proper test fixtures
    - [ ] Mock sensitive operations

- [!] **Code Cleanup**
  - *Error Handling*:
    - [ ] Replace blind exceptions with specific ones
    - [ ] Add proper error context
    - [ ] Improve error messages
  - *Refactoring*:
    - [ ] Split complex functions
    - [ ] Remove unnecessary else/elif blocks
    - [ ] Fix function argument issues
  - *Type Safety*:
    - [ ] Fix type stub issues
    - [ ] Add missing type hints
    - [ ] Remove unused types

- [!] **Test Infrastructure**
  - *Setup*:
    - [ ] Add proper hatch configuration
    - [ ] Set up pytest fixtures
    - [ ] Add test categories
  - *Coverage*:
    - [ ] Add unit tests for core functionality
    - [ ] Add integration tests
    - [ ] Add security tests
  - *Mocking*:
    - [ ] Mock external services
    - [ ] Mock file operations
    - [ ] Mock process management

Remember: Focus on reliability and simplicity over features. Keep both APIs working independently with a common interface.

## 8. Error Messages and Logging

- [ ] **Error Message Improvements**
  - *Common Errors*:
    - [ ] Add clear message for administrator password prompt
    - [ ] Add clear message for missing credentials
    - [ ] Add clear message for invalid country codes
    - [ ] Add clear message for connection timeouts
  - *API-Specific Errors*:
    - [ ] Improve Njord API JSON parsing errors
    - [ ] Improve Legacy API server response errors
    - [ ] Add API-specific troubleshooting hints

- [ ] **Logging Enhancements**
  - *Connection Flow*:
    - [ ] Log server selection process
    - [ ] Log OpenVPN configuration details
    - [ ] Log connection progress steps
    - [ ] Log IP changes during connection
  - *Debug Information*:
    - [ ] Add request/response logging for API calls
    - [ ] Add OpenVPN process output logging
    - [ ] Add system network interface logging
  - *User Experience*:
    - [ ] Add progress indicators for long operations
    - [ ] Add clear success/failure messages
    - [ ] Add troubleshooting hints in verbose mode

Remember: Focus on reliability and simplicity over features. Keep both APIs working independently with a common interface.

## 9. Country Handling Improvements

- [ ] **Country List Management**
  - *Stored Country List*:
    - [ ] Create pre-made country list in code
      - [ ] Include alpha-2 codes
      - [ ] Include full country names
      - [ ] Include NordVPN country IDs
      - [ ] Add country metadata (region, etc.)
    - [ ] Add `--countries` CLI command
      - [ ] Show stored list in `de "Germany"` format
      - [ ] Add sorting options
      - [ ] Make this the default fast path
  - *Live Country List*:
    - [ ] Add `--countries-live` CLI command
      - [ ] Fetch from API in background
      - [ ] Show loading indicator
      - [ ] Cache results temporarily
      - [ ] Compare with stored list
    - [ ] Add validation against stored list
      - [ ] Warn about missing countries
      - [ ] Update stored list if needed

- [ ] **Pycountry Integration**
  - *Core Integration*:
    - [ ] Add pycountry dependency
    - [ ] Create country code mapping utility
    - [ ] Add country name normalization
    - [ ] Handle special cases (UK vs GB, etc.)
  - *Input Handling*:
    - [ ] Support alpha-2 codes (de, pl)
    - [ ] Support alpha-3 codes (deu, pol)
    - [ ] Support full names (Germany, Poland)
    - [ ] Support case-insensitive matching
  - *Output Formatting*:
    - [ ] Add `de "Germany"` format for list-countries
    - [ ] Add country grouping by region
    - [ ] Add sorting options (by code, name)
    - [ ] Add search/filter capabilities

- [ ] **Country Selection Logic**
  - *Random Selection*:
    - [ ] Add weighted random selection
    - [ ] Add region-based selection
    - [ ] Add preferred server selection
    - [ ] Add load balancing
  - *User Preferences*:
    - [ ] Add favorite countries
    - [ ] Add recently used countries
    - [ ] Add blocked countries
    - [ ] Add custom country groups
  - *Validation*:
    - [ ] Add country code validation
    - [ ] Add server availability check
    - [ ] Add region validation
    - [ ] Add custom validation rules

Remember: Focus on reliability and simplicity over features. Keep both APIs working independently with a common interface.

