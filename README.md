# nyord-vpn

nyord-vpn is a simple NordVPN client for macOS users. It provides an easy way to manage VPN connections. 

nyord-vpn is primarily designed for macOS, as it relies on OpenVPN, which is easily installable via Homebrew. However, with some modifications, it might be possible to use it on other platforms like Linux or Windows. Contributions to support additional platforms are welcome.

## Key Features

- **Simple and Reliable Connection Management:** Connect and disconnect from VPN with minimal hassle.
- **Support for Legacy OpenVPN and njord APIs:** Choose between different API versions for flexibility.
- **Country Selection:** Connect to servers in specific countries easily.
- **Status Monitoring:** Check the current status of your VPN connection.
- **Clear Error Messages:** Resolve issues quickly with informative error messages.
- **Minimal Dependencies:** Lightweight and easy to set up.

## Installation

To use nyord-vpn, you need to install some system requirements and the package itself.

### System Requirements

- macOS operating system
- OpenVPN installed

### Installing OpenVPN

Install OpenVPN using Homebrew:

```bash
brew install openvpn
```

### Installing nyord-vpn

Install the package using pip:

```bash
pip install nyord-vpn
```


## Configuration

Before using nyord-vpn, set your NordVPN credentials as environment variables:

```bash
export NORD_USER="your-username"
export NORD_PASSWORD="your-password"
```

Replace `"your-username"` and `"your-password"` with your actual NordVPN credentials.

## Usage

nyord-vpn can be used via the command line interface (CLI) or programmatically through its Python API.

### API Options

### CLI Commands

Here are the available CLI commands:

- **`nyord-vpn connect`**: Connects to a NordVPN server. Defaults to a server in the United States.
- **`nyord-vpn connect --country <country>`**: Connects to a server in the specified country. Replace `<country>` with the country name or code (e.g., `netherlands`).
- **`nyord-vpn --api njord connect`**: Uses the njord API to connect to the VPN.
- **`nyord-vpn --verbose connect`**: Connects to the VPN with verbose logging enabled for debugging.
- **`nyord-vpn status`**: Displays the current status of the VPN connection, including connection status, server, and IP address.
- **`nyord-vpn list-countries`**: Lists all available countries with NordVPN servers.
- **`nyord-vpn disconnect`**: Disconnects from the VPN.

**Note:** Some commands, such as connecting and disconnecting, may require sudo privileges. You might be prompted to enter your password.

### Python API

You can use nyord-vpn programmatically in Python:

```python
from nyord_vpn.core.factory import create_client

# Create a client (choose "legacy" or "njord")
client = create_client("legacy")

# Connect to VPN in a specific country
client.connect("netherlands")

# Check connection status
status = client.status()
print(f"Connected to {status['server']} ({status['ip']})")

# Disconnect from VPN
client.disconnect()
```

Ensure you have the necessary permissions to run OpenVPN when using the Python API.

## Development

To contribute to nyord-vpn or modify the code:

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Install optional njord support:**

   ```bash
   pip install njord
   ```

3. **Run with debug logging:**

   ```bash
   NORD_USER="username" NORD_PASSWORD="password" nyord-vpn --verbose connect
   ```

For a full development setup, clone the repository, create a virtual environment, and install the package in editable mode:

```bash
git clone https://github.com/yourusername/nyord-vpn.git
cd nyord-vpn
python -m venv venv
source venv/bin/activate
pip install -e .
```

Replace `yourusername` with the actual repository owner.

## Error Handling and Troubleshooting

nyord-vpn provides clear error messages to help resolve issues. Common errors include:

- **`VPNCredentialsError`**: Missing or invalid credentials. Ensure `NORD_USER` and `NORD_PASSWORD` are set correctly.
- **`VPNConnectionError`**: Failed to connect or disconnect. Check your internet connection and try again.
- **`VPNConfigError`**: Configuration issues, such as missing OpenVPN. Install OpenVPN if not already installed.
- **`VPNServerError`**: Failed to get server information. Try again later or check your network connection.

### Troubleshooting Tips

- **"OpenVPN not found" error:** Install OpenVPN using `brew install openvpn`.
- **"Authentication failed" error:** Verify your NordVPN credentials in the environment variables.
- **"Failed to connect" error:** Check your internet connection or try a different country/server.
- **"No servers available" error:** Wait a few minutes and try again; this may be a temporary API issue.

### Security Considerations

- **Keep Credentials Secure:** Do not hardcode credentials; use environment variables or secure storage.
- **Update Regularly:** Keep nyord-vpn and dependencies up to date for security patches.
- **Monitor Connections:** Regularly check your connection status.
- **Use Strong Passwords:** Ensure your NordVPN account has a strong, unique password.

## Contributing

We welcome contributions to nyord-vpn! To contribute:

1. Fork the repository.
2. Create a feature branch for your changes.
3. Make your changes and commit them.
4. Submit a pull request with a clear description of your changes.

For issues or questions, open an issue on the [GitHub repository](https://github.com/yourusername/nyord-vpn).

## License

nyord-vpn is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
