# TODO

A modern Python client for NordVPN with automatic API fallback support, providing both a CLI interface and a Python library.

```bash
# Install system requirements first
brew install openvpn  # macOS
sudo apt install openvpn  # Ubuntu/Debian
sudo dnf install openvpn  # Fedora/RHEL

# Then install and use the package
pip install nyord-vpn
export NORD_USER="username" NORD_PASSWORD="password"
nyord-vpn go de  # Connect to a German VPN
nyord-vpn info  # Check status
nyord-vpn bye  # Disconnect
```

## DEVELOPMENT

After each set of changes, update @TODO.md with what you've done (`- [x] `). Upgrade priorities for NEXT TODO (`- [!]`), re-think the normal TODO (`- [ ] `)

Periodically do:

```
uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]; tree -I *cache__; hatch fmt --unsafe-fixes; hatch fmt --unsafe-fixes; hatch -e test run test; 
```

and react to the results. Use `uv pip...` instead of `pip...` if needed. 

## Working modality

You'll lead two experts: "Ideot" for creative, unorthodox ideas and "Critin" to critique flawed thinking and moderate for balanced discussions. The three of you shall illuminate knowledge with concise, beautiful responses, process methodically for clear answers, collaborate step-by-step, sharing thoughts and adapting. If errors are found, step back and focus on accuracy and progress.

Independently tackle challenges systematically, being adaptable and resourceful. Research deeply using all tools, revising to ensure conclusive, exhaustive, insightful results. When you’re finished, print "Wait, but" to go back, think & reflect, revise & improvement what you’ve done (but don’t invent functionality freely). Repeat this. Focus on minimal viable next versions of the code. Ship often and early. 

## General coding principles

Verify info. No assumptions. No apologies. No major invented changes. No unneeded confirmations or checks. Keep existing code and structures unless they need to change. No unnecessary updates or current implementation discussion. Avoid magic numbers, handle edge cases, use assertions to validate assumptions and catch potential errors early.

Every code can fail. Write code that fails gracefully and is UX friendly: uses retries (within reason), does not make stupid assumptions, tests successes, uses fallbacks and backoffs, and then, if the code needs to message the user, be clear and suggest to the user the next steps. Don't prompt the user to do something that the computer can obviously do. The code should ask the user only if there is a real decision to be made. And you should ask me only if a real decision is needed.  

## Keep track of paths

In every source file you create or edit, always maintain the up-to-date `this_file` record that shows the path of the current file relative to the root of the project. Place the `this_file` record near the top of the file, as a comment after the shebangs, or in the YAML Markdown frontmatter. Use these records for orientation. 

## Follow this style for Python

Follow PEP 8. Write clear names. Keep it simple (PEP 20). Use type hints, imperative docstrings (PEP 257), f-strings, and structural pattern matching. Extract repeated logic. Handle errors. Keep functions small. Prefer flat structures. Use pathlib, pydantic as needed. Write maintainable code. 

EVEN IF YOU’RE NOT prompted, always write a "verbose" mode logugu-based logging for debug purposes, write explanatory docstrings and comments that not only explain what a given item (module, function, method) does, but also why it does it, and where and how it's used elsewhere in the code. 

ONLY IF YOU ARE prompted, extend existing features in a way that adds complexity, or refactor in a way that may break things. Remember: minimal viable next version is always our goal. IF NOT PROMPTED, do NOT make such changes. 

For CLI Python scripts, use fire & rich, and start the script with 

```
#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["PKG1", "PKG2"]
# ///
# this_file: PATH_TO_CURRENT_FILE
```

# Nyord VPN Codebase Refactoring Specification

## Guiding Principles

1. **Adopt the new Pydantic-based API layer**
2. **Maintain stability by prioritizing non-disruptive changes**
3. **Address linting and code style issues systematically**
4. **Implement security improvements where straightforward**
5. **Clearly mark deprecated components without removing critical functionality**
6. **Improve error handling consistently across the codebase**

## File-by-File Specification

### API Module (`src/nyord_vpn/api/`)

#### `src/nyord_vpn/api/api.py`

**Action**: Modify to make this the central API interface.

```python
"""Central API client for NordVPN interactions.

This module provides the main entry point for interacting with the NordVPN API,
utilizing both v1 and v2 API endpoints as needed.
"""

# Remove shebang and any commented-out code at the top

class NordVPNAPI:
    def __init__(self, timeout: int = 10) -> None:
        """Initialize the NordVPN API client.
        
        Args:
            timeout: Request timeout in seconds
        """
        # Current implementation...

    def get_recommended_servers(
        self, *, refresh: bool = False
    ) -> list[v1_recommendations.RecommendedServer]:
        """DEPRECATED: Get recommended servers using v1 API.
        
        Use find_best_server with use_v2=True instead. Will be removed in a future version.
        
        Args:
            refresh: Whether to refresh the cached data
            
        Returns:
            List of recommended servers
        """
        # Current implementation but with keyword-only argument

    # Similarly update other v1 methods with deprecation notices and keyword-only arguments

    def find_best_server(
        self, 
        country_code: str, 
        group_identifier: str | None = None, 
        *, 
        use_v2: bool = True
    ) -> Union[v1_recommendations.RecommendedServer, v2_servers.Server]:
        """Find the best server matching the given criteria.
        
        Attempts to use the v2 API by default with fallback to v1 if specified or needed.
        
        Args:
            country_code: Two-letter country code
            group_identifier: Optional group identifier for filtering
            use_v2: Whether to use v2 API (recommended)
            
        Returns:
            Best server based on load and availability
            
        Raises:
            ValueError: If no matching servers are found
        """
        try:
            if use_v2:
                # Implement v2 logic
                servers = self.get_servers()[0]
                matching_servers = [
                    server for server in servers 
                    if server.locations[0].country.code.upper() == country_code.upper()
                ]
                
                if group_identifier:
                    matching_servers = [
                        server for server in matching_servers
                        if any(group.identifier == group_identifier for group in server.groups)
                    ]
                
                if not matching_servers:
                    raise ValueError("No matching servers found with v2 API")
                    
                return min(matching_servers, key=lambda s: s.load)
        except Exception as e:
            # Log the error
            logger.warning(f"V2 API error: {e}, falling back to v1")
            pass
            
        # Fall back to v1 implementation
        servers = self.get_recommended_servers()
        # Rest of current implementation...

    # Remove main block and move to a test script or file
```

#### `src/nyord_vpn/api/v1_*.py` files (v1_countries.py, v1_groups.py, v1_recommendations.py, v1_technologies.py)

**Action**: Keep but mark as deprecated and clean up.

For each file:

```python
"""DEPRECATED: Client for the NordVPN v1 API {specific endpoint}.

This module provides access to the legacy NordVPN v1 API. 
Use v2_servers.py for new development.
This module will be removed in a future version.
"""

# Remove shebang and commented-out code
# Fix boolean positional arguments
# Fix ambiguous variable names
# Add proper docstrings to classes and methods
# Update error handling to use specific exceptions from exceptions.py
# Remove main block if present
```

#### `src/nyord_vpn/api/v2_servers.py`

**Action**: Refine and improve.

```python
"""Client for the NordVPN v2 API servers endpoint.

This module provides access to the modern NordVPN v2 API, which offers
more comprehensive server information in a single request.
"""

# Fix linting issues, particularly ambiguous variable names (E741)
# For example, change 'l' to 'location_data'

def _link_server_relations(self, server: Server, maps: dict) -> None:
    """Link server relations from separate data structures.
    
    This method connects servers with their related entities (groups, services, locations)
    by replacing IDs with actual object references. This simplifies data access in the
    returned server objects.
    
    Args:
        server: Server object to update
        maps: Dictionary of related entity maps
    """
    # Current implementation with improved comments

# Add proper docstrings to other methods
# Add comprehensive type hints where missing
```

### Core Module (`src/nyord_vpn/core/`)

#### `src/nyord_vpn/core/__init__.py`

**Action**: Add module docstring.

```python
"""Core module for nyord_vpn, containing client implementation."""
```

#### `src/nyord_vpn/core/api.py`

**Action**: Deprecate and eventually remove.

```python
"""DEPRECATED: Legacy API client implementation.

This module has been replaced by nyord_vpn.api.api.NordVPNAPI.
It will be removed in a future version.
"""

import warnings

warnings.warn(
    "This module is deprecated. Use nyord_vpn.api.api.NordVPNAPI instead.",
    DeprecationWarning,
    stacklevel=2
)

# Rest of existing code
```

#### `src/nyord_vpn/core/base.py`

**Action**: Deprecate and eventually remove.

```python
"""DEPRECATED: Legacy base client implementation.

This module has been replaced by nyord_vpn.api.api.NordVPNAPI.
It will be removed in a future version.
"""

import warnings

warnings.warn(
    "This module is deprecated. Use nyord_vpn.api.api.NordVPNAPI instead.",
    DeprecationWarning,
    stacklevel=2
)

# Fix boolean positional arguments and other linting issues
# But don't spend time on major refactoring since this is deprecated
```

#### `src/nyord_vpn/core/client.py`

**Action**: Refactor significantly to use the new API.

```python
"""Main client implementation for nyord_vpn."""

from nyord_vpn.api.api import NordVPNAPI
# Change import to avoid shadowing built-in
from nyord_vpn.exceptions import ConnectionError as VPNConnectionError

class Client:
    def __init__(self, username: str, password: str, *, verbose: bool = False) -> None:
        """Initialize the VPN client.
        
        Args:
            username: NordVPN username
            password: NordVPN password
            verbose: Whether to enable verbose logging
            
        Raises:
            VPNError: If credentials are missing
        """
        self.username = (
            username
            or os.environ.get("NORD_USER")
            or os.environ.get("NORDVPN_LOGIN")
        )
        self.password = (
            password
            or os.environ.get("NORD_PASSWORD")
            or os.environ.get("NORDVPN_PASSWORD")
        )
        
        # Validate credentials
        if not self.username or not self.password:
            raise VPNError(
                "Missing VPN credentials. Set username/password or environment variables."
            )
            
        # Add the new API client
        self.api = NordVPNAPI(timeout=30)
        
        # Keep legacy client, but mark as deprecated with comment
        self.api_client = NordVPNAPIClient(self.username, self.password, verbose)  # DEPRECATED
        self.server_manager = ServerManager(self.api_client)
        self.vpn_manager = VPNConnectionManager(
            self.api_client, self.server_manager, verbose=verbose
        )
        
        # Rest of initialization...
    
    def is_protected(self) -> bool:
        """Check if the VPN connection is active.
        
        Returns:
            True if connected, False otherwise
        """
        status = self.status()
        return bool(status.get("connected", False))
    
    def go(self, country_code: str) -> None:
        """Connect to a VPN server in the specified country.
        
        Args:
            country_code: Two-letter country code
            
        Raises:
            VPNError: If connection fails
        """
        try:
            # Check if already connected
            status = self.status()
            if status.get("connected", False):
                current_country = status.get("country", "").lower()
                if current_country == country_code.lower():
                    self.logger.info(f"Already connected to {country_code}")
                    return
                else:
                    self.logger.info(f"Disconnecting from {current_country}")
                    self.bye()
            
            # Try with new v2 API first
            try:
                server = self.api.find_best_server(country_code, use_v2=True)
                hostname = server.hostname
                self.logger.info(f"Selected server: {hostname}")
                console.print(f"Selected server: [cyan]{hostname}[/cyan]")
            except Exception as e:
                # Fall back to legacy server selection
                self.logger.warning(f"V2 API server selection failed: {e}, using legacy method")
                servers = self.server_manager.select_fastest_server(country_code)
                if not servers:
                    raise VPNError(f"No servers available in {country_code}")
                server = servers[0]  # Take the first/best server
                hostname = server.get("hostname")
                if not hostname:
                    raise VPNError("Selected server has no hostname")
                self.logger.info(f"Selected server (legacy): {hostname}")
                console.print(f"Selected server: [cyan]{hostname}[/cyan]")
            
            # Connect using the selected server
            if not self.username or not self.password:
                raise VPNError("Missing VPN credentials")
                
            self.vpn_manager.setup_connection(hostname, self.username, self.password)
            self.logger.info("Establishing VPN connection...")
            console.print("Establishing VPN connection...")
            
            # Pass the server to connect
            self.vpn_manager.connect([server])  # Will be modified to handle single server
            
            # Show connection info
            status = self.status()
            console.print("[green]Successfully connected to VPN[/green]")
            console.print(f"Private IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]")
            console.print(f"Country: [cyan]{status.get('country', 'Unknown')}[/cyan]")
            console.print(f"Server: [cyan]{status.get('server', 'Unknown')}[/cyan]")
        except Exception as e:
            raise VPNError(f"Failed to connect: {e}") from e
    
    # Refactor other methods similarly
    # Break down complex methods into smaller helper functions
    # Fix boolean arguments and other linting issues
```

### Network Module (`src/nyord_vpn/network/`)

#### `src/nyord_vpn/network/__init__.py`

**Action**: Add module docstring.

```python
"""Network-related functionality for nyord_vpn."""
```

#### `src/nyord_vpn/network/country.py`

**Action**: Keep but mark for future consolidation.

```python
"""DEPRECATED: Country-related data handling.

This module will be consolidated with the API module in a future version.
"""

# Add TODO comments for future consolidation with API code
# Keep existing functionality intact
```

#### `src/nyord_vpn/network/server.py`

**Action**: Refactor to use new API.

```python
"""Server selection and management for VPN connections.

This module provides functionality for selecting optimal VPN servers
based on various criteria including location, load, and ping time.
"""

# Add type hints for functions and variables
# Replace random.randrange and random.choice with secrets.choice
import secrets

# Example refactored method
def _select_diverse_servers(
    self, servers: list[dict[str, Any]], count: int = 5
) -> list[dict[str, Any]]:
    """Select a diverse set of servers from different regions.
    
    Args:
        servers: List of server dictionaries
        count: Number of servers to select
        
    Returns:
        List of selected servers
    """
    if not servers:
        return []
        
    # Group servers by region
    regions: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for server in servers:
        region = server.get("country", {}).get("region", {}).get("name", "Unknown")
        regions[region].append(server)
    
    selected = []
    region_names = list(regions.keys())
    
    # Select one server from each region until we have enough
    while len(selected) < count and region_names:
        region_idx = secrets.randbelow(len(region_names))
        region = region_names.pop(region_idx)
        
        if region_servers := regions.get(region, []):
            server_idx = secrets.randbelow(len(region_servers))
            server = region_servers[server_idx]
            selected.append(server)
    
    # If we need more servers, add from remaining
    remaining_servers = [s for s in servers if s not in selected]
    if remaining_servers and len(selected) < count:
        sample_size = min(count - len(selected), len(remaining_servers))
        
        # Add up to sample_size servers from remaining_servers
        indices = []
        for _ in range(sample_size):
            if not remaining_servers:
                break
            idx = secrets.randbelow(len(remaining_servers))
            selected.append(remaining_servers.pop(idx))
    
    return selected

# Address security issues in subprocess calls by validating input
# Reduce complexity where possible by extracting helper functions
```

#### `src/nyord_vpn/network/vpn_commands.py`

**Action**: Refactor for better usability.

```python
"""OpenVPN command generation utilities."""

from dataclasses import dataclass
from pathlib import Path

@dataclass
class OpenVPNConfig:
    """Configuration parameters for OpenVPN command generation."""
    config_path: Path
    auth_path: Path
    verbosity: int = 3
    connect_retry: int = 10
    connect_timeout: int = 10
    ping_interval: int = 10
    ping_restart: int = 60
    log_path: Path = None
    proxy: str = None

def get_openvpn_command(config: OpenVPNConfig) -> list[str]:
    """Generate OpenVPN command with the given configuration.
    
    Args:
        config: OpenVPN configuration parameters
        
    Returns:
        List of command arguments
        
    Raises:
        VPNConfigError: If configuration is invalid or files not found
    """
    if not config.config_path.exists():
        raise VPNConfigError(f"OpenVPN config file not found: {config.config_path}")
        
    if not config.auth_path.exists():
        raise VPNConfigError(f"OpenVPN auth file not found: {config.auth_path}")
    
    # Validate verbosity
    if not 1 <= config.verbosity <= 6:
        raise VPNConfigError(f"Invalid verbosity level: {config.verbosity} (must be 1-6)")
        
    # Generate base command
    cmd = [
        "openvpn",
        "--config", str(config.config_path),
        "--auth-user-pass", str(config.auth_path),
        "--verb", str(config.verbosity),
        "--connect-retry", str(config.connect_retry),
        "--connect-timeout", str(config.connect_timeout),
        "--ping", str(config.ping_interval),
        "--ping-restart", str(config.ping_restart),
        "--daemon"
    ]
    
    # Add platform-specific options
    system = platform.system().lower()
    if system == "linux":
        cmd.extend(
            ["--writepid", "/var/run/openvpn.pid", "--script-security", "2"]
        )
        
        # Add resolv-conf script if available
        resolv_conf_script = Path("/etc/openvpn/update-resolv-conf")
        if resolv_conf_script.exists():
            cmd.extend([
                "--up", str(resolv_conf_script),
                "--down", str(resolv_conf_script)
            ])
    
    # Add log path if specified
    if config.log_path:
        cmd.extend(["--log", str(config.log_path)])
    
    # Add proxy if specified
    if config.proxy:
        cmd.extend(["--http-proxy", config.proxy])
        
    return cmd
```

#### `src/nyord_vpn/network/vpn.py`

**Action**: Refactor for better maintainability.

```python
"""VPN connection management using OpenVPN."""

# Remove redundant constants
# Make boolean arguments keyword-only
# Add type hints
# Add retry logic for connection attempts

from tenacity import retry, stop_after_attempt, wait_exponential

class VPNConnectionManager:
    def __init__(self, api_client: Any, server_manager: Any, *, verbose: bool = False) -> None:
        """Initialize the VPN connection manager.
        
        Args:
            api_client: API client for VPN server information
            server_manager: Server manager for server selection
            verbose: Whether to enable verbose logging
        """
        # Current initialization...
    
    # Add retry logic to connect method
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def _start_openvpn_process(self, cmd: list[str]) -> subprocess.Popen:
        """Start the OpenVPN process with retries.
        
        Args:
            cmd: Command to execute
            
        Returns:
            Process object
            
        Raises:
            VPNError: If process cannot be started after retries
        """
        try:
            self.logger.debug("Running OpenVPN command:")
            self.logger.debug(" ".join(cmd))
            
            if OPENVPN_LOG and OPENVPN_LOG.exists():
                OPENVPN_LOG.unlink()
                
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if process.poll() is not None:
                stdout, stderr = process.communicate()
                raise VPNError(f"OpenVPN process exited immediately: {stderr}")
                
            return process
        except Exception as e:
            raise VPNError(f"Failed to start OpenVPN process: {e}")
    
    def connect(self, servers: list[dict[str, Any]]) -> None:
        """Connect to a VPN server.
        
        Args:
            servers: List of server information dictionaries
            
        Raises:
            VPNError: If connection fails
        """
        if not servers:
            raise VPNError("No servers provided")
            
        error_messages = []
        for server in servers:
            try:
                hostname = server.get("hostname")
                if not hostname:
                    raise VPNError("Invalid server info - missing hostname")
                
                # Rest of connection logic...
                # Use the _start_openvpn_process method with retry
                
                # Break the loop if connection succeeds
                break
            except Exception as e:
                error_messages.append(str(e))
                self.logger.warning(f"Failed to connect to {hostname}: {e}")
                continue
        else:
            # This executes if the loop didn't break (all servers failed)
            raise VPNError(
                "Failed to connect after trying all servers:\n" + "\n".join(error_messages)
            )
    
    # Break down other complex methods similarly
    # Replace random.uniform with secrets.SystemRandom().uniform
    # Improve error handling consistently
```

### Scripts Module (`src/nyord_vpn/scripts/`)

#### `src/nyord_vpn/scripts/__init__.py`

**Action**: Add module docstring.

```python
"""Scripts for nyord_vpn, including configuration updates."""
```

#### `src/nyord_vpn/scripts/update_countries.py`

**Action**: Update to use new API.

```python
"""Script to update country data for nyord_vpn.

TODO: Refactor this script to use the v2 API for fetching country data.
"""

# Remove unused variables
# Improve error handling
# Keep core functionality intact
```

### Storage Module (`src/nyord_vpn/storage/`)

#### `src/nyord_vpn/storage/__init__.py`

**Action**: Add module docstring.

```python
"""Storage functionality for nyord_vpn, including models and state management."""
```

#### `src/nyord_vpn/storage/models.py`

**Action**: Rename ConnectionError and document classes.

```python
"""Data models and exceptions for nyord_vpn."""

class City(TypedDict):
    """City information."""
    # Current implementation...

class Country(TypedDict):
    """Country information."""
    # Current implementation...

class CountryCache(TypedDict):
    """Cache structure for country data."""
    # Current implementation...

class VPNError(Exception):
    """Base class for VPN-related errors."""
    def __init__(self, message: str | None = None) -> None:
        """Initialize VPN error.
        
        Args:
            message: Error message
        """
        super().__init__(message or "An unknown VPN error occurred")

class ServerError(VPNError):
    """Error related to VPN server operations."""
    # Current implementation...

class VPNConnectionError(VPNError):
    """Error occurring during VPN connection."""
    # Renamed from ConnectionError to avoid shadowing built-in

# Remove unused exception classes or comment them out with deprecation notices
```

#### `src/nyord_vpn/storage/state.py`

**Action**: Improve error handling.

```python
"""State management for VPN connections."""

# Add docstrings to functions
# Improve error handling for file operations
```

### Utils Module (`src/nyord_vpn/utils/`)

#### `src/nyord_vpn/utils/__init__.py`

**Action**: Add module docstring.

```python
"""Utility functions for nyord_vpn."""
```

#### `src/nyord_vpn/utils/connection.py`

**Action**: Review for usage and potentially remove.

```python
"""DEPRECATED: Connection utilities.

This module will be removed in a future version.
"""

import warnings

warnings.warn(
    "This module is deprecated and will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

# Current implementation
```

#### `src/nyord_vpn/utils/templates.py`

**Action**: Simplify with tenacity.

```python
"""Template and configuration file utilities."""

from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=1, max=MAX_RETRY_DELAY)
)
def download_with_retry(url: str, headers: dict = None, timeout: int = 10) -> tuple[bytes, str]:
    """Download data with automatic retries.
    
    Args:
        url: URL to download
        headers: Optional request headers
        timeout: Request timeout in seconds
        
    Returns:
        Tuple of (content_bytes, content_hash)
        
    Raises:
        VPNConfigError: If download ultimately fails after retries
    """
    try:
        response = requests.get(url, headers=headers or HEADERS, timeout=timeout)
        response.raise_for_status()
        content = response.content
        content_hash = calculate_sha256(content)
        return content, content_hash
    except Exception as e:
        raise VPNConfigError(f"Failed to download {url}: {e}") from e

# Break down complex functions into smaller ones
# Improve docstrings and type hints
```

#### `src/nyord_vpn/utils/utils.py`

**Action**: Clean up unused components.

```python
"""General utility functions."""

# Remove references to unused COUNTRY_IDS_FILE and NORDVPN_COUNTRY_IDS
# Fix path-related issues
# Add proper docstrings and type hints
```

### Main Module Files

#### `src/nyord_vpn/__init__.py`

**Action**: Add exports.

```python
"""nyord_vpn: A modern Python client for NordVPN."""

from nyord_vpn.core.client import Client

__all__ = ["Client"]
```

#### `src/nyord_vpn/__main__.py`

**Action**: Update to use new API.

```python
"""Command-line interface for nyord_vpn."""

class CLI:
    def __init__(self, *, verbose: bool = False) -> None:
        """Initialize the CLI.
        
        Args:
            verbose: Whether to enable verbose logging
        """
        try:
            username = os.getenv("NORD_USER") or os.getenv("NORDVPN_LOGIN")
            password = os.getenv("NORD_PASSWORD") or os.getenv("NORDVPN_PASSWORD")
            
            if not username or not password:
                console.print("[red]Error: Missing credentials[/red]")
                console.print("Please set the following environment variables:")
                console.print("  NORD_USER or NORDVPN_LOGIN")
                console.print("  NORD_PASSWORD or NORDVPN_PASSWORD")
                sys.exit(1)
                
            self.client = Client(username, password, verbose=verbose)
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)
    
    # Update go, bye, info methods to use the updated Client
    # Remove update method if confirmed unnecessary
```

#### `src/nyord_vpn/exceptions.py`

**Action**: Rename ConnectionError and improve documentation.

```python
"""Exceptions for the nyord_vpn package."""

class NyordVPNError(Exception):
    """Base class for all nyord-vpn exceptions."""
    def __init__(self, message: str | None = None) -> None:
        """Initialize the exception.
        
        Args:
            message: Error message
        """
        super().__init__(message or self._format_message())
    
    def _format_message(self) -> str:
        """Format the error message.
        
        Returns:
            Formatted error message
        """
        return f"{self.__class__.__name__} occurred"

class VPNError(NyordVPNError):
    """General VPN operation error."""
    # Add docstring
    
class CredentialsError(NyordVPNError):
    """Error related to VPN credentials."""
    # Add docstring
    
class VPNConnectionError(NyordVPNError):
    """Error occurring during VPN connection."""
    # Renamed from ConnectionError
    
# Comment out unused exception classes with deprecation notices
# class DisconnectionError(NyordVPNError):
#     """DEPRECATED: This exception class may be removed in a future version."""
```

### Tests

**Action**: Update to reflect code changes.

For each test file, update imports to use `VPNConnectionError` instead of `ConnectionError` and ensure tests pass with the refactored code. Don't remove tests for legacy functionality yet.

## Implementation Strategy

1. **Small, Incremental Changes**: Make changes in small, testable increments
2. **Test After Each Step**: Run tests after each file change to catch regressions early
3. **Prioritization Order**:
   - Documentation improvements (docstrings, module comments)
   - Rename `ConnectionError` to `VPNConnectionError` throughout
   - Boolean parameter fixes and type hints
   - API integration in client code
   - Security improvements (secrets module, subprocess validation)
   - Error handling improvements
   - Complex method refactoring

## Additional Notes for Developers

- **Version Control**: Commit after each logical set of changes with descriptive messages
- **Backward Compatibility**: DO NOT Maintain backward compatibility with existing CLI usage patterns, we don't need it. You can reimagine the CLI (but we do like the simple "go" and "bye")
- **Testing Focus**: Pay special attention to testing the refactored `Client.go()` method as it's critical
- **Deprecation Timeline**: Add clear, specific information about when deprecated components will be removed
- **Documentation**: Update documentation to reflect API changes and new usage patterns

