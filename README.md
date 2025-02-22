# nyord-vpn

A modern Python client for NordVPN with automatic API fallback support, providing both a CLI interface and a Python library.

```bash
# Install system requirements first
brew install openvpn  # macOS
sudo apt install openvpn  # Ubuntu/Debian
sudo dnf install openvpn  # Fedora/RHEL

# Then install and use the package
pip install nyord-vpn
export NORD_USER="username" NORD_PASSWORD="password"
nyord-vpn connect de  # Connect to a German VPN
nyord-vpn status  # Check status
nyord-vpn disconnect  # Disconnect
```


## Features

- Modern async Python client with type hints and runtime type checking
- Automatic fallback between modern and legacy APIs for maximum reliability
- Rich CLI interface with progress indicators and colorful output
- Secure credential management with environment variables or config files
- Comprehensive error handling and logging
- PEP 621 compliant packaging
- Full test coverage and documentation

## Installation

```bash
pip install nyord-vpn
```

## CLI Usage

The package provides a rich command-line interface with the following commands:

```bash
# Connect to VPN (defaults to US)
nyord-vpn connect

# Connect to specific country
nyord-vpn connect --country "Netherlands"

# Check connection status
nyord-vpn status

# List available countries
nyord-vpn list-countries

# Disconnect from VPN
nyord-vpn disconnect
```

### CLI Configuration

You can configure the CLI in several ways:

1. Environment variables:
```bash
# These environment variables are compatible with njord
export NORD_USER="your-username"
export NORD_PASSWORD="your-password"

# Additional configuration (optional)
export NORDVPN_DEFAULT_COUNTRY="Netherlands"
export NORDVPN_USE_LEGACY_FALLBACK=true
```

> **Note**: The `NORD_USER` and `NORD_PASSWORD` environment variables are compatible with the njord package. If you're using both packages, you only need to set these credentials once.

2. Command line arguments:
```bash
nyord-vpn --username "your-username" --password "your-password" connect
```

3. Configuration file:
```bash
# Create config file at ~/.config/nyord-vpn/config.json
{
  "username": "your-username",
  "password": "your-password",
  "default_country": "Netherlands",
  "retry_attempts": 3,
  "use_legacy_fallback": true
}

# Use config file
nyord-vpn --config ~/.config/nyord-vpn/config.json connect
```

## Python Library Usage

The package can also be used as a Python library:

```python
import asyncio
from nyord_vpn import VPNClient, VPNConfig

async def main():
    # Create client with environment variables
    client = VPNClient()
    
    # Or with explicit configuration
    config = VPNConfig(
        username="your-username",
        password="your-password",
        default_country="Netherlands"
    )
    client = VPNClient(config=config)
    
    # Connect to VPN
    async with client:
        # Connect (defaults to config.default_country)
        await client.connect()
        
        # Or connect to specific country
        await client.connect("Netherlands")
        
        # Check status
        status = await client.status()
        print(f"Connected: {status['connected']}")
        print(f"IP: {status['ip']}")
        print(f"Country: {status['country']}")
        print(f"Server: {status['server']}")
        
        # List available countries
        countries = await client.list_countries()
        print("Available countries:", countries)
        
        # Disconnect
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

### Error Handling

The library provides specific exception types for different error cases:

```python
from nyord_vpn import (
    VPNError,           # Base exception
    VPNConfigError,     # Configuration errors
    VPNConnectionError, # Connection failures
    VPNStatusError,     # Status check failures
    VPNCredentialsError # Authentication failures
)

try:
    await client.connect()
except VPNConnectionError as e:
    print(f"Failed to connect: {e}")
except VPNCredentialsError as e:
    print(f"Invalid credentials: {e}")
```

## Development

This project uses [Hatch](https://hatch.pypa.io/) for development workflow management.

```bash
# Install hatch if you haven't already
pip install hatch

# Create and activate development environment
hatch shell

# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Run linting
hatch run lint

# Format code
hatch run format
```

## Logging Configuration

The package uses structured logging with configurable output:

```python
from nyord_vpn import VPNClient
from nyord_vpn.utils.log_utils import LogConfig

# Configure logging to file
log_config = LogConfig(log_file="~/vpn.log")
client = VPNClient(log_file="~/vpn.log")

# Or from CLI
nyord-vpn --log-file ~/vpn.log connect
```

The logs include:
- Connection attempts and results
- API fallback events
- Error details (with sensitive data redacted)
- Status changes

## Security Considerations

1. Credential Storage:
   - Use environment variables (preferred) or config files
   - Config files are created with secure permissions (0o700)
   - Passwords are handled using `SecretStr` to prevent accidental exposure

2. API Security:
   - All API calls use HTTPS
   - Certificate validation is enforced
   - Automatic retry with exponential backoff for API calls

3. System Security:
   - Subprocess commands are validated to prevent injection
   - Temporary files are securely created and cleaned up
   - Sensitive data is redacted from logs

## Troubleshooting

### Common Issues

1. Connection Failures
   ```bash
   # Check if credentials are properly set
   echo $NORD_USER $NORD_PASSWORD
   
   # Verify network connectivity
   nyord-vpn status
   
   # Try connecting with verbose logging
   nyord-vpn --log-file ~/vpn.log connect
   ```

2. Permission Issues
   ```bash
   # Fix config directory permissions
   chmod 700 ~/.config/nyord-vpn
   
   # Ensure proper sudo access for VPN commands
   sudo nyord-vpn connect
   ```

3. API Errors
   ```python
   # Enable fallback API
   config = VPNConfig(use_legacy_fallback=True)
   client = VPNClient(config=config)
   
   # Or via CLI
   nyord-vpn --config <(echo '{"use_legacy_fallback": true}') connect
   ```

### Debug Mode

For detailed debugging:

```bash
# Enable debug logging
export NORDVPN_LOG_LEVEL=DEBUG
nyord-vpn --log-file ~/vpn.log connect

# Check logs
tail -f ~/vpn.log
```

### Common Error Messages

1. "Failed to initialize VPN client"
   - Check if config file exists and has correct permissions
   - Verify environment variables are set correctly

2. "Failed to connect to {country}"
   - Try a different country
   - Check if country name is valid (use `list-countries`)
   - Verify network connectivity

3. "Network or system error"
   - Check system firewall settings
   - Verify OpenVPN is installed and accessible
   - Check system DNS settings

## License

MIT License 