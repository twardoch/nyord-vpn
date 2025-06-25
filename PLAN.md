1.  **Understand Project Structure and Entry Points (Done)**
    *   Reviewed `README.md`, `__main__.py`, `core/client.py`, `api/api.py`, `core/api.py` (deprecated), `network/vpn.py`.
    *   Reviewed `network/server.py`, `storage/state.py`, `scripts/update_countries.py`, `api/v1_countries.py`, `api/v2_servers.py`.

2.  **Consolidate API Interaction and Data Fetching:**
    *   **Remove Deprecated API Client**: Delete `src/nyord_vpn/core/api.py`. Confirm no essential code uses it.
    *   **Centralize API Usage**: Ensure all API calls go through `NordVPNAPI` in `src/nyord_vpn/api/api.py`.
    *   **Prioritize v2 API**:
        *   In `NordVPNAPI` (`src/nyord_vpn/api/api.py`), remove initializations and methods related to v1 endpoints (`v1_recommendations`, `v1_technologies`, `v1_groups`, `v1_countries` clients and their wrapper methods like `get_recommended_servers`, `get_technologies`, `get_groups`, `get_countries`).
        *   Ensure `find_best_server` relies solely on v2 data or a simplified v2-only approach. The fallback to v1 within it should be removed.
        *   This will likely lead to deleting the `src/nyord_vpn/api/v1_*.py` files (except potentially `v1_countries.py` if `update_countries.py` is kept temporarily, but the goal is to remove that too).
    *   **Eliminate Static Country Data**:
        *   Remove `src/nyord_vpn/scripts/update_countries.py`.
        *   Remove the `update` command from `src/nyord_vpn/__main__.py`.
        *   Remove `src/nyord_vpn/data/countries.json` and `src/nyord_vpn/data/country_ids.json`.
        *   Remove `FALLBACK_DATA` from `src/nyord_vpn/core/client.py`.
        *   The `list-countries` CLI command will need to be updated to fetch country information from the v2 server data via `NordVPNAPI` or be removed if out of MVP scope.
    *   **Consolidate Caching**:
        *   Review caching in `NordVPNAPI` (`api/api.py`) and `ServerManager` (`network/server.py`).
        *   Aim to have `NordVPNAPI` manage its own caching effectively.
        *   Modify `ServerManager` to rely on `NordVPNAPI` for fresh data and its caching, removing `ServerManager`'s own `servers.json` cache (`SERVERS_CACHE_FILE`, `cache_servers`, `get_cached_servers`). `ServerManager` would always ask `NordVPNAPI` for server lists.

3.  **Simplify Server Selection (`network/server.py` - `ServerManager`):**
    *   For MVP, remove the active pinging logic (`_ping_server`, `_fallback_ping`, `_test_server`).
    *   Modify `select_fastest_server` to select servers based on API-reported load or other available v2 API metrics, or even random selection from suitable servers.
    *   This may also simplify or remove `_select_diverse_servers`.
    *   The goal is to connect to a working server in the chosen country without complex local testing.

4.  **Refactor Core Client (`core/client.py`):**
    *   **Remove Circular Dependency**: Remove the `vpn_manager` parameter and attribute from `VPNConnectionManager` (`src/nyord_vpn/network/vpn.py`) as it appears unused. Verify this thoroughly.
    *   **Review `init()` method**: Decide if its functionality (creating dirs, API test, initial IP) should be part of `Client.__init__` or explicitly called by the CLI. For now, explicit call by CLI is acceptable.

5.  **Code Cleanup and Verification:**
    *   After major changes, run static analysis (if available) and manually review for broken imports or logic.
    *   Test core functionality: connect to a specific country, check status, disconnect.

6.  **Documentation and Output Files:**
    *   Create `PLAN.md` with these detailed steps (this is the plan itself).
    *   Create `TODO.md` with a checklist version of this plan.
    *   Create `CHANGELOG.md` and update it as changes are made.
    *   Update `PLAN.md` and `TODO.md` to reflect progress.

7.  **Submission:**
    *   Commit changes with a descriptive message.
    *   Submit.
