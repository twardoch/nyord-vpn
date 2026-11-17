# nyord-vpn: NordVPN for macOS, one command

`nyord-vpn go JP` and your Mac is in Japan. That's the whole idea.

`nyord-vpn` is a Python CLI and library that connects macOS to NordVPN over OpenVPN. It fetches the live server list from NordVPN's v2 API, picks the least-loaded server in your target country, manages the `openvpn` subprocess, verifies the new IP, and cleans up after itself.

## Visual

![A laptop slipping through the globe to Mount Fuji, drawn in one line](docs/assets/icon.png)

## Quick start

```bash
pip install nyord-vpn
brew install openvpn                     # the client shells out to it

export NORD_USER="your@email.com"        # NordVPN service credentials
export NORD_PASSWORD="your_password"

nyord-vpn go JP                          # connect to Japan
nyord-vpn info                           # current IP, server, country
nyord-vpn bye                            # disconnect
```

Connecting needs admin rights — macOS asks for your **system** password (not your NordVPN one) because OpenVPN reconfigures network interfaces.

## Requirements

- macOS
- OpenVPN — `brew install openvpn`
- Python 3.10+
- A NordVPN account (use the *service* credentials from "Manual setup", not your dashboard login)

## CLI

```bash
nyord-vpn go JP            # connect to Japan
nyord-vpn go DE --verbose  # connect to Germany, show every step
nyord-vpn go US --dry-run  # pick a server and print it — connect to nothing (no root needed)
nyord-vpn info             # show current IP, server, country
nyord-vpn list-countries   # list available country codes
nyord-vpn bye              # disconnect
```

`--dry-run` is the fast way to check that server selection and the API work before you involve `sudo` and OpenVPN.

## Python API

```python
import os
from nyord_vpn import Client, VPNError

client = Client(
    username_str=os.environ["NORD_USER"],
    password_str=os.environ["NORD_PASSWORD"],
)

client.go("NL")  # connect to the Netherlands
status = client.status()  # {"connected": True, "ip": "...", "server": "..."}
print(f"Connected via {status['server']} — IP {status['ip']}")
client.bye()  # disconnect
```

Scripts that actually connect need to run with `sudo -E` so root inherits your credentials.

## How it works

```
nyord-vpn go US
  ├── NordVPNAPI          fetches the server list from api.nordvpn.com/v2
  ├── ServerManager       filters OpenVPN TCP servers in the country, picks lowest load
  ├── VPNConnectionManager
  │     ├── writes a temporary auth file, chmod 600, before writing the password
  │     ├── resolves the bundled .ovpn config for the server
  │     ├── spawns the openvpn subprocess (via sudo)
  │     └── polls until the IP changes, then verifies it against a public IP echo
  └── saves ephemeral state to ~/Library/Caches/nyord-vpn/state.json
```

**Server selection:** lowest `load` (a 0–100 percentage from the API) wins. If the API is unreachable after a successful call, the client reuses its in-memory server cache for the rest of the session.

**Security:** the auth file holding your password is chmod `600` and lives in the OS cache directory, never in config or the repo. See [Security notes](https://twardoch.github.io/nyord-vpn/security).

## Package structure

| Path | Purpose |
|------|---------|
| `core/client.py` | `Client` — the high-level entry point that coordinates everything |
| `api/api.py` | NordVPN v2 API client with per-instance caching |
| `api/v2_servers.py` | Typed models and fetch for the v2 servers endpoint |
| `network/server.py` | Server discovery, validation, and load-based selection |
| `network/vpn.py` | OpenVPN subprocess lifecycle and IP verification |
| `storage/state.py` | Persist and restore connection state |
| `utils/templates.py` | Locate and cache the bundled `.ovpn` config files |
| `exceptions.py` | `VPNError`, `VPNConnectionError`, `VPNAPIError`, and friends |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `NORD_USER` (or `NORDVPN_LOGIN`) | NordVPN service username |
| `NORD_PASSWORD` (or `NORDVPN_PASSWORD`) | NordVPN service password |

## Troubleshooting

When OpenVPN won't start or the `sudo` prompt confuses you, see the [troubleshooting guide](https://twardoch.github.io/nyord-vpn/troubleshooting). The short version: check `which openvpn`, run with `--verbose`, and read `~/Library/Caches/nyord-vpn/openvpn.log`.

## Contributing

```bash
uvx hatch run test:default        # run tests
uvx hatch run quality:fix         # ruff check --fix + format
uvx hatch run quality:typecheck   # mypy
```

Follow [Conventional Commits](https://www.conventionalcommits.org/).

## License

MIT. See `LICENSE`.
