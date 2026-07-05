# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### 2026-07 — Modernization pass

#### Fixed (real bugs surfaced by the v2 refactor)
- `network/server.py`: repaired `_validate_country_code`, whose verification block was mis-indented after a `raise` (dead code) and used the wrong `get_servers(refresh_cache=...)` kwarg — valid country codes were never actually verified. Restored the missing `cast`, `secrets`, and `VPNAPIError` imports that a prior cleanup had wrongly removed while the code still used them.
- `core/client.py`: `list_countries` caught `VPNAPIError` without importing it (a `NameError` waiting to fire).
- `network/vpn.py`: `status()` called a removed `api_client.get_country_by_code` (silently swallowed); now resolves country names from the v2 country list. `go()` referenced non-existent `api_client.username`/`.password`; credentials are now captured in `setup_connection` and reused. Removed a redundant `OPENVPN_AUTH`/`OPENVPN_LOG` redefinition that forced `~/.cache` instead of the platformdirs cache path.
- `utils/templates.py`: `download_config_zip` used an unimported `CACHE_DIR` (`NameError`); added the import and guarded `HTTPError.response` access.
- Python 3.10 compatibility: import `NotRequired` from `typing_extensions` (it is not in `typing` before 3.11) so the package imports on the supported floor.
- Deleted dead, import-broken modules `core/base.py` and `network/country.py`, and the stray `src/__init__.py` that broke src-layout module resolution.

#### Added
- `go --dry-run`: select and print the target server without connecting (needs no root); exposed on both `Client.go` and the CLI.
- `py.typed` marker (PEP 561) so downstream type checkers see the package's types.
- Jekyll docs site under `docs/` (Just the Docs): home, Security notes, Troubleshooting.
- `CLAUDE.md` with architecture notes and `this_file:` map.
- Full mocked test suite covering the current v2 surface; obsolete v1/legacy test modules removed. Every test runs offline — no real VPN, network, or credentials.
- Explanatory comments for load-based server selection, IP verification, and cache-dir state placement.

#### Changed
- CI: `push.yml` → `ci.yml` with an added mypy type-check job; `release.yml` pinned to `softprops/action-gh-release@v2`.
- `pyproject.toml`: mypy scoped to `src/` with `ignore_missing_imports` and pragmatic strictness for this legacy CLI; ruff given a documented ignore list so `ruff check` is clean without rewriting working subprocess logic.
- Replaced the bloated Visual Studio `.gitignore` with a focused Python/macOS one.

### Added
- `PLAN.md`: Detailed plan for codebase streamlining.
- `TODO.md`: Checklist for implementing the streamlining plan.
- `CHANGELOG.md`: This file, to track changes.
- Added `list_countries` method to `Client` and `CLI` to list countries using v2 API data.

### Changed
- **API Layer (`src/nyord_vpn/api/api.py` - `NordVPNAPI`):**
    - Focused `NordVPNAPI` on v2 NordVPN API.
    - Removed internal clients and wrapper methods for v1 API endpoints (recommendations, technologies, groups, countries).
    - `find_best_server` now exclusively uses v2 data; removed v1 fallback and `use_v2` parameter.
    - `get_server_stats` now exclusively uses v2 data; removed v1 fallback.
    - Added `get_all_countries_from_v2` method.
- **Server Data Handling (`src/nyord_vpn/network/server.py` - `ServerManager`):**
    - Removed its own file-based caching (`servers.json`) and memory caching for server data.
    - `ServerManager.get_servers_cache()` now directly fetches data from `NordVPNAPI.get_servers()` (which has its own instance-level cache) and transforms it into the previously expected `ServerCache` format.
    - `_validate_country_code` now relies solely on data from `NordVPNAPI.get_servers()`.
- **CLI (`src/nyord_vpn/__main__.py`):**
    - Removed the `update` command (related to static country data).
    - Added `list_countries` command.

### Removed
- **Deprecated API Client:**
    - Deleted `src/nyord_vpn/core/api.py` (contained `NordVPNAPIClient`).
- **V1 API Modules:**
    - Deleted `src/nyord_vpn/api/v1_recommendations.py` and `.json`.
    - Deleted `src/nyord_vpn/api/v1_technologies.py` and `.json`.
    - Deleted `src/nyord_vpn/api/v1_groups.py` and `.json`.
    - Deleted `src/nyord_vpn/api/v1_countries.py` and `.json`.
- **Static Country Data & Script:**
    - Deleted `src/nyord_vpn/scripts/update_countries.py`.
    - Deleted `src/nyord_vpn/data/countries.json`.
    - Deleted `src/nyord_vpn/data/country_ids.json`.
- **Constants related to static data in `core/client.py`:**
    - Removed `FALLBACK_DATA`.
    - Removed `COUNTRIES_CACHE`, `CACHE_FILE`, `CACHE_EXPIRY`.
- Unused imports `API_HEADERS`, `CACHE_DIR` from `src/nyord_vpn/network/server.py`.
- **Server Selection Logic (`src/nyord_vpn/network/server.py` - `ServerManager`):**
    - Removed active server pinging logic (`_ping_server`, `_fallback_ping`, etc.) and related helper methods (`_check_for_ping_command`, `_measure_socket_connection`, `_test_server`).
    - Removed `_select_diverse_servers()` method as it was tied to server testing.
    - `select_fastest_server()` now relies on API-reported server load and filtering, not active pinging. It first tries `api_client.find_best_server()` for an optimal single server, then falls back to filtering and sorting the broader list from `get_servers_cache()`.
- **Core Client & Utilities (`core/client.py`, `utils/utils.py`, `utils/templates.py`):**
    - Removed circular dependency: `VPNConnectionManager` no longer takes `Client` instance as `vpn_manager` argument.
    - Standardized `CONFIG_DIR` usage: OpenVPN configuration files and the `ovpn.zip` are now stored in the user's standard config directory (e.g., `~/.config/nyord-vpn/`) instead of a cache subdirectory.
    - `Client.init()` no longer creates the user-level `DATA_DIR` as its main purpose (static country files) was removed.
    - API connectivity test in `Client.init()` updated to use `api_client.get_servers(refresh=True)`.
- Cleaned up unused `DATA_DIR`-related variables and functions from `utils/utils.py`.

### Fixed
- Corrected type hint for `api_client` in `VPNConnectionManager` constructor to `NordVPNAPI`.
- Removed unused imports (`os`, `platform`, `random`, `secrets`, `socket`, `subprocess`, `cast`, `requests`) from `src/nyord_vpn/network/server.py`.
- Removed unused `OPENVPN_CONFIG` and `API_HEADERS` constants from `src/nyord_vpn/utils/utils.py`.
- Removed unused `City`, `Country`, `CountryCache` TypedDicts from `src/nyord_vpn/core/client.py`.
- Corrected `fetch_server_info` in `network/server.py` to call `find_best_server` without the removed `use_v2` parameter.
- **Documentation (`README.md`):**
    - Updated "Key Features" to reflect current API strategy (v2 focused, no "njord").
    - Removed non-existent `--api njord` CLI command.
    - Corrected Python API usage example (direct Client instantiation, current methods).
    - Removed mention of optional "njord" dependency installation.
    - Updated error type from `VPNServerError` to `VPNAPIError`.
