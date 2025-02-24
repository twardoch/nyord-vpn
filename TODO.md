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

After each set of changes, update @PROGRESS.md with what you've done (`- [x] `). Upgrade priorities for NEXT TODO (`- [!]`), re-think the normal TODO (`- [ ] `)

Periodically do:

```
uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]; tree -I *cache__; hatch fmt --unsafe-fixes; hatch fmt --unsafe-fixes; hatch -e test run test; 
```

and react to the results. Use `uv pip...` instead of `pip...` if needed. 

## Working modality

You'll lead two experts: "Ideot" for creative, unorthodox ideas and "Critin" to critique flawed thinking and moderate for balanced discussions. The three of you shall illuminate knowledge with concise, beautiful responses, process methodically for clear answers, collaborate step-by-step, sharing thoughts and adapting. If errors are found, step back and focus on accuracy and progress.

Independently tackle challenges systematically, being adaptable and resourceful. Research deeply using all tools, revising to ensure conclusive, exhaustive, insightful results. When you're finished, print "Wait, but" to go back, think & reflect, revise & improvement what you've done (but don't invent functionality freely). Repeat this. Focus on minimal viable next versions of the code. Ship often and early. 

## General coding principles

Verify info. No assumptions. No apologies. No major invented changes. No unneeded confirmations or checks. Keep existing code and structures unless they need to change. No unnecessary updates or current implementation discussion. Avoid magic numbers, handle edge cases, use assertions to validate assumptions and catch potential errors early.

Every code can fail. Write code that fails gracefully and is UX friendly: uses retries (within reason), does not make stupid assumptions, tests successes, uses fallbacks and backoffs, and then, if the code needs to message the user, be clear and suggest to the user the next steps. Don't prompt the user to do something that the computer can obviously do. The code should ask the user only if there is a real decision to be made. And you should ask me only if a real decision is needed.  

## Keep track of paths

In every source file you create or edit, always maintain the up-to-date `this_file` record that shows the path of the current file relative to the root of the project. Place the `this_file` record near the top of the file, as a comment after the shebangs, or in the YAML Markdown frontmatter. Use these records for orientation. 

## Follow this style for Python

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

# Nyord VPN Codebase Refactoring Specification

## Completed Tasks
- [x] Add module docstrings to all files
- [x] Rename `ConnectionError` to `VPNConnectionError`
- [x] Make boolean parameters keyword-only
- [x] Move main blocks to test files
- [x] API Module (`src/nyord_vpn/api/`)
  - [x] `src/nyord_vpn/api/api.py`: Implement central API interface
  - [x] `src/nyord_vpn/api/v1_*.py`: Add deprecation notices and clean up
  - [x] `src/nyord_vpn/api/v2_servers.py`: Fix linting and improve type hints
- [x] Core Module - Initial cleanup
  - [x] `src/nyord_vpn/core/api.py` and `src/nyord_vpn/core/base.py`: Add deprecation warnings
- [x] Network Module - `vpn_commands.py`
  - [x] Create `OpenVPNConfig` dataclass with proper validation
  - [x] Implement `get_openvpn_command` function with proper validation
- [x] Network Module - `server.py`
  - [x] Replace random module with secrets module for secure randomization
  - [x] Fix type compatibility issues in server.py
  - [x] Address security issues in subprocess calls by validating input
  - [x] Add comprehensive type hints for functions and variables
- [x] Core Module (`src/nyord_vpn/core/`)
  - [x] `src/nyord_vpn/core/client.py`: Update to use the new `NordVPNAPI` class

## Remaining Tasks (Prioritized)

### High Priority Items

#### Core Module (`src/nyord_vpn/core/`)

##### `src/nyord_vpn/core/client.py`

**Action**: Continue refactoring to improve quality.

- [!] Improve error handling and user feedback
  - [!] Add more detailed error messages with troubleshooting steps
  - [!] Implement proper exception handling with specific exception types
  - [!] Add recovery suggestions in error messages
- [!] Break down complex methods into smaller helper functions
  - [!] Refactor the `go()` method into smaller functions for each step
  - [!] Extract connection validation logic into separate functions
  - [!] Create helper functions for environment variable handling
- [!] Fix boolean arguments and other linting issues
  - [!] Make all boolean parameters keyword-only arguments
  - [!] Fix type annotations for better static analysis
  - [!] Add proper validation for function parameters

### Medium Priority Items

#### Network Module (`src/nyord_vpn/network/`)

##### `src/nyord_vpn/network/vpn.py`

**Action**: Refactor for better maintainability.

- [!] Make boolean arguments keyword-only
- [!] Add comprehensive type hints for all functions and methods
- [ ] Implement retry logic for connection attempts with tenacity
- [ ] Break down complex methods:
  - [ ] Split `setup_connection()` into smaller focused functions
  - [ ] Refactor `connect()` method to improve readability
  - [ ] Extract IP validation logic into a utility function
- [ ] Replace random.uniform with secrets.SystemRandom().uniform for better security
- [ ] Improve error handling with specific exception types and recovery mechanisms

#### Tests

**Action**: Update to reflect code changes.

- [!] Fix import error in `tests/test_client.py` (change import from nyord_vpn.core.exceptions to nyord_vpn.exceptions)
- [!] Update test fixtures to include missing fields:
  - Add `type` field to Group model in test fixtures
  - Add `server_count` field to Country and City models in test fixtures 
- [!] Fix validation errors in models and tests:
  - Fix test mocks to have all required fields in API responses
  - Update model validation to handle missing fields gracefully
  - Fix server filtering test failures in test_v2_servers.py
- [!] Fix mock setup in `tests/test_server_manager.py` (AttributeError: Mock object has no attribute 'get')
- [ ] Update imports to use `VPNConnectionError` instead of `ConnectionError`
- [ ] Fix test failures in integration tests

### Lower Priority Items

#### Utils Module (`src/nyord_vpn/utils/`)

##### `src/nyord_vpn/utils/templates.py`

**Action**: Simplify with tenacity.

- [!] Fix security vulnerabilities in subprocess calls (S603, S607)
- [!] Replace datetime.now() and datetime.fromtimestamp() with timezone-aware versions (DTZ005, DTZ006)
- [!] Fix exception handling issues:
  - Replace long error messages with proper exception classes (TRY003)
  - Use `raise ... from err` consistently (B904)
  - Move try/except out of loops for better performance (PERF203)
  - Use `else` blocks appropriately after try/except (TRY300)
- [ ] Implement retry logic with tenacity for network operations
- [ ] Break down complex functions into smaller ones
- [ ] Improve docstrings and type hints
- [ ] Add more detailed logging for debugging purposes
- [ ] Replace random module usage with secrets module (S311)

##### `src/nyord_vpn/utils/utils.py`

**Action**: Update file handling and security.

- [!] Replace os.path functions with pathlib equivalents (PTH110, PTH118, PTH123)
- [!] Fix security vulnerability in subprocess call (S603)
- [!] Fix error handling to use `else` blocks appropriately (TRY300)
- [ ] Implement atomic file operations for state management
- [ ] Add better error handling for file operations
- [ ] Improve type annotations and docstrings

#### Main Module Files

##### `src/nyord_vpn/__main__.py`

**Action**: Update to use new API.

- [!] Update CLI class to use the updated Client API
  - [!] Replace any usage of deprecated classes/methods with their updated counterparts
  - [!] Update command-line arguments to match new API structure
  - [!] Ensure all commands use the new Client implementation
- [!] Improve error handling and user feedback
  - [!] Add specific error handling for common user errors (e.g., invalid credentials, connection failures)
  - [!] Provide clear, actionable error messages with recovery steps
  - [!] Add verbose output mode for troubleshooting
- [ ] Add more detailed help messages and documentation
  - [ ] Enhance command-line help with examples and parameter descriptions
  - [ ] Add context-specific help for each command
  - [ ] Include version information and system requirements
- [ ] Implement command auto-completion for better user experience
  - [ ] Add shell completion scripts (Bash, Zsh, Fish)
  - [ ] Provide dynamic completion for country/server names
  - [ ] Document how to enable command completion

#### Documentation

**Action**: Update documentation.

- [!] Update README.md with installation and usage instructions
  - [!] Add clear step-by-step installation guide for different platforms
  - [!] Include dependency installation instructions
  - [!] Update usage examples with the new API
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

Based on the prioritized tasks, the immediate next steps should be:

1. **Improve error handling in client.py**
   - Add structured error message catalog with troubleshooting steps
   - Create helper methods for consistent error handling
   - Implement recovery mechanisms with exponential backoff
   - Refactor the `go()` method into smaller, focused functions:
     - `_validate_country_code()`
     - `_resolve_server()`
     - `_connect_to_server()`
     - `_verify_connection()`
   - Update the `VPNError` exception to include troubleshooting steps
   - Update method docstrings with error handling information

2. **Fix test fixtures**
   - Update `sample_group_type` and `sample_group` fixtures to properly handle the type reference
   - Add `server_count` field to `sample_city` and `sample_country` fixtures
   - Fix the server groups issue in the `test_fetch_all` test by ensuring server objects have proper group references
   - Update the mock setup in `test_server_manager.py` to correctly mock the API methods
   - Add model configuration for better validation handling with `Config` class

3. **Make boolean arguments keyword-only in vpn.py**
   - Update function signatures to use the `*` parameter separator
   - Update all function calls to use keyword arguments
   - Add proper validation for boolean parameters
   - Update docstrings to clarify which parameters are keyword-only

4. **Fix security vulnerabilities in templates.py**
   - Replace subprocess calls with safer alternatives by properly escaping input
   - Fix datetime timezone issues by using timezone-aware versions
   - Improve exception handling with `raise ... from err`
   - Move try/except blocks out of loops for better performance
   - Add proper `else` blocks after try/except where appropriate

These tasks should be implemented in the order presented for maximum impact on code quality and stability.

## Implementation Notes

### Improving Error Handling in client.py

The following approach is recommended for improving error handling in the Client class:

1. **Define structured error messages**:
   ```python
   ERROR_MESSAGES = {
       "auth_failed": {
           "message": "Authentication failed with NordVPN servers",
           "troubleshooting": [
               "Check that your username and password are correct",
               "Verify your internet connection",
               "Try again in a few minutes"
           ]
       },
       "connection_failed": {
           "message": "Failed to establish VPN connection",
           "troubleshooting": [
               "Check if OpenVPN is installed",
               "Verify you have sufficient permissions",
               "Try connecting to a different server"
           ]
       },
       # Add more structured error messages
   }
   ```

2. **Create helper functions for error handling**:
   ```python
   def _handle_error(self, error_code: str, details: str = None) -> None:
       """Handle errors with consistent messaging and logging."""
       error_info = self.ERROR_MESSAGES.get(error_code, {"message": "An unknown error occurred"})
       message = error_info["message"]
       if details:
           message = f"{message}: {details}"
           
       # Log the error
       logger.error(f"Error {error_code}: {message}")
       
       # Raise a specific exception with troubleshooting steps
       troubleshooting = error_info.get("troubleshooting", [])
       raise VPNError(message, troubleshooting=troubleshooting)
   ```

3. **Add recovery mechanisms**:
   ```python
   def _try_reconnect(self, country_code: str, max_attempts: int = 3) -> bool:
       """Attempt to reconnect to VPN after a failure."""
       for attempt in range(max_attempts):
           try:
               logger.info(f"Reconnection attempt {attempt + 1}/{max_attempts}")
               # Try with a different server
               self._connect(country_code, bypass_cache=True)
               return True
           except VPNError as e:
               logger.warning(f"Reconnection attempt {attempt + 1} failed: {e}")
               time.sleep(2 ** attempt)  # Exponential backoff
       
       return False
   ```

4. **Break down the `go()` method**:
   ```python
   def go(self, country_code: str) -> None:
       """Connect to VPN in specified country."""
       try:
           # Validate country code
           self._validate_country_code(country_code)
           
           # Resolve server for country
           server = self._resolve_server(country_code)
           
           # Connect to server
           self._connect_to_server(server)
           
           # Verify connection
           self._verify_connection()
           
       except VPNError as e:
           # Try recovery based on error type
           if self._try_recovery(e, country_code):
               logger.info("Recovery successful")
           else:
               raise  # Re-raise if recovery failed
   ```

5. **Update docstrings to include error handling information**:
   ```python
   def disconnect(self) -> None:
       """Disconnect from VPN.
       
       Terminates all OpenVPN processes and cleans up connection state.
       
       Raises:
           VPNError: If disconnection fails (e.g., process termination issues).
               Check if OpenVPN processes are still running manually.
       """
   ```

By implementing these changes, the client.py module will have significantly improved error handling with clear messages, recovery options, and better guidance for users.

