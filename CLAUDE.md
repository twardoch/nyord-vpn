# CLAUDE.md

Guidance for AI agents (and humans) working in this repository.

## What this is

`nyord-vpn` is a **macOS-only** Python CLI and library that connects to NordVPN over OpenVPN. It targets the NordVPN **v2 API only** — all v1/legacy code paths were removed. Do not reintroduce them.

## Golden rules

- **Never touch a real VPN, network, or credential in tests.** Every `requests` call, subprocess, and OpenVPN interaction must be mocked. The suite runs fully offline in ~1s.
- **macOS-only.** It shells out to `openvpn` and `sudo`, and resolves paths with `platformdirs` (cache lands in `~/Library/Caches/nyord-vpn`, not `~/.cache`). Do not hardcode `~/.cache`.
- **Version comes from git tags** via `hatch-vcs` (written to `src/nyord_vpn/__version__.py`, which is gitignored). Never edit the version by hand.
- **The floor for Python is 3.10.** `typing.NotRequired` does not exist there — import it from `typing_extensions`.

## Layout (src/ layout, `this_file:` headers in each module)

- `core/client.py` — `Client`, the high-level coordinator used by CLI and library callers.
- `__main__.py` — the `fire`-based CLI (`go`, `bye`, `info`, `list_countries`).
- `api/api.py` — `NordVPNAPI`: `get_servers`, `find_best_server` (min load wins), `get_server_stats`, `get_all_countries_from_v2`.
- `api/v2_servers.py` — pydantic models and `fetch_all()` for the v2 endpoint. Servers carry `*_ids` int lists that `_link_server_relations` resolves into objects.
- `network/server.py` — `ServerManager`: validation, transform to the internal `ServerInfo` shape, load-based selection.
- `network/vpn.py` — `VPNConnectionManager`: OpenVPN subprocess lifecycle, IP verification, state.
- `storage/state.py` + `utils/utils.py` — ephemeral connection state under the cache dir; path constants.
- `storage/models.py` — TypedDicts plus a *separate* exception hierarchy (`ServerError`, `VPNError`) used by `network/server.py`. The richer hierarchy in `exceptions.py` (`VPNError`, `VPNAPIError`, `VPNConnectionError`, ...) is what the rest of the package raises.
- `utils/templates.py` — downloads and caches the bundled `.ovpn` config archive.

## Working on it

```bash
uvx hatch run test:default        # tests (mocked, offline)
uvx hatch run test:cov            # tests + coverage gate
uvx hatch run quality:fix         # ruff check --fix + format
uvx hatch run quality:typecheck   # mypy (src only; tests are exercised by pytest)
```

Ruff runs a broad rule set with a documented pragmatic ignore list in `pyproject.toml` for this legacy CLI (subprocess/complexity/error-chaining opinions). mypy is scoped to `src/nyord_vpn` and the package ships a `py.typed` marker.

## Credentials

Read from `NORD_USER`/`NORDVPN_LOGIN` and `NORD_PASSWORD`/`NORDVPN_PASSWORD`. `NordVPNAPI` holds no credentials — `VPNConnectionManager` captures them in `setup_connection` and reuses them across fallback servers.
