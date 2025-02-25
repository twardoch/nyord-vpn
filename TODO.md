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

## 1. DEVELOPMENT

After each set of changes, update @PROGRESS.md with what you've done (`- [x]`). Upgrade priorities for NEXT TODO (`- [!]`), re-think the normal TODO (`- [ ]`)

Periodically do:

```
uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]; tree -I *cache__; hatch fmt --unsafe-fixes; hatch fmt --unsafe-fixes; hatch -e test run test; 
```

and react to the results. Use `uv pip...` instead of `pip...` if needed. 

## 2. Working modality

You'll lead two experts: "Ideot" for creative, unorthodox ideas and "Critin" to critique flawed thinking and moderate for balanced discussions. The three of you shall illuminate knowledge with concise, beautiful responses, process methodically for clear answers, collaborate step-by-step, sharing thoughts and adapting. If errors are found, step back and focus on accuracy and progress.

Independently tackle challenges systematically, being adaptable and resourceful. Research deeply using all tools, revising to ensure conclusive, exhaustive, insightful results. When you're finished, print "Wait, but" to go back, think & reflect, revise & improvement what you've done (but don't invent functionality freely). Repeat this. Focus on minimal viable next versions of the code. Ship often and early. 

## 3. General coding principles

Verify info. No assumptions. No apologies. No major invented changes. No unneeded confirmations or checks. Keep existing code and structures unless they need to change. No unnecessary updates or current implementation discussion. Avoid magic numbers, handle edge cases, use assertions to validate assumptions and catch potential errors early.

Every code can fail. Write code that fails gracefully and is UX friendly: uses retries (within reason), does not make stupid assumptions, tests successes, uses fallbacks and backoffs, and then, if the code needs to message the user, be clear and suggest to the user the next steps. Don't prompt the user to do something that the computer can obviously do. The code should ask the user only if there is a real decision to be made. And you should ask me only if a real decision is needed.  

## 4. Keep track of paths

In every source file you create or edit, always maintain the up-to-date `this_file` record that shows the path of the current file relative to the root of the project. Place the `this_file` record near the top of the file, as a comment after the shebangs, or in the YAML Markdown frontmatter. Use these records for orientation. 

## 5. Follow this style for Python

Follow PEP 8. Write clear names. Keep it simple (PEP 20). Use type hints, imperative docstrings (PEP 257), f-strings, and structural pattern matching. Extract repeated logic. Handle errors. Keep functions small. Prefer flat structures. Use pathlib, pydantic as needed. Write maintainable code. 

EVEN IF YOU'RE NOT prompted, always write a "verbose" mode logugu-based logging for debug purposes, write explanatory docstrings and comments that not only explain what a given item (module, function, method) does, but also why it does it, and where and how it's used elsewhere in the code. 

ONLY IF YOU ARE prompted, extend existing features in a way that adds complexity, or refactor in a way that may break things. Remember: minimal viable next version is always our goal. IF NOT PROMPTED, do NOT make such changes. 

For CLI Python scripts, use fire & rich, and start the script with 

```
#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["PKG1", "PKG2"]
# ///
# this_file: PATH_TO_CURRENT_FILE
```

# Nyord VPN Codebase Refactoring TODO

## 6. Remaining Tasks (Prioritized)

### 6.1. High Priority Items

#### 6.1.1. Fix Test Failures

- [!] Fix test_openvpn_tcp_validation failure in ServerManager class
  - Update `_is_valid_server()` method to correctly check for OpenVPN TCP support
  - Add debug logging to diagnose technology validation issues
- [!] Fix test_fetch_all, test_get_servers_by_country, and test_get_servers_by_group failures
  - Update sample fixtures to include proper server relationships
  - Ensure server-to-group relationships are properly established
  - Ensure server-to-location relationships are properly established
- [!] Fix test_get_servers test failure related to locations relationship
- [!] Fix test_server_filtering failure related to mock implementation

#### 6.1.2. Fix Import Errors in Integration Tests

- [!] Update import statements in integration tests
  - Change `from nyord_vpn.core.exceptions import ...` to `from nyord_vpn.exceptions import ...`
  - Replace references to `VPNClient` with `Client`
- [!] Fix mock setup in test_server_manager.py to correctly simulate API response structure

#### 6.1.3. Core Module - `client.py`

- [!] Break down complex methods into smaller helper functions
  - [!] Refactor the `go()` method into smaller functions for each step:
    - Extract server selection logic into a separate method
    - Create a dedicated method for connection validation
    - Implement retry logic with proper error handling
  - [!] Extract connection validation logic into separate functions
  - [!] Create helper functions for environment variable handling
- [!] Fix boolean arguments and other linting issues
  - [!] Make all boolean parameters keyword-only arguments
  - [!] Fix type annotations for better static analysis
  - [!] Add proper validation for function parameters

### 6.2. Medium Priority Items

#### 6.2.1. Network Module - `vpn.py`

- [!] Make boolean arguments keyword-only
- [!] Add comprehensive type hints for all functions and methods
- [ ] Implement retry logic for connection attempts with tenacity
- [ ] Break down complex methods:
  - [ ] Split `setup_connection()` into smaller focused functions
  - [ ] Refactor `connect()` method to improve readability
  - [ ] Extract IP validation logic into a utility function
- [ ] Replace random.uniform with secrets.SystemRandom().uniform for better security
- [ ] Improve error handling with specific exception types and recovery mechanisms

#### 6.2.2. Utils Module - `templates.py`

- [!] Fix security vulnerabilities in subprocess calls (S603, S607)
- [!] Replace datetime.now() and datetime.fromtimestamp() with timezone-aware versions (DTZ005, DTZ006)
- [!] Fix exception handling issues:
  - [!] Replace long error messages with proper exception classes (TRY003)
  - [!] Use `raise ... from err` consistently (B904)
  - [!] Move try/except out of loops for better performance (PERF203)
  - [!] Use `else` blocks appropriately after try/except (TRY300)

### 6.3. Lower Priority Items

#### 6.3.1. Utils Module - `utils.py`

- [!] Replace os.path functions with pathlib equivalents (PTH110, PTH118, PTH123)
- [!] Fix security vulnerability in subprocess call (S603)
- [!] Fix error handling to use `else` blocks appropriately (TRY300)
- [ ] Implement atomic file operations for state management

#### 6.3.2. Main Module - `__main__.py`

- [!] Update CLI class to use the updated Client API
  - [!] Replace any usage of deprecated classes/methods with their updated counterparts
  - [!] Update command-line arguments to match new API structure
  - [!] Ensure all commands use the new Client implementation
- [!] Improve error handling and user feedback
  - [!] Add specific error handling for common user errors
  - [!] Provide clear, actionable error messages with recovery steps
  - [!] Add verbose output mode for troubleshooting

## 7. Implementation Steps

### 7.1. Fixing Test Failures

#### 7.1.1. Fix the OpenVPN TCP validation issue in server_manager.py

```python
def _is_valid_server(self, server: dict) -> bool:
    """Check if a server is valid for OpenVPN TCP connection."""
    # Add debug logging for technologies to diagnose the issue
    if self.verbose:
        technologies = server.get("technologies", [])
        self.logger.debug(f"Server technologies: {technologies}")
        
    # Check server status
    if server.get("status") != "online":
        if self.verbose:
            self.logger.debug(f"Server {server.get('hostname')} is not online")
        return False
        
    # Check hostname
    hostname = server.get("hostname", "")
    if not hostname.endswith(".nordvpn.com"):
        if self.verbose:
            self.logger.debug(f"Invalid hostname: {hostname}")
        return False
    
    # Check load
    load = server.get("load", -1)
    if not (0 <= load <= 100):
        if self.verbose:
            self.logger.debug(f"Server {hostname} has invalid load: {load}")
        return False
    
    # Fix the OpenVPN TCP check:
    has_openvpn_tcp = False
    for tech in server.get("technologies", []):
        if isinstance(tech, dict) and "name" in tech:
            tech_name = tech.get("name", "")
            if "OpenVPN TCP" in tech_name:
                has_openvpn_tcp = True
                break
    
    if not has_openvpn_tcp:
        if self.verbose:
            self.logger.debug(f"Server {hostname} does not support OpenVPN TCP")
        return False
    
    return True
```

#### 7.1.2. Fix model relationship issues in test fixtures

Update sample_server fixture:

```python
@pytest.fixture
def sample_server(sample_group, sample_location, sample_technology):
    """Create a sample server with proper relationships."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "name": "us1234.nordvpn.com",
        "station": "us1234",
        "hostname": "us1234.nordvpn.com",
        "ipv6_station": "",
        "status": "online",
        "load": 45,
        "groups": [{"id": 1, "pivot": {"server_id": 1, "group_id": 1}}],
        "locations": [{"id": 1, "pivot": {"server_id": 1, "location_id": 1}}],
        "technologies": [sample_technology],
    }
```

### 7.2. Refactoring the Client.go() Method

Break down the go() method into smaller functions:

```python
def _validate_country_code(self, country_code: str) -> None:
    """Validate that the country code is valid."""
    if not country_code or not isinstance(country_code, str) or len(country_code) != 2:
        raise VPNError(f"Country code must be a two-letter code, got: {country_code!r}")
    
    # Optionally validate against known country codes
    countries = self.list_countries()
    country_codes = [c["code"].lower() for c in countries]
    
    if country_code.lower() not in country_codes:
        raise VPNError(f"Country code '{country_code}' not found in available countries: {', '.join(country_codes)}")

def _select_server(self, country_code: str) -> dict:
    """Select the best server for the specified country."""
    servers = self.server_manager.select_fastest_server(country_code)
    if not servers:
        raise VPNError(f"No servers available in {country_code}")

    # Take the first (fastest) server
    server = servers[0]
    hostname = server.get("hostname")
    if not hostname:
        raise VPNError("Selected server has no hostname")

    if self.verbose:
        self.logger.info(f"Selected server: {hostname}")
        
    return server

def _establish_connection(self, server: dict) -> None:
    """Establish the VPN connection to the specified server."""
    hostname = server.get("hostname")
    
    # Set up VPN configuration
    if not self.username or not self.password:
        raise VPNError("Missing VPN credentials")
        
    self.vpn_manager.setup_connection(hostname, self.username, self.password)

    # Connect to VPN
    if self.verbose:
        self.logger.info("Establishing VPN connection...")
        
    # Connect and wait for result
    self.vpn_manager.connect([server])  # Pass server to try

def go(self, country_code: str) -> None:
    """Connect to VPN in specified country."""
    try:
        # First check if we're already connected
        status = self.status()
        if status.get("connected", False):
            # VPN manager will handle disconnection automatically
            if self.verbose:
                self.logger.info("Already connected, will disconnect before connecting to new server")

        # Validate the country code
        self._validate_country_code(country_code)
        
        # Select the best server
        server = self._select_server(country_code)
        
        # Establish the connection
        self._establish_connection(server)

        # Get status for display
        status = self.status()
        console.print("[green]Successfully connected to VPN[/green]")
        console.print(f"Private IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]")
        console.print(f"Country: [cyan]{status.get('country', 'Unknown')}[/cyan]")
        console.print(f"Server: [cyan]{status.get('server', 'Unknown')}[/cyan]")

    except Exception as e:
        raise VPNError(f"Failed to connect: {e}")
```
