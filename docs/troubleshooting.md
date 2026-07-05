---
title: Troubleshooting
layout: default
nav_order: 3
---

# Troubleshooting

Most failures come from three places: OpenVPN, `sudo`, or credentials. Here is how to tell which one you hit.

## "OpenVPN fails to start"

The client shells out to the `openvpn` binary. If it is missing or not on your `PATH`, connection dies immediately.

```bash
which openvpn        # should print a path
brew install openvpn # if it prints nothing
```

If `openvpn` exists but the process still exits, run with `--verbose` and read the log it writes to `~/Library/Caches/nyord-vpn/openvpn.log`. The usual culprits:

- **Config not found** — the bundled `.ovpn` for that server could not be resolved. Try a different country; the server may have rotated out of the config bundle.
- **Auth failure** — your `NORD_USER` / `NORD_PASSWORD` are wrong, or you used your NordVPN *account* password instead of your *service* credentials. Check them in the Nord dashboard under "Manual setup".
- **TLS handshake timeout** — the chosen server is overloaded or unreachable. Reconnect; `nyord-vpn` picks the least-loaded server each time.

## The sudo prompt is confusing

VPN commands need root because OpenVPN reconfigures network interfaces. When you run `nyord-vpn go ...`, macOS prompts for your **computer** admin password — not your NordVPN password. If the prompt scrolls past in a busy terminal, run the command on its own:

```bash
sudo -E nyord-vpn go JP
```

The `-E` preserves your `NORD_USER` / `NORD_PASSWORD` environment across the escalation. Without it, root has no credentials and the connection fails.

## Nothing connects and you want to see why

```bash
nyord-vpn go US --dry-run   # select a server, print it, connect to nothing
```

Dry-run needs no root. If it prints a hostname, server selection and the API work — your problem is downstream in OpenVPN or `sudo`. If it errors, the API or your country code is the issue; check `nyord-vpn list-countries`.

## Still stuck

Open an issue at [github.com/twardoch/nyord-vpn/issues](https://github.com/twardoch/nyord-vpn/issues) with the `--verbose` output and the tail of `openvpn.log`.
