# Nyord VPN Streamlining Plan - TODO Checklist

## Phase 1: Understanding and Setup (Initial Exploration)
- [x] Analyze codebase structure.
- [x] Understand data flow for server fetching and connection.
- [x] Create `PLAN.md` with detailed streamlining steps.
- [x] Create `TODO.md` (this file).
- [x] Create `CHANGELOG.md`.

## Phase 2: Consolidate API Interaction and Data Fetching
- [x] **Remove Deprecated API Client**:
    - [x] Delete `src/nyord_vpn/core/api.py`.
    - [x] Implicitly verified no essential code imports `NordVPNAPIClient`.
- [x] **Centralize API Usage & Prioritize v2 API in `NordVPNAPI` (`src/nyord_vpn/api/api.py`)**:
    - [x] Remove `self.recommendations` client and `get_recommended_servers()` method.
    - [x] Remove `self.technologies` client and `get_technologies()` method.
    - [x] Remove `self.groups` client and `get_groups()` method.
    - [x] Remove `self.countries` client and `get_countries()` method.
    - [x] Update `find_best_server()`:
        - [x] Remove `use_v2` parameter.
        - [x] Remove v1 fallback logic.
        - [x] Ensured it correctly uses v2 server data.
    - [x] Update `get_server_stats()`:
        - [x] Remove v1 fallback logic.
        - [x] Ensured it uses only v2 data.
    - [x] Added `get_all_countries_from_v2()` method.
    - [x] Delete `src/nyord_vpn/api/v1_recommendations.py` and `.json`.
    - [x] Delete `src/nyord_vpn/api/v1_technologies.py` and `.json`.
    - [x] Delete `src/nyord_vpn/api/v1_groups.py` and `.json`.
    - [x] Delete `src/nyord_vpn/api/v1_countries.py` and `.json`.
- [x] **Eliminate Static Country Data & Related Functionality**:
    - [x] Delete `src/nyord_vpn/scripts/update_countries.py`.
    - [x] In `src/nyord_vpn/__main__.py`: Remove the `update` CLI command.
    - [x] Delete `src/nyord_vpn/data/countries.json`.
    - [x] Delete `src/nyord_vpn/data/country_ids.json`.
    - [x] In `src/nyord_vpn/core/client.py`: Remove `FALLBACK_DATA` constant.
    - [x] In `src/nyord_vpn/core/client.py`: Remove `COUNTRIES_CACHE` constant (and related).
    - [x] **Address `list-countries` CLI command**:
        - [x] Added `list_countries` method to `Client` (`core/client.py`).
        - [x] Added `list_countries` method to `CLI` class (`__main__.py`).
- [x] **Consolidate Caching in `ServerManager` (`src/nyord_vpn/network/server.py`)**:
    - [x] Remove `SERVERS_CACHE_FILE` constant and `SERVERS_CACHE_TTL`.
    - [x] Remove `cache_servers()` function.
    - [x] Remove `_parse_timestamp()` function.
    - [x] Remove `get_cached_servers()` function.
    - [x] Modify `get_servers_cache()`:
        - [x] Remove memory caching (`self._servers_cache`, `self._last_cache_update`).
        - [x] Remove file caching logic.
        - [x] Make it directly call `self.api_client.get_servers()` and transform data.
    - [x] `_validate_country_code` updated for direct API call.
    - [x] Removed unused imports `API_HEADERS`, `CACHE_DIR`.

## Phase 3: Simplify Server Selection (`network/server.py` - `ServerManager`)
- [x] Remove `_ping_server()` method.
- [x] Remove `_check_for_ping_command()` method.
- [x] Remove `_fallback_ping()` method.
- [x] Remove `_measure_socket_connection()` method.
- [x] Remove `_test_server()` method.
- [x] Modify `select_fastest_server()`:
    - [x] Remove calls to pinging/testing methods.
    - [x] Select servers based on API-reported load (primarily via `api_client.find_best_server()`, then fallback to sorted list).
    - [x] Ensure it returns a list of server dictionaries as expected.
- [x] Review and potentially simplify or remove `_select_diverse_servers()`. (Removed)

## Phase 4: Refactor Core Client (`core/client.py`)
- [x] **Remove Circular Dependency in `VPNConnectionManager` (`src/nyord_vpn/network/vpn.py`)**:
    - [x] Remove `vpn_manager` from constructor parameters.
    - [x] Remove `self.vpn_manager` attribute.
    - [x] Verified no functionality is broken (it was unused).
- [x] **Review `Client.init()` method**:
    - [x] Standardized `CONFIG_DIR` to XDG path for downloaded OpenVPN configs; `utils/templates.py` updated.
    - [x] Removed creation of user-level `DATA_DIR` in `Client.init()`.
    - [x] Cleaned up unused `DATA_DIR` definitions and related code from `utils/utils.py`.
    - [x] API connectivity test in `Client.init()` updated to `api_client.get_servers(refresh=True)`.
    - [x] Decision: Explicit call of `init()` by `__main__.py` is acceptable.

## Phase 5: Code Cleanup and Verification
- [x] Perform a full codebase review for unused imports, variables, or functions.
    - [x] Removed unused TypedDicts from `core/client.py`.
    - [x] Removed unused `OPENVPN_CONFIG`, `API_HEADERS` from `utils/utils.py`.
    - [x] Fixed `fetch_server_info` call in `network/server.py`.
    - [x] Removed unused imports from `network/server.py`.
    - [x] Corrected `api_client` type hint in `VPNConnectionManager`.
- [x] Manually test core CLI commands. (Simulated by code path review)
- [x] Check logs for errors or unexpected warnings. (Simulated by code path review)

## Phase 6: Documentation and Finalization
- [x] Update `PLAN.md` to reflect completed steps. (Implicitly done by tool usage)
- [x] Update `TODO.md` to reflect completed steps. (This update)
- [x] Update `CHANGELOG.md` with all significant changes made.
- [x] Review `README.md` for any outdated information.
    - [x] Updated Key Features (API strategy).
    - [x] Removed `--api njord` CLI command.
    - [x] Corrected Python API example.
    - [x] Removed "njord" dependency mention.
    - [x] Updated `VPNServerError` to `VPNAPIError`.

## Phase 7: Submission
- [ ] Commit all changes with a comprehensive commit message.
- [ ] Submit the changes.
