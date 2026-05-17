#!/usr/bin/env bash
# install.sh: Install nyord-vpn in editable mode
# nyord-vpn: NordVPN client with API fallback support

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Installing nyord-vpn (editable) ==="
uv pip install -e .
echo "=== Install complete ==="
