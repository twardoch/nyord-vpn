---
title: Home
layout: default
nav_order: 1
---

# nyord-vpn

One command puts your Mac in another country. `nyord-vpn go JP` — that's all.

`nyord-vpn` is a Python CLI and library that connects macOS to NordVPN over OpenVPN. It pulls the live server list from NordVPN's v2 API, picks the least-loaded server in the country you asked for, launches the `openvpn` subprocess, and confirms the new IP before it hands back the prompt.

## Install

```bash
pip install nyord-vpn
brew install openvpn   # the client shells out to it
```

## Set credentials

```bash
export NORD_USER="your@email.com"
export NORD_PASSWORD="your_nordvpn_password"
```

Put those in `~/.zshrc` to persist them.

## Connect

```bash
nyord-vpn go JP            # connect to Japan
nyord-vpn go DE --verbose  # connect to Germany, show what happens
nyord-vpn go US --dry-run  # pick a server and print it — connect to nothing
nyord-vpn info             # current IP, server, country
nyord-vpn list-countries   # available country codes
nyord-vpn bye              # disconnect
```

Connecting needs admin rights — macOS asks for your system password because OpenVPN reconfigures network interfaces.

## Read next

- [Security notes](security) — what the temporary auth file holds and how long it lives.
- [Troubleshooting](troubleshooting) — when OpenVPN refuses to start.

## License

MIT.
