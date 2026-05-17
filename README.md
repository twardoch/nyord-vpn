# nyord-vpn: NordVPN client for macOS

`nyord-vpn` is a Python command-line tool and library that connects macOS to NordVPN via OpenVPN. It fetches server lists from NordVPN's API, picks the least-loaded server for your target country, and manages the OpenVPN subprocess — including connection verification and cleanup.

## Requirements

- macOS
- OpenVPN (`brew install openvpn`)
- Python 3.9+
- Root/sudo access (OpenVPN needs it)
- A NordVPN account

## Installation

```bash
pip install nyord-vpn
```

## Setup

```bash
export NORD_USER="your@email.com"
export NORD_PASSWORD="your_nordvpn_password"
```

Add to `~/.zshrc` or `~/.bash_profile` to persist.

## Usage

### CLI

```bash
nyord-vpn go JP          # connect to Japan
nyord-vpn go DE --verbose  # connect to Germany with debug output
nyord-vpn info           # show current IP, server, country
nyord-vpn list-countries # show available country codes
nyord-vpn bye            # disconnect
```

VPN commands require admin rights — you'll be prompted for your system password.

### Python API

```python
import os
from nyord_vpn import Client, VPNError

client = Client(username_str=os.environ["NORD_USER"],
                password_str=os.environ["NORD_PASSWORD"])

client.go("NL")                        # connect to Netherlands
status = client.status()               # {"connected": True, "ip": "...", "server": "..."}
print(f"Connected via {status['server']} — IP {status['ip']}")
client.bye()                           # disconnect
```

Scripts calling the API directly may need `sudo`.

## How it works

```
nyord-vpn go US
  ├── NordVPNAPI          fetches server list from api.nordvpn.com/v2
  ├── ServerManager       picks the lowest-load US OpenVPN server
  ├── VPNConnectionManager
  │     ├── writes a temporary auth file (chmod 600)
  │     ├── resolves the bundled .ovpn config template
  │     ├── spawns openvpn subprocess
  │     └── polls until IP changes, then verifies new IP via ipinfo.io
  └── saves state to ~/.cache/nyord-vpn/vpn_state.json
```

**Encryption:** AES-256-GCM with ChaCha20-Poly1305 support. Certificate validation and DNS leak prevention are on by default.

**Server selection:** filters for OpenVPN TCP servers in the target country, sorts by load, picks the lightest.

**Fallback:** if the NordVPN API is unreachable, the client falls back to a local server cache.

## Package structure

| Path | Purpose |
|------|---------|
| `core/client.py` | Main `Client` class — coordinates everything |
| `api/api.py` | NordVPN v2 API client with caching |
| `network/server.py` | Server discovery and load-based selection |
| `network/vpn.py` | OpenVPN subprocess lifecycle |
| `network/country.py` | Country code normalisation |
| `storage/state.py` | Persist/restore connection state |
| `utils/connection.py` | IP address checking |
| `utils/templates.py` | Locate bundled `.ovpn` config files |
| `exceptions.py` | `VPNError`, `VPNConnectionError`, `ServerError`, `CredentialsError` |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `NORD_USER` | NordVPN username / email |
| `NORD_PASSWORD` | NordVPN password |

## Contributing

- Format: `black .`
- Lint: `ruff check .`
- Tests: `pytest tests/`
- Follow [Conventional Commits](https://www.conventionalcommits.org/)

## License

MIT. See `LICENSE`.
