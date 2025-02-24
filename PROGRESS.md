# Progress Report

## Overview
This progress report tracks the refactoring of the nyord-vpn codebase.

The primary focus of the refactoring effort is to:
1. Improve code quality and maintainability
2. Enhance error handling and user feedback
3. Strengthen security with better validation and randomization
4. Update the API interface for better usability
5. Add comprehensive documentation and testing

Current status: Completed initial refactoring of API and core modules, with focus shifting to improving error handling and breaking down complex methods.

## Completed Tasks

- [x] Add module docstrings to all files
- [x] Rename `ConnectionError` to `VPNConnectionError`
- [x] Make boolean parameters keyword-only
- [x] Move main blocks to test files
- [x] API Module refactoring
  - [x] Make `api.py` the central API interface with `NordVPNAPI` class
  - [x] Implement `find_best_server` method with v2 API support and v1 fallback
  - [x] Add deprecation notices and clean up `v1_*.py` files
  - [x] Fix linting issues and improve type hints in `v2_servers.py`
- [x] Core Module initial clean-up
  - [x] Add deprecation warnings to `api.py` and `base.py`
  - [x] Fix boolean positional arguments
- [x] Network Module - `vpn_commands.py`
  - [x] Create `OpenVPNConfig` dataclass with proper validation
  - [x] Implement `get_openvpn_command` function with proper validation
- [x] Network Module - `server.py`
  - [x] Replace random module with secrets module for secure randomization
  - [x] Fix type compatibility issues:
    - [x] Fix Technology type in server_technologies creation
    - [x] Fix parameter type in _select_diverse_servers function 
    - [x] Fix return type in get_country_info function
  - [x] Address security issues in subprocess calls by enhancing hostname validation
  - [x] Add comprehensive type hints for return types, parameters and variables
- [x] Core Module
  - [x] Refactor `client.py` to use the new `NordVPNAPI` class
  - [x] Update `tests/test_server_manager.py` to use `NordVPNAPI` instead of `NordVPNAPIClient`

## Current Tasks

### High Priority

#### Core Module - `client.py`
- [ ] Improve error handling and user feedback
  - [ ] Add more detailed error messages with troubleshooting steps
  - [ ] Implement proper exception handling with specific exception types
  - [ ] Add recovery suggestions in error messages
- [ ] Break down complex methods into smaller helper functions
  - [ ] Refactor the `go()` method into smaller functions for each step
  - [ ] Extract connection validation logic into separate functions
  - [ ] Create helper functions for environment variable handling
- [ ] Fix boolean arguments and other linting issues
  - [ ] Make all boolean parameters keyword-only arguments
  - [ ] Fix type annotations for better static analysis
  - [ ] Add proper validation for function parameters

### Medium Priority

#### Network Module - `vpn.py`
- [ ] Make boolean arguments keyword-only
- [ ] Add comprehensive type hints for all functions and methods
- [ ] Implement retry logic for connection attempts with tenacity
- [ ] Break down complex methods:
  - [ ] Split `setup_connection()` into smaller focused functions
  - [ ] Refactor `connect()` method to improve readability
  - [ ] Extract IP validation logic into a utility function
- [ ] Replace random.uniform with secrets.SystemRandom().uniform for better security
- [ ] Improve error handling with specific exception types and recovery mechanisms

#### Tests
- [ ] Fix import error in `tests/test_client.py` (change import from nyord_vpn.core.exceptions to nyord_vpn.exceptions)
- [ ] Update test fixtures to include missing fields:
  - [ ] Add `type` field to Group model in test fixtures
  - [ ] Add `server_count` field to Country and City models in test fixtures 
- [ ] Fix validation errors in models and tests:
  - [ ] Fix test mocks to have all required fields in API responses
  - [ ] Update model validation to handle missing fields gracefully
  - [ ] Fix server filtering test failures in test_v2_servers.py
- [ ] Fix mock setup in `tests/test_server_manager.py` (AttributeError: Mock object has no attribute 'get')
- [ ] Update imports to use `VPNConnectionError` instead of `ConnectionError`
- [ ] Fix test failures in integration tests

### Lower Priority

#### Utils Module - `templates.py`
- [ ] Fix security vulnerabilities in subprocess calls (S603, S607)
- [ ] Replace datetime.now() and datetime.fromtimestamp() with timezone-aware versions (DTZ005, DTZ006)
- [ ] Fix exception handling issues:
  - [ ] Replace long error messages with proper exception classes (TRY003)
  - [ ] Use `raise ... from err` consistently (B904)
  - [ ] Move try/except out of loops for better performance (PERF203)
  - [ ] Use `else` blocks appropriately after try/except (TRY300)
- [ ] Implement retry logic with tenacity for network operations
- [ ] Break down complex functions into smaller ones
- [ ] Improve docstrings and type hints
- [ ] Add more detailed logging for debugging purposes
- [ ] Replace random module usage with secrets module (S311)

#### Utils Module - `utils.py`
- [ ] Replace os.path functions with pathlib equivalents (PTH110, PTH118, PTH123)
- [ ] Fix security vulnerability in subprocess call (S603)
- [ ] Fix error handling to use `else` blocks appropriately (TRY300)
- [ ] Implement atomic file operations for state management
- [ ] Add better error handling for file operations
- [ ] Improve type annotations and docstrings

#### Main Module - `__main__.py`
- [ ] Update CLI class to use the updated Client API
  - [ ] Replace any usage of deprecated classes/methods with their updated counterparts
  - [ ] Update command-line arguments to match new API structure
  - [ ] Ensure all commands use the new Client implementation
- [ ] Improve error handling and user feedback
  - [ ] Add specific error handling for common user errors (e.g., invalid credentials, connection failures)
  - [ ] Provide clear, actionable error messages with recovery steps
  - [ ] Add verbose output mode for troubleshooting
- [ ] Add more detailed help messages and documentation
  - [ ] Enhance command-line help with examples and parameter descriptions
  - [ ] Add context-specific help for each command
  - [ ] Include version information and system requirements
- [ ] Implement command auto-completion for better user experience
  - [ ] Add shell completion scripts (Bash, Zsh, Fish)
  - [ ] Provide dynamic completion for country/server names
  - [ ] Document how to enable command completion

#### Documentation
- [ ] Update README.md with installation and usage instructions
  - [ ] Add clear step-by-step installation guide for different platforms
  - [ ] Include dependency installation instructions
  - [ ] Update usage examples with the new API
- [ ] Add API documentation with example usage
  - [ ] Document the public API classes and methods
  - [ ] Provide usage examples for common scenarios
  - [ ] Include type information and error handling patterns
- [ ] Create usage examples for common scenarios
  - [ ] Basic connection and disconnection
  - [ ] Connecting to specific countries/servers
  - [ ] Handling connection failures
  - [ ] Using different protocols and settings
- [ ] Document troubleshooting steps for common issues
  - [ ] Authentication problems
  - [ ] Connection failures
  - [ ] OpenVPN configuration issues
  - [ ] Platform-specific troubleshooting
- [ ] Add architecture overview diagrams
  - [ ] Component interaction diagram
  - [ ] Class hierarchy diagram
  - [ ] API request flows
  - [ ] Error handling paths

## Next Steps

Based on the prioritized tasks, the following immediate next steps have been identified:

1. **Improve error handling in client.py**
   - Add more detailed error messages with troubleshooting steps
   - Implement proper exception handling with specific exception types
   - Add recovery suggestions in error messages

2. **Fix test fixtures**
   - Add `type` field to Group model in test fixtures
   - Add `server_count` field to Country and City models in test fixtures
   - Fix validation errors in test mocks to address test failures

3. **Make boolean arguments keyword-only in vpn.py**
   - Update function signatures
   - Update all function calls to use keyword arguments
   - Add proper validation for boolean parameters

4. **Fix security vulnerabilities in templates.py**
   - Replace subprocess calls with safer alternatives
   - Fix datetime timezone issues
   - Improve exception handling

These tasks will form the basis for the next sprint of work, focusing on improving code quality, security, and test reliability.

## Implementation Notes

### Fixing Test Fixtures

The following approach is recommended for addressing the test fixture issues:

1. **Update Group model fixtures**:
   ```python
   # In tests/test_v2_servers.py and other test files
   @pytest.fixture
   def sample_group_type() -> dict:
       """Create a sample group type for testing."""
       return {
           "id": 1,
           "created_at": "2024-01-01T00:00:00Z",
           "updated_at": "2024-01-01T00:00:00Z",
           "title": "Legacy Groups",
           "identifier": "legacy_group_category",
       }

   @pytest.fixture
   def sample_group(sample_group_type) -> dict:
       """Create a sample group for testing."""
       return {
           "id": 1,
           "created_at": "2024-01-01T00:00:00Z",
           "updated_at": "2024-01-01T00:00:00Z",
           "title": "P2P",
           "identifier": "legacy_p2p",
           "type": sample_group_type,  # Ensure this is properly passed
       }
   ```

   **Fix for the specific error in test_fetch_groups**:
   The error `Input should be a valid dictionary or instance of GroupType` occurs because the test is trying to use the fixture function directly instead of its return value. Modify the test code:

   ```python
   # In tests/test_v1_groups.py
   @pytest.fixture
   def sample_groups(sample_group) -> list[dict]:
       """Create a list of sample groups for testing."""
       # Make sure we're using the return value of sample_group, not the function itself
       return [
           sample_group,  # First group (P2P)
           {
               "id": 2,
               "created_at": "2024-01-01T00:00:00Z",
               "updated_at": "2024-01-01T00:00:00Z",
               "title": "Standard VPN",
               "identifier": "standard",
               "type": {  # Directly provide the type dictionary
                   "id": 1,
                   "created_at": "2024-01-01T00:00:00Z",
                   "updated_at": "2024-01-01T00:00:00Z",
                   "title": "Legacy Groups",
                   "identifier": "legacy_group_category",
               }
           }
       ]
   ```

2. **Update City and Country model fixtures**:
   ```python
   # In tests/test_v2_servers.py
   @pytest.fixture
   def sample_city() -> dict:
       """Create a sample city for testing."""
       return {
           "id": 1,
           "name": "New York",
           "latitude": 40.7128,
           "longitude": -74.0060,
           "dns_name": "us-nyc.nordvpn.com",
           "hub_score": 1,
           "server_count": 50  # Add the missing server_count field
       }

   @pytest.fixture
   def sample_country(sample_city) -> dict:
       """Create a sample country for testing."""
       return {
           "id": 1, 
           "name": "United States", 
           "code": "US", 
           "city": sample_city,
           "server_count": 100  # Add the missing server_count field
       }
   ```

3. **Fix the server_manager.py issue**:
   ```python
   # Current setup causing AttributeError
   # mock_api_client.get.return_value.json.return_value = [...]
   
   # Fix the AttributeError by properly mocking the API client methods
   # For example, if using NordVPNAPI class:
   mock_api_client.get_servers.return_value = [
       {
           "hostname": "tcp1.nordvpn.com",
           "status": "online",
           "load": 50,
           "country": {"code": "US", "name": "United States"},
           "technologies": [
               {"id": 5, "name": "OpenVPN TCP", "status": "online"},
           ],
       },
       # Add more sample servers as needed
   ]
   ```

   **Fix for the test_openvpn_tcp_validation failure**:
   The test shows that `_is_valid_server()` is returning `True` for servers without OpenVPN TCP. Check the implementation:

   ```python
   # In src/nyord_vpn/network/server.py
   def _is_valid_server(self, server: dict) -> bool:
       """Check if a server is valid for OpenVPN TCP connection.
       
       A valid server must:
       - Be online
       - Have a valid hostname (nordvpn.com domain)
       - Have a load between 0-100
       - Support OpenVPN TCP technology
       
       Args:
           server: Server information dictionary
           
       Returns:
           True if server is valid, False otherwise
       """
       # Add debug logging
       if self.verbose:
           self.logger.debug(f"Validating server: {server['hostname']}")
           
       # Check server status
       if server.get("status") != "online":
           if self.verbose:
               self.logger.debug(f"Server {server['hostname']} is not online")
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
           
       # Check country
       country = server.get("country", {})
       country_code = country.get("code", "")
       if not (country_code and len(country_code) == 2):
           if self.verbose:
               self.logger.debug(f"Server {hostname} has invalid country code: {country_code}")
           return False
           
       # Check for OpenVPN TCP support - THIS IS THE ISSUE
       technologies = server.get("technologies", [])
       has_openvpn_tcp = False
       for tech in technologies:
           if isinstance(tech, dict) and "name" in tech and "id" in tech:
               name = tech.get("name", "")
               # Check for both regular and dedicated OpenVPN TCP
               if "OpenVPN TCP" in name:
                   if self.verbose:
                       self.logger.debug(f"Found OpenVPN TCP support: {name}")
                   has_openvpn_tcp = True
                   break
                   
       if not has_openvpn_tcp:
           if self.verbose:
               self.logger.debug(f"Server {hostname} doesn't support OpenVPN TCP")
           # This should return False but might be returning True
           return False
           
       return True
   ```

4. **Fix the server groups issue in `test_fetch_all`**:
   ```python
   # The test is failing because server.groups is empty
   # In the sample_api_response fixture:
   
   @pytest.fixture
   def sample_api_response(sample_server, sample_group, sample_service, sample_location, sample_technology):
       """Create a sample API response for testing."""
       return {
           "servers": [sample_server],
           "groups": [sample_group],
           "services": [sample_service],
           "locations": [sample_location],
           "technologies": [sample_technology],
       }
   
   @pytest.fixture
   def sample_server(sample_location, sample_group, sample_service, sample_technology):
       """Create a sample server for testing."""
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
           # Ensure server has a groups array that references the group ID
           "groups": [{"id": 1, "pivot": {"server_id": 1, "group_id": 1}}],
           # Other server fields...
       }
   ```

5. **Update model validation to handle missing fields gracefully**:
   ```python
   # In model definitions, add default values for optional fields
   
   # For example, in src/nyord_vpn/api/v2_servers.py:
   class Group(BaseModel):
       """Server group information (e.g., P2P, Standard VPN, etc.)."""
       id: int
       created_at: datetime
       updated_at: datetime
       title: str
       identifier: str
       type: GroupType
       
       # Add model configuration for better validation handling
       class Config:
           extra = "ignore"  # Ignore extra fields
           protected_namespaces = ()  # Allow arbitrary attribute access
   
   # In src/nyord_vpn/api/v1_countries.py:
   class City(BaseModel):
       """City information."""
       id: int
       name: str
       latitude: float
       longitude: float
       dns_name: str
       hub_score: int
       server_count: int = 0  # Default value for backward compatibility
       
       class Config:
           extra = "ignore"
           protected_namespaces = ()
   
   class Country(BaseModel):
       """Country information from the v1 API."""
       id: int
       name: str
       code: str
       server_count: int = 0  # Default value for backward compatibility
       cities: list[City]
       
       class Config:
           extra = "ignore"
           protected_namespaces = ()
   ```

By implementing these changes, we'll ensure test fixtures include all required fields and fix the server groups issue in the `test_fetch_all` test. The model validation improvements will also make the code more resilient when handling API responses with missing fields.

### Improving Error Handling in client.py

To enhance error handling in the Client class, we should implement a more robust approach that provides detailed feedback and recovery options:

1. **Define an error message catalog**:
   ```python
   # At the top of the Client class
   ERROR_MESSAGES = {
       "auth_failed": {
           "message": "Authentication failed with NordVPN servers",
           "troubleshooting": [
               "Check that your username and password are correct",
               "Verify your internet connection is working",
               "Try again in a few minutes as NordVPN servers might be temporarily unavailable"
           ]
       },
       "connection_failed": {
           "message": "Failed to establish VPN connection",
           "troubleshooting": [
               "Check if OpenVPN is installed (run 'which openvpn')",
               "Verify you have sufficient permissions (try running with sudo)",
               "Try connecting to a different server or country"
           ]
       },
       "server_not_found": {
           "message": "No suitable servers found for the specified country",
           "troubleshooting": [
               "Check if the country code is valid (use list_countries to see available countries)",
               "Try a different country as servers might be temporarily unavailable",
               "Check your internet connection"
           ]
       },
       "config_error": {
           "message": "Error generating OpenVPN configuration file",
           "troubleshooting": [
               "Check if you have write permissions in the config directory",
               "Make sure there's enough disk space available",
               "Try manually clearing the cache directory and reconnecting"
           ]
       },
       "openvpn_error": {
           "message": "Error running OpenVPN",
           "troubleshooting": [
               "Verify OpenVPN is installed correctly",
               "Check system logs for OpenVPN errors",
               "Try reinstalling OpenVPN"
           ]
       }
   }
   ```

2. **Create helper methods for error handling**:
   ```python
   def _handle_error(self, error_code: str, exception: Exception = None, details: str = None) -> None:
       """Handle errors with consistent messaging and logging.
       
       Args:
           error_code: The error code key from ERROR_MESSAGES dictionary
           exception: The original exception that was caught, if any
           details: Additional details about the error
           
       Raises:
           VPNError: A structured error with troubleshooting steps
       """
       error_info = self.ERROR_MESSAGES.get(
           error_code, 
           {
               "message": "An unknown error occurred", 
               "troubleshooting": ["Check logs for more details"]
           }
       )
       
       message = error_info["message"]
       if details:
           message = f"{message}: {details}"
           
       # Log the full error with context
       if exception:
           logger.error(f"Error {error_code}: {message}", exc_info=exception)
       else:
           logger.error(f"Error {error_code}: {message}")
       
       # Raise a specific exception with troubleshooting steps
       troubleshooting = error_info.get("troubleshooting", [])
       raise VPNError(message, troubleshooting=troubleshooting)
   
   def _format_troubleshooting(self, steps: list[str]) -> str:
       """Format troubleshooting steps into a readable string.
       
       Args:
           steps: List of troubleshooting steps
           
       Returns:
           Formatted string with numbered steps
       """
       if not steps:
           return ""
           
       result = "\n\nTroubleshooting steps:\n"
       for i, step in enumerate(steps, 1):
           result += f"{i}. {step}\n"
           
       return result
   ```

3. **Implement recovery mechanisms**:
   ```python
   def _try_reconnect(self, country_code: str, max_attempts: int = 3) -> bool:
       """Attempt to reconnect to VPN after a failure.
       
       Args:
           country_code: The country code to connect to
           max_attempts: Maximum number of reconnection attempts
           
       Returns:
           True if reconnection was successful, False otherwise
       """
       for attempt in range(max_attempts):
           try:
               wait_time = 2 ** attempt  # Exponential backoff
               logger.info(f"Reconnection attempt {attempt + 1}/{max_attempts} after waiting {wait_time}s")
               
               if attempt > 0:
                   time.sleep(wait_time)  # Skip waiting on first attempt
                   
               # Try with a different server by bypassing cache
               self._connect(country_code, bypass_cache=True)
               logger.info(f"Successfully reconnected on attempt {attempt + 1}")
               return True
               
           except VPNError as e:
               logger.warning(f"Reconnection attempt {attempt + 1} failed: {e}")
       
       logger.error(f"All {max_attempts} reconnection attempts failed")
       return False
   ```

4. **Refactor the `go()` method into smaller functions**:
   ```python
   def _validate_country_code(self, country_code: str) -> None:
       """Validate that the country code is valid.
       
       Args:
           country_code: Two-letter country code to validate
           
       Raises:
           VPNError: If country code is invalid
       """
       if not country_code or not isinstance(country_code, str) or len(country_code) != 2:
           self._handle_error(
               "invalid_country", 
               details=f"Country code must be a two-letter code, got: {country_code!r}"
           )
           
       # Optionally validate against known country codes
       countries = self.list_countries()
       country_codes = [c["code"].lower() for c in countries]
       
       if country_code.lower() not in country_codes:
           self._handle_error(
               "unknown_country", 
               details=f"Country code '{country_code}' not found in available countries: {', '.join(country_codes)}"
           )
   
   def _resolve_server(self, country_code: str) -> dict:
       """Resolve a server for the given country code.
       
       Args:
           country_code: Two-letter country code
           
       Returns:
           Server information dictionary
           
       Raises:
           VPNError: If no suitable server could be found
       """
       try:
           logger.info(f"Finding optimal server for country: {country_code}")
           server = self._api.find_best_server(country_code)
           
           if not server:
               self._handle_error(
                   "server_not_found", 
                   details=f"No servers available for country: {country_code}"
               )
               
           logger.info(f"Selected server: {server['hostname']} (load: {server['load']}%)")
           return server
           
       except Exception as e:
           self._handle_error("api_error", exception=e, details=str(e))
   
   def _connect_to_server(self, server: dict) -> None:
       """Connect to the specified server.
       
       Args:
           server: Server information dictionary
           
       Raises:
           VPNError: If connection fails
       """
       try:
           hostname = server["hostname"]
           logger.info(f"Connecting to {hostname}")
           
           # Generate config
           config_path = self._generate_config(hostname)
           
           # Start OpenVPN process
           success = self._start_openvpn(config_path)
           
           if not success:
               self._handle_error(
                   "connection_failed", 
                   details=f"Failed to connect to {hostname}"
               )
               
       except Exception as e:
           self._handle_error("connection_error", exception=e, details=str(e))
   
   def _verify_connection(self) -> None:
       """Verify that the VPN connection is working properly.
       
       Raises:
           VPNError: If connection verification fails
       """
       try:
           # Check if process is still running
           if not self._is_connected():
               self._handle_error(
                   "connection_verification_failed", 
                   details="OpenVPN process is not running"
               )
               
           # Optionally check IP changes
           current_ip = self._get_current_ip()
           if current_ip == self._original_ip:
               logger.warning(f"IP address hasn't changed after connection: {current_ip}")
               
           logger.info(f"Connection verified, new IP: {current_ip}")
           
       except Exception as e:
           self._handle_error("verification_error", exception=e, details=str(e))
   
   def go(self, country_code: str, *, retry_on_failure: bool = True) -> bool:
       """Connect to VPN in the specified country.
       
       Args:
           country_code: Two-letter country code
           retry_on_failure: Whether to retry on connection failure
           
       Returns:
           True if connection was successful
           
       Raises:
           VPNError: If connection fails and retry fails or is disabled
       """
       try:
           # Record original IP for verification
           self._original_ip = self._get_current_ip()
           logger.info(f"Original IP: {self._original_ip}")
           
           # Validate country code
           self._validate_country_code(country_code)
           
           # Find a server
           server = self._resolve_server(country_code)
           
           # Connect to server
           self._connect_to_server(server)
           
           # Verify connection
           self._verify_connection()
           
           logger.info(f"Successfully connected to {country_code.upper()} using {server['hostname']}")
           return True
           
       except VPNError as e:
           logger.error(f"Connection failed: {e}")
           
           # Try recovery if enabled
           if retry_on_failure:
               logger.info("Attempting to recover from connection failure")
               if self._try_reconnect(country_code):
                   return True
           
           # Re-raise with troubleshooting steps if recovery failed or disabled
           if hasattr(e, 'troubleshooting') and e.troubleshooting:
               steps = self._format_troubleshooting(e.troubleshooting)
               raise VPNError(f"{str(e)}{steps}") from e
           else:
               raise
   ```

5. **Update the `VPNError` exception class to include troubleshooting steps**:
   ```python
   # In nyord_vpn/exceptions.py
   class VPNError(Exception):
       """Base exception for VPN-related errors.
       
       This exception includes troubleshooting steps to help users
       resolve common issues without needing technical support.
       """
       
       def __init__(self, message: str, troubleshooting: list[str] = None):
           """Initialize the exception.
           
           Args:
               message: Error message
               troubleshooting: List of troubleshooting steps
           """
           self.message = message
           self.troubleshooting = troubleshooting or []
           super().__init__(message)
   ```

6. **Update docstrings to include error handling information**:
   ```python
   def connect(self, country_code: str, *, bypass_cache: bool = False) -> bool:
       """Connect to a VPN server in the specified country.
       
       This method finds the best server in the specified country,
       generates an OpenVPN configuration, and establishes a connection.
       
       Args:
           country_code: Two-letter country code (e.g., 'us', 'de')
           bypass_cache: Whether to bypass the server cache
           
       Returns:
           True if connection was successful
           
       Raises:
           VPNError: If connection fails for any reason:
               - Authentication failure (check credentials)
               - No servers available (try a different country)
               - OpenVPN error (check if OpenVPN is installed)
               - Configuration error (check write permissions)
       """
   ```

By implementing these changes, the Client class will have significantly improved error handling with clear, actionable messages, recovery mechanisms, and well-organized code structure that separates different aspects of the connection process.