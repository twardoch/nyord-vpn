# Progress Report

## Completed Tasks

- [x] Add module docstrings to all files
  - [x] Created `api/__init__.py` with docstring
  - [x] Confirmed `network/__init__.py` has docstring
  - [x] Added docstring to `storage/models.py`

- [x] Rename `ConnectionError` to `VPNConnectionError`
  - [x] Updated in `exceptions.py`
  - [x] Updated in `storage/models.py`
  - [x] Updated in `core/client.py`
  - [x] Updated in `__init__.py`

- [x] Make boolean parameters keyword-only
  - [x] Updated in `core/client.py`
  - [x] Updated in `core/api.py`
  - [x] Updated in `network/vpn.py`

- [x] Move main blocks to test files
  - [x] Created `tests/test_v1_recommendations.py`
  - [x] Created `tests/test_v1_groups.py`
  - [x] Created `tests/test_v1_technologies.py`
  - [x] Created `tests/test_api.py`
  - [x] Created `tests/test_v2_servers.py`
  - [x] Removed main blocks from corresponding files
    - [x] Removed from `v1_recommendations.py`
    - [x] Removed from `v1_groups.py`
    - [x] Removed from `v1_technologies.py`
    - [x] Removed from `api.py`
    - [x] Removed from `v2_servers.py`

- [x] API Module (`src/nyord_vpn/api/`)
  - [x] `src/nyord_vpn/api/api.py`
    - [x] Remove shebang and any commented-out code at the top
    - [x] Implement `NordVPNAPI` class with proper docstrings and type hints
    - [x] Add `find_best_server` method with v2 API support and v1 fallback
    - [x] Update v1 methods with deprecation notices and keyword-only arguments
  
  - [x] `src/nyord_vpn/api/v1_*.py` files
    - [x] Add deprecation notices to docstrings
    - [x] Fix boolean positional arguments
    - [x] Add proper docstrings to classes and methods
    - [x] Update error handling to use specific exceptions from exceptions.py

  - [x] `src/nyord_vpn/api/v2_servers.py`
    - [x] Fix linting issues, particularly ambiguous variable names (E741)
    - [x] Add proper docstrings to methods
    - [x] Add comprehensive type hints where missing

- [x] Core Module (`src/nyord_vpn/core/`)
  - [x] `src/nyord_vpn/core/api.py` and `src/nyord_vpn/core/base.py`
    - [x] Add deprecation warnings
    - [x] Fix boolean positional arguments and other linting issues

## Remaining Tasks

### Core Module (`src/nyord_vpn/core/`)

#### `src/nyord_vpn/core/client.py`

**Action**: Refactor significantly to use the new API.

- [ ] Update to use the new `NordVPNAPI` class
- [ ] Improve error handling and user feedback
- [ ] Break down complex methods into smaller helper functions
- [ ] Fix boolean arguments and other linting issues

### Network Module (`src/nyord_vpn/network/`)

#### `src/nyord_vpn/network/server.py`

**Action**: Refactor to use new API.

- [ ] Add type hints for functions and variables
- [ ] Replace random.randrange and random.choice with secrets module
- [ ] Address security issues in subprocess calls by validating input
- [ ] Reduce complexity by extracting helper functions

#### `src/nyord_vpn/network/vpn.py`

**Action**: Refactor for better maintainability.

- [ ] Make boolean arguments keyword-only
- [ ] Add type hints
- [ ] Add retry logic for connection attempts
- [ ] Break down complex methods
- [ ] Replace random.uniform with secrets.SystemRandom().uniform
- [ ] Improve error handling

#### `src/nyord_vpn/network/vpn_commands.py`

**Action**: Refactor for better usability.

- [ ] Create `OpenVPNConfig` dataclass
- [ ] Implement `get_openvpn_command` function with proper validation

### Utils Module (`src/nyord_vpn/utils/`)

#### `src/nyord_vpn/utils/templates.py`

**Action**: Simplify with tenacity.

- [ ] Implement retry logic with tenacity
- [ ] Break down complex functions into smaller ones
- [ ] Improve docstrings and type hints

### Main Module Files

#### `src/nyord_vpn/__main__.py`

**Action**: Update to use new API.

- [ ] Update CLI class to use the updated Client
- [ ] Improve error handling and user feedback

### Tests

**Action**: Update to reflect code changes.

- [ ] Update imports to use `VPNConnectionError` instead of `ConnectionError`
- [ ] Update test fixtures to match model requirements
- [ ] Fix validation errors in tests
- [ ] Update integration tests to use correct import paths

### Documentation

**Action**: Update documentation.

- [ ] Update README.md with installation and usage instructions
- [ ] Add API documentation
- [ ] Add usage examples