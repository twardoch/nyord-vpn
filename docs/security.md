---
title: Security notes
layout: default
nav_order: 2
---

# Security notes

A VPN tool handles your password and rewrites your network. Here is exactly what `nyord-vpn` touches, so nothing about it has to be a matter of trust.

## The temporary auth file

OpenVPN cannot read your credentials from an environment variable. It wants a file. So before each connection `nyord-vpn` writes your username and password to:

```
~/Library/Caches/nyord-vpn/openvpn.auth
```

Three things about that file:

- **It is chmod `600`** — readable and writable by your user only, no group, no world. The client sets those permissions the moment it creates the file, before it writes a single byte of your password.
- **It lives in the OS cache directory**, resolved through `platformdirs`, not in a config directory and not in the repo. Cache is the honest home for a throwaway secret.
- **It holds the password in plain text** for as long as the OpenVPN process runs. That is a constraint OpenVPN imposes, not a choice the client makes. When you run `nyord-vpn bye`, the process ends; the file remains until the next connection overwrites it.

If you want the file gone the instant you disconnect, delete it yourself — nothing reads it between sessions.

## Credentials in your environment

`nyord-vpn` reads `NORD_USER` and `NORD_PASSWORD` from the environment. Anything you `export` is visible to other processes you run and may land in your shell history. Prefer a file your shell sources with `600` permissions over typing the `export` line at an interactive prompt.

## What runs as root

Only OpenVPN. The client escalates with `sudo` solely to launch the `openvpn` subprocess, because configuring a network interface requires it. Server selection, API calls, and state files all run as your normal user.

## State on disk

Connection state — current IP, server hostname, country, a timestamp — is written to `~/Library/Caches/nyord-vpn/state.json`. It is ephemeral status, not configuration, and it never contains your password.
