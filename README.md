# nyord-vpn: Your Simple and Reliable NordVPN Client

**nyord-vpn** is a Python-based command-line tool and library designed to provide straightforward and effective management of NordVPN connections on macOS. It leverages OpenVPN for robust and secure connections, and interacts with the latest NordVPN APIs to fetch server information.

## Who is this for?

*   **macOS Users:** Specifically tailored for users on macOS who prefer managing their VPN via the command line.
*   **Python Developers:** Offers a simple programmatic API to integrate NordVPN functionalities into Python scripts and applications.
*   **Privacy-Conscious Individuals:** Anyone looking for a reliable way to secure their internet connection through NordVPN with an open-source client.

## Why use nyord-vpn?

*   **Simplicity:** Easy-to-understand commands and a clean interface.
*   **Reliability:** Uses robust OpenVPN protocols and fetches up-to-date server information from NordVPN's official APIs.
*   **Control:** Connect to specific countries with ease.
*   **Transparency:** Open-source, allowing you to inspect the code.
*   **Status Monitoring:** Quickly check your connection status, current IP, and connected server.
*   **Clear Error Handling:** Informative error messages to help troubleshoot issues.
*   **Lightweight:** Minimal dependencies for a swift setup.

## Installation

### System Requirements

*   **macOS:** Currently, nyord-vpn is optimized for macOS.
*   **OpenVPN:** Required for establishing VPN connections.

### 1. Install OpenVPN

If you don't have OpenVPN installed, you can easily install it using [Homebrew](https://brew.sh/):

```bash
brew install openvpn
```

### 2. Install nyord-vpn

Install `nyord-vpn` using pip:

```bash
pip install nyord-vpn
```

## Configuration

Before using `nyord-vpn`, you must set your NordVPN credentials as environment variables. This is a secure way to provide your credentials without hardcoding them into scripts.

Open your terminal and run:

```bash
export NORD_USER="your_nordvpn_username"
export NORD_PASSWORD="your_nordvpn_password"
```

Replace `"your_nordvpn_username"` and `"your_nordvpn_password"` with your actual NordVPN login details. To make these variables permanent, add these lines to your shell's configuration file (e.g., `~/.zshrc`, `~/.bash_profile`, or `~/.bashrc`) and then source the file (e.g., `source ~/.zshrc`).

## Usage

`nyord-vpn` can be used directly from your terminal (CLI) or imported as a module in your Python scripts.

### Command-Line Interface (CLI)

Here are the primary commands:

*   **Connect to a VPN server:**
    ```bash
    nyord-vpn go <country_code>
    ```
    Replace `<country_code>` with the two-letter code of the country you want to connect to (e.g., `US` for United States, `NL` for Netherlands).
    *Example:* `nyord-vpn go JP`

*   **Connect with verbose logging (for debugging):**
    ```bash
    nyord-vpn --verbose go <country_code>
    ```
    *Example:* `nyord-vpn --verbose go DE`

*   **Get connection status:**
    Displays your current IP address, connection status, and connected server (if any).
    ```bash
    nyord-vpn info
    ```

*   **List available countries:**
    Shows a list of all countries with NordVPN servers that you can connect to.
    ```bash
    nyord-vpn list-countries
    ```

*   **Disconnect from VPN:**
    ```bash
    nyord-vpn bye
    ```

**Note on Permissions:** Connecting and disconnecting the VPN often requires administrative privileges to manage network interfaces and routing. `nyord-vpn` will automatically attempt to use `sudo` if necessary, and you may be prompted to enter your system password.

### Programmatic Usage (Python API)

You can integrate `nyord-vpn` into your Python projects for automated VPN management.

```python
import os
import sys
from nyord_vpn.core.client import Client
from nyord_vpn.exceptions import VPNError

# Ensure NORD_USER and NORD_PASSWORD are set as environment variables
# These can be loaded from a .env file using python-dotenv if preferred for development
username = os.getenv("NORD_USER")
password = os.getenv("NORD_PASSWORD")

if not username or not password:
    print("Error: NORD_USER and NORD_PASSWORD environment variables must be set.")
    print("Please set them before running the script, e.g.:")
    print("  export NORD_USER=\"your_username\"")
    print("  export NORD_PASSWORD=\"your_password\"")
    sys.exit(1)

try:
    # Initialize the client
    # Pass verbose=True for detailed logging during development or troubleshooting
    vpn_client = Client(username_str=username, password_str=password, verbose=False)

    # Optional: Initialize client environment (checks OpenVPN, API, creates dirs)
    # Recommended for first run or to ensure setup is correct.
    # vpn_client.init() # Currently, init() is more for internal setup validation.

    # Connect to a VPN server in a specific country (e.g., Netherlands)
    country_to_connect = "NL"  # Use a two-letter country code
    print(f"Attempting to connect to VPN in {country_to_connect}...")
    vpn_client.go(country_to_connect)

    # Check connection status
    current_status = vpn_client.status()
    print("\nConnection Status:")
    print(f"  Connected: {current_status.get('connected')}")
    print(f"  Current IP: {current_status.get('ip')}")
    print(f"  Server: {current_status.get('server')}")
    print(f"  Country: {current_status.get('country')}")

    # Keep the connection active for a while (e.g., for some tasks)
    if current_status.get('connected'):
        print("\nVPN connection is active. Performing some tasks...")
        # import time
        # time.sleep(30) # Example: keep VPN active for 30 seconds

    # Disconnect from VPN
    print("\nAttempting to disconnect from VPN...")
    vpn_client.bye()

    status_after_disconnect = vpn_client.status()
    print("\nStatus after disconnection:")
    print(f"  Connected: {status_after_disconnect.get('connected')}")
    print(f"  IP after disconnect: {status_after_disconnect.get('ip')}")

except VPNError as e:
    print(f"\nA VPN-related error occurred: {e}")
except Exception as e:
    # Catch any other unexpected errors
    print(f"\nAn unexpected error occurred: {e}")

```

When using the Python API, ensure that the script has the necessary permissions if it invokes operations that require `sudo` (like connecting/disconnecting). Running the Python script with `sudo python your_script.py` might be necessary in some environments if not handled internally by `nyord-vpn`'s subprocess calls that use `sudo`.

---

## Technical Deep Dive

This section provides a more detailed look into how `nyord-vpn` works internally and guidelines for contributors.

### How the Code Works

`nyord-vpn` is structured into several core components that work together to manage VPN connections:

*   **`src/nyord_vpn/__main__.py` (CLI Entry Point):**
    *   Uses the `python-fire` library to create an intuitive command-line interface.
    *   Parses CLI arguments and commands (e.g., `go`, `bye`, `info`, `list-countries`).
    *   Initializes and calls methods on the `Client` class from `core/client.py`.
    *   Handles loading of NordVPN credentials from environment variables (`NORD_USER`, `NORD_PASSWORD`).
    *   Provides user feedback via the `rich` library for formatted console output.

*   **`src/nyord_vpn/core/client.py` (Main Orchestrator):**
    *   The `Client` class is the central hub of `nyord-vpn`.
    *   It initializes and coordinates actions between the API, server selection, and VPN connection management modules.
    *   **Key responsibilities:**
        *   Managing user credentials.
        *   Orchestrating the connection (`go`) and disconnection (`bye`) flows.
        *   Providing connection status (`info`, `status`).
        *   Listing available countries (`list_countries`).
        *   Configuring logging using `loguru`.

*   **`src/nyord_vpn/api/api.py` (NordVPN API Interaction):**
    *   The `NordVPNAPI` class is responsible for all communication with NordVPN's backend services.
    *   It primarily utilizes the NordVPN v2 API (via `src/nyord_vpn/api/v2_servers.py`) to:
        *   Fetch lists of available servers, their capabilities, locations, and current load.
        *   Retrieve country information.
    *   Implements instance-level caching for API responses to reduce redundant calls and improve performance.

*   **`src/nyord_vpn/network/server.py` (Server Selection Logic):**
    *   The `ServerManager` class uses data obtained by `NordVPNAPI`.
    *   Its main function is to select the most suitable VPN server based on specified criteria, such as:
        *   Target country.
        *   Server load (preferring less loaded servers for better performance).
        *   Specific server technologies or groups (though primarily focuses on standard OpenVPN connections).

*   **`src/nyord_vpn/network/vpn.py` (VPN Connection Management):**
    *   The `VPNConnectionManager` class is the workhorse for handling the OpenVPN connection itself.
    *   **Core tasks include:**
        *   Locating and verifying the OpenVPN executable on the system.
        *   Dynamically finding the appropriate `.ovpn` configuration file for the selected NordVPN server. These configuration files are typically sourced from NordVPN's recommendations and might be packaged or downloaded. (The tool uses pre-downloaded configs that are stored within the package, specifically referenced by `src/nyord_vpn/utils/templates.py` which helps locate them).
        *   Securely writing a temporary authentication file (`openvpn.auth`) containing the user's NordVPN credentials for OpenVPN to use. This file is strictly permissioned and cleaned up.
        *   Constructing the precise OpenVPN command-line arguments using details from `src/nyord_vpn/network/vpn_commands.py`.
        *   Launching and managing the OpenVPN subprocess. This often requires `sudo` privileges for network interface manipulation, which the tool handles.
        *   Monitoring the OpenVPN process and its log file (`openvpn.log`) for connection status (e.g., "Initialization Sequence Completed").
        *   Checking the system's current public IP address using external services (like `api.ipify.org`) to verify connection success and changes.
        *   Gracefully terminating the OpenVPN process during disconnection.
        *   Cleaning up temporary files (auth file, log file).

*   **`src/nyord_vpn/exceptions.py` (Custom Error Handling):**
    *   Defines a hierarchy of custom exceptions (e.g., `VPNError`, `VPNAPIError`, `VPNConfigError`, `VPNConnectionError`).
    *   This allows for more specific error handling and clearer feedback to the user when things go wrong.

*   **`src/nyord_vpn/storage/state.py` (Connection State Persistence):**
    *   Manages saving and loading the VPN connection state to/from a JSON file (e.g., `vpn_state.json`) located in a user-specific cache directory (`~/.cache/nyord-vpn/`).
    *   The state can include information like the last connected server, current IP, connection status, and timestamps. This helps in resuming or understanding the previous state.

*   **`src/nyord_vpn/utils/` (Utilities):**
    *   `connection.py`: Contains functions for network-related tasks, primarily checking the current public IP address.
    *   `templates.py`: This module is crucial for finding and providing paths to the OpenVPN configuration (`.ovpn`) files. `nyord-vpn` bundles these configuration files within its package, and this utility helps in accessing them based on the selected server.
    *   `utils.py`: Provides general helper functions, such as:
        *   Setting up cache and configuration directories (`~/.cache/nyord-vpn/`, `~/.config/nyord-vpn/`).
        *   Functions for checking if the script is run as root (`sudo`).

#### Typical Workflow Example: `nyord-vpn go US`

1.  **CLI Parsing (`__main__.py`):** The command `go` with argument `US` is parsed. Environment variables `NORD_USER` and `NORD_PASSWORD` are checked.
2.  **Client Instantiation (`core/client.py`):** A `Client` object is created. `NordVPNAPI`, `ServerManager`, and `VPNConnectionManager` are initialized.
3.  **`Client.go("US")` Invoked:**
    a.  The client checks if already connected. If so, it calls `VPNConnectionManager.disconnect()` first.
    b.  `ServerManager.select_fastest_server("US")` is called. This internally uses `NordVPNAPI` to fetch all servers, then filters them for the "US" country and selects one with low load.
    c.  `VPNConnectionManager.setup_connection(selected_server, username, password)` is called:
        i.  The path to the OpenVPN configuration file for `selected_server` is determined using `utils/templates.py`.
        ii. Securely writes credentials to `~/.cache/nyord-vpn/openvpn.auth`.
    d.  `VPNConnectionManager.connect([selected_server])` is called:
        i.  The OpenVPN command is constructed (e.g., `sudo openvpn --config <path_to_ovpn> --auth-user-pass <path_to_auth_file> ...`).
        ii. The OpenVPN subprocess is started.
    e.  The client monitors the connection, waits for OpenVPN to establish it, and verifies the new public IP.
4.  **Feedback:** The CLI displays the connection status (IP address, server name).

### Coding and Contribution Guidelines

We welcome contributions to `nyord-vpn`! Please follow these guidelines:

*   **Code Style:**
    *   This project uses **Black** for uncompromising code formatting and **Ruff** (as a linter, configured in `pyproject.toml`) to enforce code style and catch errors.
    *   Please ensure your code is formatted with Black before committing.
    *   Run `ruff check .` and `ruff format .` to check and format your code.

*   **Pre-commit Hooks:**
    *   The repository is configured with pre-commit hooks (see `.pre-commit-config.yaml`). These hooks automatically run tools like Black and Ruff when you commit changes.
    *   Install pre-commit hooks locally in your cloned repository:
        ```bash
        pip install pre-commit
        pre-commit install
        ```
    *   Now, formatting and linting checks will run automatically on `git commit`.

*   **Testing:**
    *   Tests are written using `pytest` and are located in the `tests/` directory.
    *   Contributions, especially new features or bug fixes, should ideally include relevant tests.
    *   Run tests with:
        ```bash
        pytest
        ```

*   **Dependencies:**
    *   Project dependencies are managed using `Poetry` (see `pyproject.toml` and `poetry.lock`).
    *   If you add a new dependency, use `poetry add <package_name>`.

*   **Logging:**
    *   `loguru` is used for application logging. It provides a more pleasant and powerful logging experience than the standard `logging` module.
    *   Use the global `logger` instance available in most modules.
    *   Leverage the `--verbose` CLI flag, which sets the log level to DEBUG for more detailed output.

*   **Error Handling:**
    *   Use the custom exceptions defined in `src/nyord_vpn/exceptions.py` where appropriate.
    *   Aim to provide clear and actionable error messages to the user.

*   **Development Setup:**
    1.  Fork and clone the repository:
        ```bash
        git clone https://github.com/your-username/nyord-vpn.git
        cd nyord-vpn
        ```
    2.  It's highly recommended to use a virtual environment. If you have Poetry installed:
        ```bash
        poetry install --with dev  # Installs main and development dependencies
        poetry shell             # Activates the virtual environment
        ```
    3.  If you prefer pip and `venv`:
        ```bash
        python -m venv venv
        source venv/bin/activate
        pip install -e .[dev] # Installs the package in editable mode with dev dependencies
        ```
        *(Note: The `.[dev]` extra needs to be defined in `pyproject.toml` under `[project.optional-dependencies]` for this pip command to work. If not using Poetry directly, ensure you install development requirements, e.g., from a `requirements-dev.txt` if available, or manually install `pytest`, `black`, `ruff`, `pre-commit`)*

*   **Commit Messages:**
    *   While not strictly enforced, consider following [Conventional Commits](https://www.conventionalcommits.org/) guidelines for commit messages (e.g., `feat: add new country listing feature`, `fix: resolve connection timeout issue`). This helps in generating changelogs and understanding project history.

*   **Pull Requests (PRs):**
    *   Submit PRs to the `main` branch (or the relevant development branch if specified).
    *   Ensure your PR includes:
        *   A clear description of the changes made.
        *   Reasons for the change.
        *   Reference to any related issues.
    *   Ensure all tests pass and linting checks (Black, Ruff via pre-commit) are clean before submitting.
    *   Keep PRs focused on a single issue or feature where possible.

## License

nyord-vpn is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
