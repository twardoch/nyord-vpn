## SpecStory

## Analyzing nyord-vpn CLI Issues (25/02/2025, 01:03:31)

_**User**_

@VIBE.txt 

---

_**Assistant**_

<think>I am being asked to look at the VIBE.txt file that was attached to the conversation. This file contains the outputs of several `nyord-vpn` commands, which appears to be a CLI tool for managing VPN connections, possibly related to NordVPN given the name.

Let's analyze the content of the file:

1. `sudo nyord-vpn info --verbose` shows:
   - Debug info about OpenVPN being found at `/usr/local/sbin/openvpn`
   - Creation of auth file at `/Users/adam/.cache/nyord-vpn/openvpn.auth`
   - IP checking via api.ipify.org
   - Current status: "Not Connected" with public IP 89.64.28.48

2. `sudo nyord-vpn --help` and just `sudo nyord-vpn` show the CLI help information:
   - It's a NordVPN CLI interface
   - Has groups like `client`
   - Has commands like `bye`, `go`, `info`, and `update`

3. `sudo nyord-vpn update` shows:
   - Successfully updated country information

4. `sudo nyord-vpn go de --verbose` shows:
   - Several errors related to Pydantic field validation (missing required fields)
   - A warning about failing to get the fastest server from the API and falling back to cache
   - A final error: "Failed to connect: Failed to select server: [Errno 2] No such file or directory: 'ping'"

The main issue appears to be that the `go` command, which tries to connect to a VPN server in Germany (`de`), is failing. The error suggests that the `ping` command is not found, which is unusual since `ping` is a standard command on most systems.

I should explore the project structure to better understand the code and potentially suggest a fix for this issue.

Let's start by exploring the project structure.</think>I see you've shared the outputs from the `nyord-vpn` CLI tool. Let me analyze what's happening here based on the terminal outputs.

The tool appears to be a NordVPN CLI interface with several issues:

1. **Basic functionality appears to work:**
   - The info command shows current VPN status (not connected)
   - The help command shows available commands (go, bye, info, update)
   - The update command successfully updates country information

2. **The critical issue is with the connection command:**
   - When attempting `nyord-vpn go de` (connect to Germany), the command fails
   - There are multiple errors:
     - Pydantic validation errors (missing required fields like 'created_at')
     - Fallback to cache after API failure
     - Final error: `[Errno 2] No such file or directory: 'ping'`

Let me explore the codebase to understand how the tool is structured and how to fix these issues.

---

_****_

<details>
            <summary>Listed current directory • **27** results</summary>
        
| Name |
|-------|
| 📄 `VIBE.txt` |
| 📁 `.venv` |
| 📄 `TODO.md` |
| 📄 `PROGRESS.md` |
| 📁 `.git` |
| 📄 `CLEANUP.txt` |
| 📄 `nyord_vpn.txt` |
| 📁 `src` |
| 📄 `cleanup.py` |
| 📄 `.DS_Store` |
| 📁 `.pytest_cache` |
| 📁 `tests` |
| 📁 `_private` |
| 📁 `.specstory` |
| 📁 `.ruff_cache` |
| 📄 `pyproject.toml` |
| 📄 `uv.lock` |
| 📁 `.idea` |
| 📁 `build` |
| 📄 `README.md` |
| 📁 `.cursor` |
| 📄 `package.toml` |
| 📁 `.github` |
| 📁 `dist` |
| 📄 `.pre-commit-config.yaml` |
| 📄 `LICENSE` |
| 📄 `.gitignore` |

</details>

---

_****_



Let's check the source code directory structure:

---

_****_

<details>
            <summary>Listed directory src • **4** results</summary>
        
| Name |
|-------|
| 📁 `nyord_vpn.egg-info` |
| 📄 `.DS_Store` |
| 📁 `nyord_vpn` |
| 📄 `__init__.py` |

</details>

---

_****_



Now let's check the main package contents:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn • **12** results</summary>
        
| Name |
|-------|
| 📁 `__pycache__` |
| 📄 `exceptions.py` |
| 📄 `__init__.py` |
| 📄 `.DS_Store` |
| 📁 `api` |
| 📁 `utils` |
| 📁 `network` |
| 📁 `data` |
| 📁 `core` |
| 📁 `scripts` |
| 📁 `storage` |
| 📄 `__main__.py` |

</details>

---

_****_





I need to locate where the `ping` command is used and understand the VPN connection process. Let's check the network module:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/network • **7** results</summary>
        
| Name |
|-------|
| 📁 `__pycache__` |
| 📄 `server.py` |
| 📄 `vpn_commands.py` |
| 📄 `vpn.py` |
| 📄 `.DS_Store` |
| 📄 `__init__.py` |
| 📄 `country.py` |

</details>

---

_****_





From the error message, we can see that the issue is related to the `ping` command not being found. Let's look at the server.py file since the error occurs during server selection:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





Now let's look at the ping function:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



Let's see the rest of the ping function:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





Let's see the rest of the ping function and how it processes the results:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_







Let's see the final part of the ping function to complete our understanding:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





Let's see the error handling in case of ping failure:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





Now I need to check the main script or module to understand how the command line interface is set up:

---

_****_

Read file: src/nyord_vpn/__main__.py

---

_****_







Let's look at the rest of the __main__.py file to understand how commands are implemented:

---

_****_

Read file: src/nyord_vpn/__main__.py

---

_****_







Let's check the remaining part of __main__.py:

---

_****_

Read file: src/nyord_vpn/__main__.py

---

_****_







Let me examine how the Client class is implemented, especially the `go` method:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/core • **6** results</summary>
        
| Name |
|-------|
| 📁 `__pycache__` |
| 📄 `client.py` |
| 📄 `.DS_Store` |
| 📄 `base.py` |
| 📄 `api.py` |
| 📄 `__init__.py` |

</details>

---

_****_









Let's look at the Client class:

---

_****_

Read file: src/nyord_vpn/core/client.py

---

_****_







Let's see the Client.go() method which is failing:

---

_****_

Read file: src/nyord_vpn/core/client.py

---

_****_









Now I need to check the rest of the go method:

---

_****_

Read file: src/nyord_vpn/core/client.py

---

_****_







Let's now check how `ping` is installed in the pyproject.toml file:

---

_****_

Read file: pyproject.toml

---

_****_







Based on all the investigation, I can now understand the issue. The problem is that the `nyord-vpn` tool is trying to use the `ping` command during server selection, but it's not finding the command. This is evident from the error message: `[Errno 2] No such file or directory: 'ping'`.

Let's solve this by modifying the server.py file to add a fallback mechanism when `ping` is not available. Here's my fix:

---

_****_

```diff
  import secrets
  import re
+ import os
  from typing import Any, TypedDict, NotRequired, cast
  
          """
          try:
+             # First check if ping is available
+             ping_path = self._check_for_ping_command()
+             if not ping_path:
+                 self.logger.warning("Ping command not found, using fallback method")
+                 return self._fallback_ping(hostname)
+                 
              # Platform-specific ping command
              system = platform.system().lower()
              # Construct command based on platform with proper escaping
              if system == "windows":
-                 cmd = ["ping", "-n", "2", "-w", "1000", hostname]
+                 cmd = [ping_path, "-n", "2", "-w", "1000", hostname]
              elif system == "darwin":  # macOS
-                 cmd = ["ping", "-c", "2", "-W", "1", "-t", "1", hostname]
+                 cmd = [ping_path, "-c", "2", "-W", "1", "-t", "1", hostname]
              else:  # Linux and others
-                 cmd = ["ping", "-c", "2", "-W", "1", hostname]
+                 cmd = [ping_path, "-c", "2", "-W", "1", hostname]
  
              # Log the command if in verbose mode
                  self.logger.debug(f"Error pinging {hostname}: {e}")
              return float("inf")
+         except FileNotFoundError:
+             # This should be caught by the initial check, but just in case
+             self.logger.warning("Ping command not found during execution, using fallback method")
+             return self._fallback_ping(hostname)
+ 
+     def _check_for_ping_command(self) -> str:
+         """Check if ping command is available and return its path if found.
+         
+         Returns:
+             str: Path to ping command, or empty string if not found
+         """
+         try:
+             # Try to find ping in common locations
+             common_paths = [
+                 "/bin/ping",
+                 "/sbin/ping",
+                 "/usr/bin/ping", 
+                 "/usr/sbin/ping",
+                 "/usr/local/bin/ping",
+                 "/usr/local/sbin/ping"
+             ]
+             
+             # First check if ping is in PATH
+             try:
+                 result = subprocess.run(
+                     ["which", "ping"], 
+                     capture_output=True, 
+                     text=True, 
+                     check=False
+                 )
+                 if result.returncode == 0 and result.stdout.strip():
+                     return result.stdout.strip()
+             except (subprocess.SubprocessError, FileNotFoundError):
+                 pass
+                 
+             # Check common locations
+             for path in common_paths:
+                 if os.path.exists(path) and os.access(path, os.X_OK):
+                     return path
+                     
+             return ""
+         except Exception as e:
+             self.logger.warning(f"Error checking for ping command: {e}")
+             return ""
+             
+     def _fallback_ping(self, hostname: str) -> float:
+         """Fallback method when ping command is not available.
+         Uses socket connection to estimate latency.
+         
+         Args:
+             hostname: Server hostname to ping
+             
+         Returns:
+             float: Estimated ping time in milliseconds, or float('inf') if failed
+         """
+         try:
+             if self.verbose:
+                 self.logger.debug(f"Using socket fallback to ping {hostname}")
+                 
+             import socket
+             import time
+             
+             # Validate hostname
+             if not self._is_valid_hostname(hostname):
+                 self.logger.warning(f"Invalid hostname format: {hostname}")
+                 return float("inf")
+                 
+             # We'll make a TCP connection to port 443 (HTTPS) as most servers will have this open
+             start_time = time.time()
+             
+             # Try to establish TCP connection
+             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+             s.settimeout(2.0)  # 2 second timeout
+             try:
+                 s.connect((hostname, 443))
+                 s.shutdown(socket.SHUT_RDWR)
+                 end_time = time.time()
+                 time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
+                 
+                 if self.verbose:
+                     self.logger.debug(f"Socket connection to {hostname}:443 took {time_ms:.2f}ms")
+                 
+                 return time_ms
+             except (socket.timeout, socket.error) as e:
+                 if self.verbose:
+                     self.logger.debug(f"Socket connection to {hostname} failed: {e}")
+                 return float("inf")
+             finally:
+                 s.close()
+                 
+         except Exception as e:
+             self.logger.warning(f"Fallback ping to {hostname} failed: {e}")
+             return float("inf")
  
      def _is_valid_server(self, server: Any) -> bool:
```

---

_****_



Now, let's add a small improvement to the fallback method to also check if the "which" command might be missing:

---

_****_

```diff
              ]
              
-             # First check if ping is in PATH
+             # First try to use 'which' to find ping in PATH
+             which_paths = ["/usr/bin/which", "/bin/which", "/usr/local/bin/which"]
+             which_cmd = None
+             
+             # Find 'which' command
+             for path in which_paths:
+                 if os.path.exists(path) and os.access(path, os.X_OK):
+                     which_cmd = path
+                     break
+                     
+             # If which is found, use it to find ping
+             if which_cmd:
                  try:
                      result = subprocess.run(
-                     ["which", "ping"], 
+                         [which_cmd, "ping"], 
                          capture_output=True, 
                          text=True, 
              # Check common locations
              for path in common_paths:
+                 if os.path.exists(path) and os.access(path, os.X_OK):
+                     return path
+                     
+             # If we're on Windows, look for ping in expected locations
+             if platform.system().lower() == "windows":
+                 windows_paths = [
+                     r"C:\Windows\System32\ping.exe",
+                     r"C:\Windows\ping.exe"
+                 ]
+                 for path in windows_paths:
                      if os.path.exists(path) and os.access(path, os.X_OK):
                          return path
```

---

_****_





Finally, let's also improve the socket-based fallback to be more robust:

---

_****_

```diff
              import socket
              import time
+             import random
              
              # Validate hostname
                  return float("inf")
                  
-             # We'll make a TCP connection to port 443 (HTTPS) as most servers will have this open
+             # Try a few common ports that VPN servers often have open
+             ports = [443, 80, 1194, 53]  # HTTPS, HTTP, OpenVPN, DNS
+             
+             best_time = float("inf")
+             success = False
+             
+             # Try each port up to 2 times
+             for port in ports:
+                 for attempt in range(2):
+                     try:
+                         # We'll make a TCP connection to measure latency
                          start_time = time.time()
                          
-             # Try to establish TCP connection
                          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                          s.settimeout(2.0)  # 2 second timeout
-             try:
-                 s.connect((hostname, 443))
+                         
+                         s.connect((hostname, port))
                          s.shutdown(socket.SHUT_RDWR)
+                         
                          end_time = time.time()
                          time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
                          
                          if self.verbose:
-                     self.logger.debug(f"Socket connection to {hostname}:443 took {time_ms:.2f}ms")
+                             self.logger.debug(f"Socket connection to {hostname}:{port} took {time_ms:.2f}ms")
                          
-                 return time_ms
+                         # Add a small random factor to the time to differentiate servers
+                         # This ensures we don't get the same exact time for multiple servers
+                         jitter = random.uniform(0, 0.5)  # Up to 0.5ms jitter
+                         time_ms += jitter
+                         
+                         best_time = min(best_time, time_ms)
+                         success = True
+                         
+                         # If we've already got a successful measurement, we don't need more
+                         if success and attempt > 0:
+                             break
+                             
                      except (socket.timeout, socket.error) as e:
                          if self.verbose:
-                     self.logger.debug(f"Socket connection to {hostname} failed: {e}")
-                 return float("inf")
+                             self.logger.debug(f"Socket connection to {hostname}:{port} failed: {e}")
                      finally:
                          s.close()
                  
+                 # If we already got a good time, we can stop trying more ports
+                 if success:
+                     break
+             
+             if success:
+                 return best_time
+             else:
+                 return float("inf")
+                 
          except Exception as e:
              self.logger.warning(f"Fallback ping to {hostname} failed: {e}")
```

---

_****_







Let's fix the linter error:

---

_****_

Cancelled

---

_****_



---

_**User**_

Field required [type=missing, input_value={'id': 51, 'metadata': [{...'}], 'status': 'online'}, input_type=dict]   

THIS IS also a problem, this comes 99x

---

_**Assistant**_

<think>The user is pointing out another issue in the error message shown in the original VIBE.txt file. They're indicating that there's a Pydantic validation error that appears 99 times:

```
Field required [type=missing, input_value={'id': 51, 'metadata': [{...'}], 'status': 'online'}, input_type=dict]
```

This is a different issue from the "ping" command error that I fixed earlier. Let me analyze the problem:

1. This appears to be a Pydantic validation error about missing required fields.
2. It's coming from the API response handling for the "technologies" field.
3. Looking at the error message, it shows objects with 'id', 'metadata', and 'status', but is missing some required field(s).
4. The error mentions 99 occurrences of this, suggesting it's happening for multiple server entries.

Looking at the server.py file, the issue likely involves how the API response is being parsed and converted into Pydantic models. The error is related to the Technology model:

```python
class Technology(TypedDict):
    """Server technology information."""

    id: int
    status: str
    metadata: NotRequired[list[TechnologyMetadata]]
```

According to the error, there appear to be instances where some required fields are missing in the API response data when it's being converted to this model.

Let me look in the code to see where this validation might be happening, and specifically, what the required fields are for the Technology model that may be missing.

Based on the Pydantic error format, there should be missing required fields from the API response. The error message indicates it's related to technology entries in the API response, and specifically it mentions technologies with indices like "72.technologies.1.created_at" and "99.technologies.6.created_at".

It appears the API response is expected to have "created_at" and "updated_at" fields for technologies, but these are missing in the actual response.

Let me look at how the API response is being processed and how these fields are handled. I need to fix the code to handle missing fields properly or make those fields optional in the Pydantic models.

Based on the error, we need to:
1. Find where the API response is being processed
2. Identify how the Technology model is populated
3. Make sure that the required fields (like 'created_at' and 'updated_at') are either made optional or properly defaulted if missing

Looking at the Technology TypedDict definition, we need to either:
1. Make 'created_at' and 'updated_at' fields optional (using NotRequired[])
2. Or add defaults for these fields when processing the API response

Let's look at the part of the code that processes the API response to see how to fix this.</think>I see another issue in your error logs. You're getting Pydantic validation errors about missing required fields:

```
Field required [type=missing, input_value={'id': 51, 'metadata': [{...'}], 'status': 'online'}, input_type=dict]
```

This appears around 99 times in your logs, specifically for fields like `technologies.X.created_at` and `technologies.X.updated_at`. This is a Pydantic validation error indicating that the API response doesn't include these required timestamp fields in the technology objects.

Let's fix this by updating the `Technology` TypedDict to make those timestamp fields optional:

---

_****_

```diff
      status: str
      metadata: NotRequired[list[TechnologyMetadata]]
+     created_at: NotRequired[str]
+     updated_at: NotRequired[str]
  
  
```

---

_****_



Now, I need to also fix the linter error about the possibly unbound variable 's' in the socket fallback method:

---

_****_

```diff
              for port in ports:
                  for attempt in range(2):
+                     s = None  # Initialize s to None to avoid unbound variable error
                      try:
                          # We'll make a TCP connection to measure latency
                              self.logger.debug(f"Socket connection to {hostname}:{port} failed: {e}")
                      finally:
+                         if s is not None:
                              s.close()
                  
```

---

_****_





The linter is still flagging the issue. Let's try a different approach:

---

_****_

```diff
              for port in ports:
                  for attempt in range(2):
-                     s = None  # Initialize s to None to avoid unbound variable error
-                     try:
                      # We'll make a TCP connection to measure latency
                      start_time = time.time()
                      
-                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
-                         s.settimeout(2.0)  # 2 second timeout
-                         
-                         s.connect((hostname, port))
-                         s.shutdown(socket.SHUT_RDWR)
-                         
-                         end_time = time.time()
-                         time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
-                         
-                         if self.verbose:
-                             self.logger.debug(f"Socket connection to {hostname}:{port} took {time_ms:.2f}ms")
-                         
+                     # Create socket and measure connection time
+                     connection_time = self._measure_socket_connection(hostname, port)
+                     
+                     # If connection was successful (not infinite)
+                     if connection_time < float("inf"):
                          # Add a small random factor to the time to differentiate servers
                          # This ensures we don't get the same exact time for multiple servers
                          jitter = random.uniform(0, 0.5)  # Up to 0.5ms jitter
-                         time_ms += jitter
+                         time_ms = connection_time + jitter
                          
                          best_time = min(best_time, time_ms)
                          success = True
                          
                          # If we've already got a successful measurement, we don't need more
-                         if success and attempt > 0:
+                         if attempt > 0:
                              break
-                             
-                     except (socket.timeout, socket.error) as e:
-                         if self.verbose:
-                             self.logger.debug(f"Socket connection to {hostname}:{port} failed: {e}")
-                     finally:
-                         if s is not None:
-                             s.close()
                      
                  # If we already got a good time, we can stop trying more ports
              self.logger.warning(f"Fallback ping to {hostname} failed: {e}")
              return float("inf")
+             
+     def _measure_socket_connection(self, hostname: str, port: int) -> float:
+         """Measure connection time to a hostname:port using a socket.
+         
+         Args:
+             hostname: Server hostname to connect to
+             port: Port to connect to
+             
+         Returns:
+             float: Connection time in milliseconds, or float('inf') if failed
+         """
+         s = None
+         try:
+             start_time = time.time()
+             
+             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+             s.settimeout(2.0)  # 2 second timeout
+             
+             s.connect((hostname, port))
+             s.shutdown(socket.SHUT_RDWR)
+             
+             end_time = time.time()
+             time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
+             
+             if self.verbose:
+                 self.logger.debug(f"Socket connection to {hostname}:{port} took {time_ms:.2f}ms")
+             
+             return time_ms
+             
+         except (socket.timeout, socket.error) as e:
+             if self.verbose:
+                 self.logger.debug(f"Socket connection to {hostname}:{port} failed: {e}")
+             return float("inf")
+             
+         finally:
+             if s is not None:
+                 s.close()
  
      def _is_valid_server(self, server: Any) -> bool:
```

---

_****_







Now we need to fix the missing socket import in the new method:

---

_****_

```diff
  import re
  import os
+ import socket
  from typing import Any, TypedDict, NotRequired, cast
  
                  self.logger.debug(f"Using socket fallback to ping {hostname}")
                  
-             import socket
              import time
              import random
```

---

_****_





There was one more socket import to remove since we now have it at the top of the file:

---

_****_

```diff
  import os
  import socket
+ import random
  from typing import Any, TypedDict, NotRequired, cast
  
              if self.verbose:
                  self.logger.debug(f"Using socket fallback to ping {hostname}")
-                 
-             import time
-             import random
                  
              # Validate hostname
```

---

_****_





Now let's run the linter to make sure all errors are fixed:

---

_****_

Cancelled

---

_****_



---

_**User**_

73.technologies.3.created_at
  Field required [type=missing, input_value={'id': 42, 'status': 'online'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
73.technologies.3.updated_at
  Field required [type=missing, input_value={'id': 42, 'status': 'online'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
73.technologies.4.name
  Field required [type=missing, input_value={'id': 45, 'status': 'online'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
73.technologies.4.identifier
  Field required [type=missing, input_value={'id': 45, 'status': 'online'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
73.technologies.4.created_at
  Field required [type=missing, input_value={'id': 45, 'status': 'online'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
73.technologies.4.updated_at



Actually check 

@https://api.nordvpn.com/v2/servers 

{"servers":[{"id":929966,"created_at":"2018-09-03 07:58:14","updated_at":"2025-02-24 07:12:34","name":"Poland #128","station":"194.99.105.99","ipv6_station":"","hostname":"pl128.nordvpn.com","status":"online","load":34,"ips":[{"id":1019456,"created_at":"2023-07-14 07:40:33","updated_at":"2023-07-14 07:40:33","server_id":929966,"ip_id":23702,"type":"entry","ip":{"id":23702,"ip":"194.99.105.99","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"kjAOzXQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[367]},{"id":930428,"created_at":"2018-09-07 14:03:13","updated_at":"2025-02-24 07:08:35","name":"Hungary #48","station":"185.189.114.28","ipv6_station":"","hostname":"hu48.nordvpn.com","status":"online","load":7,"ips":[{"id":1039253,"created_at":"2023-07-19 09:32:10","updated_at":"2023-07-19 09:32:10","server_id":930428,"ip_id":6811,"type":"entry","ip":{"id":6811,"ip":"185.189.114.28","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejXY="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[247]},{"id":930488,"created_at":"2018-09-10 08:02:01","updated_at":"2025-02-24 07:08:35","name":"United States #5063","station":"185.245.87.59","ipv6_station":"","hostname":"us5063.nordvpn.com","status":"online","load":35,"ips":[{"id":767396,"created_at":"2022-12-27 12:43:51","updated_at":"2022-12-27 12:43:51","server_id":930488,"ip_id":26105,"type":"entry","ip":{"id":26105,"ip":"185.245.87.59","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[51]},{"id":930695,"created_at":"2018-09-11 14:06:28","updated_at":"2025-02-24 07:16:34","name":"Austria #86","station":"185.216.34.100","ipv6_station":"","hostname":"at86.nordvpn.com","status":"online","load":6,"ips":[{"id":1011926,"created_at":"2023-07-12 10:41:56","updated_at":"2023-07-12 10:41:56","server_id":930695,"ip_id":9103,"type":"entry","ip":{"id":9103,"ip":"185.216.34.100","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"F6b2ac9H7hEvt03EonY1bS4FzNAabEmURDTB8wIIPXc="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[205]},{"id":930743,"created_at":"2018-09-11 14:23:53","updated_at":"2025-02-24 07:16:34","name":"Switzerland #217","station":"185.156.175.132","ipv6_station":"","hostname":"ch217.nordvpn.com","status":"online","load":20,"ips":[{"id":937649,"created_at":"2023-06-19 09:50:19","updated_at":"2023-06-19 09:50:19","server_id":930743,"ip_id":8469,"type":"entry","ip":{"id":8469,"ip":"185.156.175.132","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[107]},{"id":930755,"created_at":"2018-09-11 14:38:01","updated_at":"2025-02-24 07:08:35","name":"Denmark #152","station":"82.102.20.212","ipv6_station":"","hostname":"dk152.nordvpn.com","status":"online","load":6,"ips":[{"id":1010027,"created_at":"2023-07-12 08:58:16","updated_at":"2023-07-12 08:58:16","server_id":930755,"ip_id":9533,"type":"entry","ip":{"id":9533,"ip":"82.102.20.212","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"EHL1zeXjZEJlqtFA8qaRVuvl0zR4skbC/AjiG66CLCc="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[169]},{"id":931112,"created_at":"2018-09-18 11:04:44","updated_at":"2025-02-24 07:16:34","name":"Norway #151","station":"82.102.22.92","ipv6_station":"","hostname":"no151.nordvpn.com","status":"online","load":9,"ips":[{"id":928820,"created_at":"2023-06-14 11:53:03","updated_at":"2023-06-14 11:53:03","server_id":931112,"ip_id":8291,"type":"entry","ip":{"id":8291,"ip":"82.102.22.92","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":931337,"created_at":"2018-09-21 04:24:34","updated_at":"2025-02-24 07:16:34","name":"Switzerland #218","station":"84.39.112.20","ipv6_station":"","hostname":"ch218.nordvpn.com","status":"online","load":10,"ips":[{"id":937745,"created_at":"2023-06-19 10:43:17","updated_at":"2023-06-19 10:43:17","server_id":931337,"ip_id":8629,"type":"entry","ip":{"id":8629,"ip":"84.39.112.20","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[107]},{"id":931412,"created_at":"2018-09-26 09:02:05","updated_at":"2025-02-24 07:12:34","name":"United Kingdom #1784","station":"81.92.202.11","ipv6_station":"","hostname":"uk1784.nordvpn.com","status":"online","load":11,"ips":[{"id":1028921,"created_at":"2023-07-18 09:48:03","updated_at":"2023-07-18 09:48:03","server_id":931412,"ip_id":7625,"type":"entry","ip":{"id":7625,"ip":"81.92.202.11","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[45]},{"id":931418,"created_at":"2018-09-26 09:06:11","updated_at":"2025-02-24 07:16:34","name":"France #555","station":"82.102.18.252","ipv6_station":"","hostname":"fr555.nordvpn.com","status":"online","load":14,"ips":[{"id":964649,"created_at":"2023-06-27 12:19:33","updated_at":"2023-06-27 12:19:33","server_id":931418,"ip_id":8963,"type":"entry","ip":{"id":8963,"ip":"82.102.18.252","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":931430,"created_at":"2018-09-26 09:10:56","updated_at":"2025-02-24 07:16:34","name":"Switzerland #219","station":"185.9.18.84","ipv6_station":"","hostname":"ch219.nordvpn.com","status":"online","load":11,"ips":[{"id":937793,"created_at":"2023-06-19 10:43:40","updated_at":"2023-06-19 10:43:40","server_id":931430,"ip_id":8633,"type":"entry","ip":{"id":8633,"ip":"185.9.18.84","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[107]},{"id":931490,"created_at":"2018-09-26 09:38:23","updated_at":"2025-02-24 07:12:34","name":"United States #5064","station":"195.206.104.156","ipv6_station":"","hostname":"us5064.nordvpn.com","status":"online","load":24,"ips":[{"id":767441,"created_at":"2022-12-27 12:44:02","updated_at":"2022-12-27 12:44:02","server_id":931490,"ip_id":27317,"type":"entry","ip":{"id":27317,"ip":"195.206.104.156","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[51]},{"id":931931,"created_at":"2018-10-11 10:26:09","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #765","station":"89.35.28.131","ipv6_station":"","hostname":"uk765.nordvpn.com","status":"online","load":20,"ips":[{"id":1855705,"created_at":"2024-09-27 09:00:56","updated_at":"2024-09-27 09:00:56","server_id":931931,"ip_id":26909,"type":"entry","ip":{"id":26909,"ip":"89.35.28.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":932777,"created_at":"2018-11-06 07:54:02","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #812","station":"77.81.191.3","ipv6_station":"","hostname":"uk812.nordvpn.com","status":"online","load":13,"ips":[{"id":1855719,"created_at":"2024-09-27 09:01:39","updated_at":"2024-09-27 09:01:39","server_id":932777,"ip_id":13433,"type":"entry","ip":{"id":13433,"ip":"77.81.191.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":932783,"created_at":"2018-11-06 08:09:06","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #813","station":"89.34.98.195","ipv6_station":"","hostname":"uk813.nordvpn.com","status":"online","load":12,"ips":[{"id":1855733,"created_at":"2024-09-27 09:02:09","updated_at":"2024-09-27 09:02:09","server_id":932783,"ip_id":7161,"type":"entry","ip":{"id":7161,"ip":"89.34.98.195","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":932804,"created_at":"2018-11-08 07:37:22","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #814","station":"185.121.139.100","ipv6_station":"","hostname":"uk814.nordvpn.com","status":"online","load":15,"ips":[{"id":1855746,"created_at":"2024-09-27 09:03:38","updated_at":"2024-09-27 09:03:38","server_id":932804,"ip_id":7915,"type":"entry","ip":{"id":7915,"ip":"185.121.139.100","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":932972,"created_at":"2018-11-14 08:02:57","updated_at":"2025-02-24 07:12:34","name":"United Kingdom #871","station":"89.34.99.131","ipv6_station":"","hostname":"uk871.nordvpn.com","status":"online","load":13,"ips":[{"id":1855760,"created_at":"2024-09-27 09:04:02","updated_at":"2024-09-27 09:04:02","server_id":932972,"ip_id":10931,"type":"entry","ip":{"id":10931,"ip":"89.34.99.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":933098,"created_at":"2018-11-19 09:23:03","updated_at":"2025-02-24 07:04:34","name":"United Kingdom #873","station":"195.206.180.3","ipv6_station":"","hostname":"uk873.nordvpn.com","status":"online","load":11,"ips":[{"id":1855773,"created_at":"2024-09-27 09:04:51","updated_at":"2024-09-27 09:04:51","server_id":933098,"ip_id":14385,"type":"entry","ip":{"id":14385,"ip":"195.206.180.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":933104,"created_at":"2018-11-19 09:23:12","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #875","station":"195.206.180.131","ipv6_station":"","hostname":"uk875.nordvpn.com","status":"online","load":23,"ips":[{"id":1855787,"created_at":"2024-09-27 09:05:21","updated_at":"2024-09-27 09:05:21","server_id":933104,"ip_id":16571,"type":"entry","ip":{"id":16571,"ip":"195.206.180.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":933110,"created_at":"2018-11-20 08:12:09","updated_at":"2025-02-24 06:56:35","name":"Germany #507","station":"185.130.184.115","ipv6_station":"","hostname":"de507.nordvpn.com","status":"online","load":0,"ips":[{"id":65147,"created_at":"2018-11-21 13:55:29","updated_at":"2018-11-21 13:55:29","server_id":933110,"ip_id":17666,"type":"entry","ip":{"id":17666,"ip":"185.130.184.115","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":933113,"created_at":"2018-11-20 08:12:10","updated_at":"2025-02-24 00:16:44","name":"Germany #508","station":"185.130.184.116","ipv6_station":"","hostname":"de508.nordvpn.com","status":"online","load":0,"ips":[{"id":65345,"created_at":"2018-11-21 14:00:30","updated_at":"2018-11-21 14:00:30","server_id":933113,"ip_id":17669,"type":"entry","ip":{"id":17669,"ip":"185.130.184.116","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":933116,"created_at":"2018-11-20 08:12:11","updated_at":"2025-02-24 07:16:35","name":"Germany #509","station":"185.130.184.117","ipv6_station":"","hostname":"de509.nordvpn.com","status":"online","load":3,"ips":[{"id":65543,"created_at":"2018-11-21 14:05:19","updated_at":"2018-11-21 14:05:19","server_id":933116,"ip_id":17672,"type":"entry","ip":{"id":17672,"ip":"185.130.184.117","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":933119,"created_at":"2018-11-20 08:12:12","updated_at":"2025-02-24 06:52:33","name":"Germany #510","station":"185.130.184.118","ipv6_station":"","hostname":"de510.nordvpn.com","status":"online","load":0,"ips":[{"id":791747,"created_at":"2023-01-10 11:47:01","updated_at":"2023-01-10 11:47:01","server_id":933119,"ip_id":17675,"type":"entry","ip":{"id":17675,"ip":"185.130.184.118","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":933302,"created_at":"2018-11-22 08:46:59","updated_at":"2025-02-24 07:04:35","name":"United Kingdom #877","station":"81.19.217.3","ipv6_station":"","hostname":"uk877.nordvpn.com","status":"online","load":11,"ips":[{"id":1855801,"created_at":"2024-09-27 09:06:13","updated_at":"2024-09-27 09:06:13","server_id":933302,"ip_id":24521,"type":"entry","ip":{"id":24521,"ip":"81.19.217.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":933308,"created_at":"2018-11-22 08:49:05","updated_at":"2025-02-24 04:40:34","name":"United States #2920","station":"96.9.246.179","ipv6_station":"","hostname":"us2920.nordvpn.com","status":"online","load":0,"ips":[{"id":395835,"created_at":"2021-09-27 05:55:48","updated_at":"2021-09-27 05:55:48","server_id":933308,"ip_id":24995,"type":"entry","ip":{"id":24995,"ip":"96.9.246.179","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":933311,"created_at":"2018-11-22 08:49:08","updated_at":"2025-02-24 04:53:29","name":"United States #2921","station":"96.9.246.180","ipv6_station":"","hostname":"us2921.nordvpn.com","status":"online","load":0,"ips":[{"id":109960,"created_at":"2019-04-26 08:39:37","updated_at":"2019-04-26 08:39:37","server_id":933311,"ip_id":24998,"type":"entry","ip":{"id":24998,"ip":"96.9.246.180","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":934646,"created_at":"2019-01-07 08:52:01","updated_at":"2025-02-24 07:16:34","name":"United Kingdom #879","station":"81.19.223.3","ipv6_station":"","hostname":"uk879.nordvpn.com","status":"online","load":10,"ips":[{"id":1855675,"created_at":"2024-09-27 08:58:15","updated_at":"2024-09-27 08:58:15","server_id":934646,"ip_id":35480,"type":"entry","ip":{"id":35480,"ip":"81.19.223.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":934691,"created_at":"2019-01-11 09:17:40","updated_at":"2025-02-24 07:16:35","name":"United States #2924","station":"96.9.247.187","ipv6_station":"","hostname":"us2924.nordvpn.com","status":"online","load":0,"ips":[{"id":108760,"created_at":"2019-04-26 07:22:17","updated_at":"2019-04-26 07:22:17","server_id":934691,"ip_id":35609,"type":"entry","ip":{"id":35609,"ip":"96.9.247.187","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":934694,"created_at":"2019-01-11 09:17:45","updated_at":"2025-02-24 00:16:45","name":"United States #2925","station":"96.9.247.188","ipv6_station":"","hostname":"us2925.nordvpn.com","status":"online","load":0,"ips":[{"id":573023,"created_at":"2022-06-02 12:26:29","updated_at":"2022-06-02 12:26:29","server_id":934694,"ip_id":35615,"type":"entry","ip":{"id":35615,"ip":"96.9.247.188","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":935000,"created_at":"2019-01-30 09:55:48","updated_at":"2025-02-24 07:12:35","name":"United Kingdom #884","station":"178.239.169.3","ipv6_station":"","hostname":"uk884.nordvpn.com","status":"online","load":11,"ips":[{"id":1855653,"created_at":"2024-09-27 08:55:30","updated_at":"2024-09-27 08:55:30","server_id":935000,"ip_id":36434,"type":"entry","ip":{"id":36434,"ip":"178.239.169.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":937379,"created_at":"2019-03-12 06:27:04","updated_at":"2025-02-24 00:16:45","name":"United States #2929","station":"107.173.59.99","ipv6_station":"","hostname":"us2929.nordvpn.com","status":"online","load":0,"ips":[{"id":105682,"created_at":"2019-04-25 14:21:38","updated_at":"2019-04-25 14:21:38","server_id":937379,"ip_id":42143,"type":"entry","ip":{"id":42143,"ip":"107.173.59.99","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":937382,"created_at":"2019-03-12 06:28:00","updated_at":"2025-02-24 06:12:45","name":"United States #2930","station":"172.93.147.130","ipv6_station":"","hostname":"us2930.nordvpn.com","status":"online","load":0,"ips":[{"id":105295,"created_at":"2019-04-25 14:11:08","updated_at":"2019-04-25 14:11:08","server_id":937382,"ip_id":42152,"type":"entry","ip":{"id":42152,"ip":"172.93.147.130","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":937877,"created_at":"2019-03-20 08:33:15","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #886","station":"185.44.79.131","ipv6_station":"","hostname":"uk886.nordvpn.com","status":"online","load":14,"ips":[{"id":1855631,"created_at":"2024-09-27 08:52:23","updated_at":"2024-09-27 08:52:23","server_id":937877,"ip_id":43184,"type":"entry","ip":{"id":43184,"ip":"185.44.79.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,15,11],"service_ids":[1,5],"location_ids":[45]},{"id":938291,"created_at":"2019-03-28 02:48:46","updated_at":"2025-02-24 07:16:35","name":"Belgium #149","station":"77.243.191.250","ipv6_station":"","hostname":"be149.nordvpn.com","status":"online","load":16,"ips":[{"id":1007276,"created_at":"2023-07-11 10:41:43","updated_at":"2023-07-11 10:41:43","server_id":938291,"ip_id":6923,"type":"entry","ip":{"id":6923,"ip":"77.243.191.250","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"VSa6XYcD279ahd3IuEiUH6VpXn0+h+kWrD4OcN1ExUs="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3990]},{"id":938537,"created_at":"2019-03-28 07:14:01","updated_at":"2025-02-24 07:12:35","name":"United Kingdom #1806","station":"193.9.113.134","ipv6_station":"","hostname":"uk1806.nordvpn.com","status":"online","load":14,"ips":[{"id":1028543,"created_at":"2023-07-18 09:23:03","updated_at":"2023-07-18 09:23:03","server_id":938537,"ip_id":26495,"type":"entry","ip":{"id":26495,"ip":"193.9.113.134","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[45]},{"id":940130,"created_at":"2019-04-16 06:50:09","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #888","station":"185.16.205.3","ipv6_station":"","hostname":"uk888.nordvpn.com","status":"online","load":13,"ips":[{"id":1855608,"created_at":"2024-09-27 08:50:33","updated_at":"2024-09-27 08:50:33","server_id":940130,"ip_id":50201,"type":"entry","ip":{"id":50201,"ip":"185.16.205.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":940136,"created_at":"2019-04-16 06:51:14","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #890","station":"185.16.205.131","ipv6_station":"","hostname":"uk890.nordvpn.com","status":"online","load":16,"ips":[{"id":1856382,"created_at":"2024-10-03 12:49:53","updated_at":"2024-10-03 12:49:53","server_id":940136,"ip_id":50207,"type":"entry","ip":{"id":50207,"ip":"185.16.205.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":945157,"created_at":"2019-06-13 04:49:56","updated_at":"2025-02-24 01:00:37","name":"United States #2939","station":"172.93.237.99","ipv6_station":"","hostname":"us2939.nordvpn.com","status":"online","load":0,"ips":[{"id":138778,"created_at":"2019-07-09 14:15:11","updated_at":"2019-07-09 14:15:11","server_id":945157,"ip_id":63127,"type":"entry","ip":{"id":63127,"ip":"172.93.237.99","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":945160,"created_at":"2019-06-13 04:49:57","updated_at":"2025-02-24 00:16:47","name":"United States #2940","station":"172.93.237.100","ipv6_station":"","hostname":"us2940.nordvpn.com","status":"online","load":0,"ips":[{"id":139372,"created_at":"2019-07-09 14:25:49","updated_at":"2019-07-09 14:25:49","server_id":945160,"ip_id":63130,"type":"entry","ip":{"id":63130,"ip":"172.93.237.100","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":945916,"created_at":"2019-06-25 11:49:45","updated_at":"2025-02-24 07:16:35","name":"Germany #655","station":"194.31.54.4","ipv6_station":"","hostname":"de655.nordvpn.com","status":"online","load":2,"ips":[{"id":1773885,"created_at":"2024-08-21 05:08:31","updated_at":"2024-08-21 05:08:31","server_id":945916,"ip_id":65179,"type":"entry","ip":{"id":65179,"ip":"194.31.54.4","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":946435,"created_at":"2019-07-12 07:51:12","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #892","station":"195.206.170.3","ipv6_station":"","hostname":"uk892.nordvpn.com","status":"online","load":15,"ips":[{"id":1855574,"created_at":"2024-09-27 08:48:09","updated_at":"2024-09-27 08:48:09","server_id":946435,"ip_id":68866,"type":"entry","ip":{"id":68866,"ip":"195.206.170.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":946441,"created_at":"2019-07-12 07:51:13","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #894","station":"195.206.170.131","ipv6_station":"","hostname":"uk894.nordvpn.com","status":"online","load":16,"ips":[{"id":1856397,"created_at":"2024-10-03 12:49:58","updated_at":"2024-10-03 12:49:58","server_id":946441,"ip_id":68872,"type":"entry","ip":{"id":68872,"ip":"195.206.170.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":947116,"created_at":"2019-08-06 07:35:03","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #896","station":"178.239.164.3","ipv6_station":"","hostname":"uk896.nordvpn.com","status":"online","load":14,"ips":[{"id":1855544,"created_at":"2024-09-27 08:46:21","updated_at":"2024-09-27 08:46:21","server_id":947116,"ip_id":72133,"type":"entry","ip":{"id":72133,"ip":"178.239.164.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,15],"service_ids":[1,5],"location_ids":[45]},{"id":947122,"created_at":"2019-08-06 07:35:04","updated_at":"2025-02-24 07:16:35","name":"United Kingdom #898","station":"178.239.164.131","ipv6_station":"","hostname":"uk898.nordvpn.com","status":"online","load":14,"ips":[{"id":1855524,"created_at":"2024-09-27 08:44:47","updated_at":"2024-09-27 08:44:47","server_id":947122,"ip_id":72139,"type":"entry","ip":{"id":72139,"ip":"178.239.164.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,15,11],"service_ids":[1,5],"location_ids":[45]},{"id":947235,"created_at":"2019-08-23 12:48:22","updated_at":"2025-02-24 07:16:35","name":"United States #2943","station":"89.187.175.97","ipv6_station":"","hostname":"us2943.nordvpn.com","status":"online","load":0,"ips":[{"id":1818610,"created_at":"2024-08-29 11:50:57","updated_at":"2024-08-29 11:50:57","server_id":947235,"ip_id":72639,"type":"entry","ip":{"id":72639,"ip":"89.187.175.97","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[79]},{"id":947238,"created_at":"2019-08-23 12:48:22","updated_at":"2025-02-24 06:40:35","name":"United States #2944","station":"89.187.175.98","ipv6_station":"","hostname":"us2944.nordvpn.com","status":"online","load":0,"ips":[{"id":1810823,"created_at":"2024-08-28 11:12:32","updated_at":"2024-08-28 11:12:32","server_id":947238,"ip_id":72645,"type":"entry","ip":{"id":72645,"ip":"89.187.175.98","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[79]},{"id":947280,"created_at":"2019-08-28 06:59:11","updated_at":"2025-02-24 07:16:35","name":"United States #2945","station":"89.187.185.86","ipv6_station":"","hostname":"us2945.nordvpn.com","status":"online","load":10,"ips":[{"id":1821697,"created_at":"2024-08-30 04:42:38","updated_at":"2024-08-30 04:42:38","server_id":947280,"ip_id":73533,"type":"entry","ip":{"id":73533,"ip":"89.187.185.86","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[51]},{"id":947283,"created_at":"2019-08-28 06:59:11","updated_at":"2025-02-24 07:16:35","name":"United States #2946","station":"89.187.185.97","ipv6_station":"","hostname":"us2946.nordvpn.com","status":"online","load":2,"ips":[{"id":1807685,"created_at":"2024-08-28 06:22:30","updated_at":"2024-08-28 06:22:30","server_id":947283,"ip_id":73536,"type":"entry","ip":{"id":73536,"ip":"89.187.185.97","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[51]},{"id":947592,"created_at":"2019-09-18 09:51:34","updated_at":"2025-02-24 00:16:49","name":"Netherlands #408","station":"185.229.58.3","ipv6_station":"","hostname":"nl408.nordvpn.com","status":"online","load":0,"ips":[{"id":1751714,"created_at":"2024-08-19 05:57:10","updated_at":"2024-08-19 05:57:10","server_id":947592,"ip_id":74514,"type":"entry","ip":{"id":74514,"ip":"185.229.58.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"5p4RkybdRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[5]},{"id":947595,"created_at":"2019-09-18 09:51:34","updated_at":"2025-02-24 07:04:35","name":"Netherlands #409","station":"185.229.58.129","ipv6_station":"","hostname":"nl409.nordvpn.com","status":"online","load":1,"ips":[{"id":1768144,"created_at":"2024-08-20 07:16:03","updated_at":"2024-08-20 07:16:03","server_id":947595,"ip_id":74517,"type":"entry","ip":{"id":74517,"ip":"185.229.58.129","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"5p4RkybdRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[5]},{"id":948099,"created_at":"2019-09-26 12:22:40","updated_at":"2025-02-24 00:20:39","name":"Germany #676","station":"37.120.223.116","ipv6_station":"","hostname":"de676.nordvpn.com","status":"online","load":0,"ips":[{"id":1791453,"created_at":"2024-08-26 11:14:49","updated_at":"2024-08-26 11:14:49","server_id":948099,"ip_id":75906,"type":"entry","ip":{"id":75906,"ip":"37.120.223.116","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[133]},{"id":948810,"created_at":"2019-10-11 09:06:37","updated_at":"2025-02-24 07:16:35","name":"United States #5055","station":"89.187.175.2","ipv6_station":"","hostname":"us5055.nordvpn.com","status":"online","load":11,"ips":[{"id":795035,"created_at":"2023-01-16 13:35:10","updated_at":"2023-01-16 13:35:10","server_id":948810,"ip_id":78471,"type":"entry","ip":{"id":78471,"ip":"89.187.175.2","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[79]},{"id":949095,"created_at":"2019-10-29 07:51:33","updated_at":"2025-02-24 00:16:49","name":"United States #2949","station":"64.44.32.75","ipv6_station":"","hostname":"us2949.nordvpn.com","status":"online","load":0,"ips":[{"id":155328,"created_at":"2019-10-30 08:32:23","updated_at":"2019-10-30 08:32:23","server_id":949095,"ip_id":80337,"type":"entry","ip":{"id":80337,"ip":"64.44.32.75","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":949098,"created_at":"2019-10-29 07:51:33","updated_at":"2025-02-24 03:04:34","name":"United States #2950","station":"64.44.32.76","ipv6_station":"","hostname":"us2950.nordvpn.com","status":"online","load":0,"ips":[{"id":193733,"created_at":"2020-04-28 07:18:59","updated_at":"2020-04-28 07:18:59","server_id":949098,"ip_id":80340,"type":"entry","ip":{"id":80340,"ip":"64.44.32.76","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"id":949581,"created_at":"2019-11-20 07:55:10","updated_at":"2025-02-24 07:16:35","name":"France #439","station":"185.93.2.199","ipv6_station":"","hostname":"fr439.nordvpn.com","status":"online","load":2,"ips":[{"id":1803435,"created_at":"2024-08-27 13:14:39","updated_at":"2024-08-27 13:14:39","server_id":949581,"ip_id":82254,"type":"entry","ip":{"id":82254,"ip":"185.93.2.199","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[87]},{"id":949584,"created_at":"2019-11-20 07:55:10","updated_at":"2025-02-24 07:16:35","name":"France #440","station":"185.93.2.206","ipv6_station":"","hostname":"fr440.nordvpn.com","status":"online","load":2,"ips":[{"id":1779073,"created_at":"2024-08-22 08:12:09","updated_at":"2024-08-22 08:12:09","server_id":949584,"ip_id":82257,"type":"entry","ip":{"id":82257,"ip":"185.93.2.206","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[87]},{"id":950271,"created_at":"2019-12-02 10:45:18","updated_at":"2025-02-24 07:12:35","name":"Japan #429","station":"37.120.210.107","ipv6_station":"","hostname":"jp429.nordvpn.com","status":"online","load":17,"ips":[{"id":723494,"created_at":"2022-11-17 10:58:24","updated_at":"2022-11-17 10:58:24","server_id":950271,"ip_id":85143,"type":"entry","ip":{"id":85143,"ip":"37.120.210.107","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"location_ids":[3984]},{"id":950346,"created_at":"2019-12-03 07:26:00","updated_at":"2025-02-24 07:16:35","name":"Spain #114","station":"37.120.199.243","ipv6_station":"","hostname":"es114.nordvpn.com","status":"online","load":10,"ips":[{"id":1022015,"created_at":"2023-07-14 12:08:53","updated_at":"2023-07-14 12:08:53","server_id":950346,"ip_id":85356,"type":"entry","ip":{"id":85356,"ip":"37.120.199.243","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"IF1FGVSzrUznFVZ+dymIz+6bdlCgsuiT/d6cyapN8lw="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[113]},{"id":950361,"created_at":"2019-12-03 07:52:53","updated_at":"2025-02-24 07:16:35","name":"Italy #132","station":"217.138.197.75","ipv6_station":"","hostname":"it132.nordvpn.com","status":"online","load":19,"ips":[{"id":939377,"created_at":"2023-06-20 06:54:02","updated_at":"2023-06-20 06:54:02","server_id":950361,"ip_id":85416,"type":"entry","ip":{"id":85416,"ip":"217.138.197.75","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FgxaycYZ4t1kp4x7LDv60sczNTAl0h/d4pyyUNHhgBc="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3978]},{"id":950406,"created_at":"2019-12-03 09:17:57","updated_at":"2025-02-24 07:16:35","name":"United States #4735","station":"217.138.198.235","ipv6_station":"","hostname":"us4735.nordvpn.com","status":"online","load":17,"ips":[{"id":438578,"created_at":"2021-12-08 11:11:25","updated_at":"2021-12-08 11:11:25","server_id":950406,"ip_id":85596,"type":"entry","ip":{"id":85596,"ip":"217.138.198.235","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[305]},{"id":950436,"created_at":"2019-12-03 09:54:36","updated_at":"2025-02-24 07:12:35","name":"Poland #122","station":"37.120.211.171","ipv6_station":"","hostname":"pl122.nordvpn.com","status":"online","load":14,"ips":[{"id":1020326,"created_at":"2023-07-14 07:43:43","updated_at":"2023-07-14 07:43:43","server_id":950436,"ip_id":85716,"type":"entry","ip":{"id":85716,"ip":"37.120.211.171","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"kjAOzXQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[367]},{"id":950481,"created_at":"2019-12-03 12:01:58","updated_at":"2025-02-24 07:16:35","name":"Czech Republic #93","station":"217.138.199.27","ipv6_station":"","hostname":"cz93.nordvpn.com","status":"online","load":11,"ips":[{"id":1042049,"created_at":"2023-07-19 10:40:00","updated_at":"2023-07-19 10:40:00","server_id":950481,"ip_id":85899,"type":"entry","ip":{"id":85899,"ip":"217.138.199.27","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"apEe1p4IQvCQxexoxoUTXsm2p582FtbDAboPwThFYEs="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[143]},{"id":950538,"created_at":"2019-12-03 12:56:46","updated_at":"2025-02-24 07:16:35","name":"Austria #80","station":"5.253.207.203","ipv6_station":"","hostname":"at80.nordvpn.com","status":"online","load":18,"ips":[{"id":1012112,"created_at":"2023-07-12 10:42:31","updated_at":"2023-07-12 10:42:31","server_id":950538,"ip_id":86127,"type":"entry","ip":{"id":86127,"ip":"5.253.207.203","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"F6b2ac9H7hEvt03EonY1bS4FzNAabEmURDTB8wIIPXc="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[205]},{"id":950568,"created_at":"2019-12-03 13:48:18","updated_at":"2025-02-24 07:16:35","name":"Romania #59","station":"86.106.137.187","ipv6_station":"","hostname":"ro59.nordvpn.com","status":"online","load":19,"ips":[{"id":1043009,"created_at":"2023-07-19 11:39:41","updated_at":"2023-07-19 11:39:41","server_id":950568,"ip_id":86247,"type":"entry","ip":{"id":86247,"ip":"86.106.137.187","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"o3Dj1qKYmzBBOBaD9JAhK9cg/8nfYxWg6GADL09DPHE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[65]},{"id":950598,"created_at":"2019-12-03 14:06:40","updated_at":"2025-02-24 07:12:35","name":"Switzerland #198","station":"37.120.213.131","ipv6_station":"","hostname":"ch198.nordvpn.com","status":"online","load":14,"ips":[{"id":938273,"created_at":"2023-06-19 10:48:10","updated_at":"2023-06-19 10:48:10","server_id":950598,"ip_id":86367,"type":"entry","ip":{"id":86367,"ip":"37.120.213.131","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[107]},{"id":950628,"created_at":"2019-12-03 14:25:53","updated_at":"2025-02-24 07:00:36","name":"Bulgaria #38","station":"217.138.202.147","ipv6_station":"","hostname":"bg38.nordvpn.com","status":"online","load":5,"ips":[{"id":1030013,"created_at":"2023-07-19 06:14:34","updated_at":"2023-07-19 06:14:34","server_id":950628,"ip_id":86487,"type":"entry","ip":{"id":86487,"ip":"217.138.202.147","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"xqa+kDsDeYLQAnVDUQaFun9Djfo3c1ESTMwfNArHw10="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[259]},{"id":950658,"created_at":"2019-12-03 14:43:02","updated_at":"2025-02-24 07:16:35","name":"Hungary #47","station":"217.138.192.99","ipv6_station":"","hostname":"hu47.nordvpn.com","status":"online","load":5,"ips":[{"id":1038686,"created_at":"2023-07-19 09:30:15","updated_at":"2023-07-19 09:30:15","server_id":950658,"ip_id":86607,"type":"entry","ip":{"id":86607,"ip":"217.138.192.99","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejXY="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[247]},{"id":951120,"created_at":"2019-12-09 11:56:08","updated_at":"2025-02-24 07:16:35","name":"France #452","station":"45.152.181.219","ipv6_station":"","hostname":"fr452.nordvpn.com","status":"online","load":11,"ips":[{"id":965984,"created_at":"2023-06-27 13:02:08","updated_at":"2023-06-27 13:02:08","server_id":951120,"ip_id":87555,"type":"entry","ip":{"id":87555,"ip":"45.152.181.219","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":951123,"created_at":"2019-12-09 15:34:59","updated_at":"2025-02-24 07:16:35","name":"Japan #454","station":"89.187.161.54","ipv6_station":"","hostname":"jp454.nordvpn.com","status":"online","load":17,"ips":[{"id":596243,"created_at":"2022-07-08 07:48:04","updated_at":"2022-07-08 07:48:04","server_id":951123,"ip_id":87579,"type":"entry","ip":{"id":87579,"ip":"89.187.161.54","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"location_ids":[3984]},{"id":952599,"created_at":"2019-12-18 11:06:55","updated_at":"2025-02-24 07:04:35","name":"United States #4951","station":"84.17.44.122","ipv6_station":"","hostname":"us4951.nordvpn.com","status":"online","load":1,"ips":[{"id":1809916,"created_at":"2024-08-28 10:54:56","updated_at":"2024-08-28 10:54:56","server_id":952599,"ip_id":88899,"type":"entry","ip":{"id":88899,"ip":"84.17.44.122","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[51]},{"id":956138,"created_at":"2020-02-17 09:36:29","updated_at":"2025-02-24 07:16:35","name":"Denmark #150","station":"37.120.194.3","ipv6_station":"","hostname":"dk150.nordvpn.com","status":"online","load":11,"ips":[{"id":1010432,"created_at":"2023-07-12 09:16:23","updated_at":"2023-07-12 09:16:23","server_id":956138,"ip_id":98828,"type":"entry","ip":{"id":98828,"ip":"37.120.194.3","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"EHL1zeXjZEJlqtFA8qaRVuvl0zR4skbC/AjiG66CLCc="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[169]},{"id":956471,"created_at":"2020-02-25 08:28:44","updated_at":"2025-02-24 07:16:35","name":"Germany #750","station":"5.180.62.120","ipv6_station":"","hostname":"de750.nordvpn.com","status":"online","load":12,"ips":[{"id":979883,"created_at":"2023-06-30 07:46:11","updated_at":"2023-06-30 07:46:11","server_id":956471,"ip_id":102428,"type":"entry","ip":{"id":102428,"ip":"5.180.62.120","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[133]},{"id":956477,"created_at":"2020-02-25 11:14:12","updated_at":"2025-02-24 07:16:35","name":"United States #4953","station":"89.187.175.53","ipv6_station":"","hostname":"us4953.nordvpn.com","status":"online","load":2,"ips":[{"id":1850299,"created_at":"2024-09-12 13:39:49","updated_at":"2024-09-12 13:39:49","server_id":956477,"ip_id":102437,"type":"entry","ip":{"id":102437,"ip":"89.187.175.53","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[79]},{"id":956480,"created_at":"2020-02-25 11:14:13","updated_at":"2025-02-24 05:13:28","name":"United States #4954","station":"89.187.175.54","ipv6_station":"","hostname":"us4954.nordvpn.com","status":"online","load":1,"ips":[{"id":1812651,"created_at":"2024-08-28 12:13:26","updated_at":"2024-08-28 12:13:26","server_id":956480,"ip_id":102440,"type":"entry","ip":{"id":102440,"ip":"89.187.175.54","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[79]},{"id":956489,"created_at":"2020-02-25 12:24:48","updated_at":"2025-02-24 07:16:35","name":"Poland #125","station":"217.138.209.67","ipv6_station":"","hostname":"pl125.nordvpn.com","status":"online","load":61,"ips":[{"id":1020452,"created_at":"2023-07-14 07:44:07","updated_at":"2023-07-14 07:44:07","server_id":956489,"ip_id":102491,"type":"entry","ip":{"id":102491,"ip":"217.138.209.67","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"kjAOzXQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[367]},{"id":956522,"created_at":"2020-02-28 10:10:05","updated_at":"2025-02-24 07:16:35","name":"United States #5057","station":"217.138.208.211","ipv6_station":"","hostname":"us5057.nordvpn.com","status":"online","load":13,"ips":[{"id":438611,"created_at":"2021-12-08 11:11:42","updated_at":"2021-12-08 11:11:42","server_id":956522,"ip_id":102632,"type":"entry","ip":{"id":102632,"ip":"217.138.208.211","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[305]},{"id":956525,"created_at":"2020-02-28 10:10:06","updated_at":"2025-02-24 07:12:35","name":"United States #5058","station":"217.138.208.219","ipv6_station":"","hostname":"us5058.nordvpn.com","status":"online","load":13,"ips":[{"id":438644,"created_at":"2021-12-08 11:11:57","updated_at":"2021-12-08 11:11:57","server_id":956525,"ip_id":102638,"type":"entry","ip":{"id":102638,"ip":"217.138.208.219","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[305]},{"id":956528,"created_at":"2020-02-28 10:10:06","updated_at":"2025-02-24 07:16:35","name":"United States #5059","station":"217.138.208.139","ipv6_station":"","hostname":"us5059.nordvpn.com","status":"online","load":8,"ips":[{"id":438677,"created_at":"2021-12-08 11:12:16","updated_at":"2021-12-08 11:12:16","server_id":956528,"ip_id":102644,"type":"entry","ip":{"id":102644,"ip":"217.138.208.139","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[305]},{"id":956531,"created_at":"2020-02-28 10:10:07","updated_at":"2025-02-24 07:16:35","name":"United States #5060","station":"217.138.208.147","ipv6_station":"","hostname":"us5060.nordvpn.com","status":"online","load":18,"ips":[{"id":438710,"created_at":"2021-12-08 11:12:34","updated_at":"2021-12-08 11:12:34","server_id":956531,"ip_id":102650,"type":"entry","ip":{"id":102650,"ip":"217.138.208.147","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids":[305]},{"id":956603,"created_at":"2020-03-05 13:10:47","updated_at":"2025-02-24 07:16:35","name":"Norway #141","station":"37.120.203.163","ipv6_station":"","hostname":"no141.nordvpn.com","status":"online","load":18,"ips":[{"id":924911,"created_at":"2023-06-14 11:24:03","updated_at":"2023-06-14 11:24:03","server_id":956603,"ip_id":106556,"type":"entry","ip":{"id":106556,"ip":"37.120.203.163","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956606,"created_at":"2020-03-05 13:10:47","updated_at":"2025-02-24 07:16:36","name":"Norway #142","station":"37.120.203.171","ipv6_station":"","hostname":"no142.nordvpn.com","status":"online","load":5,"ips":[{"id":924866,"created_at":"2023-06-14 11:23:43","updated_at":"2023-06-14 11:23:43","server_id":956606,"ip_id":106562,"type":"entry","ip":{"id":106562,"ip":"37.120.203.171","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956609,"created_at":"2020-03-05 13:10:48","updated_at":"2025-02-24 07:12:36","name":"Norway #143","station":"37.120.203.179","ipv6_station":"","hostname":"no143.nordvpn.com","status":"online","load":6,"ips":[{"id":917294,"created_at":"2023-06-06 12:12:15","updated_at":"2023-06-06 12:12:15","server_id":956609,"ip_id":106568,"type":"entry","ip":{"id":106568,"ip":"37.120.203.179","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956612,"created_at":"2020-03-05 13:10:48","updated_at":"2025-02-24 07:16:36","name":"Norway #144","station":"37.120.203.187","ipv6_station":"","hostname":"no144.nordvpn.com","status":"online","load":6,"ips":[{"id":917252,"created_at":"2023-06-06 12:11:27","updated_at":"2023-06-06 12:11:27","server_id":956612,"ip_id":106574,"type":"entry","ip":{"id":106574,"ip":"37.120.203.187","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956615,"created_at":"2020-03-05 13:10:48","updated_at":"2025-02-24 07:16:36","name":"Norway #145","station":"37.120.203.195","ipv6_station":"","hostname":"no145.nordvpn.com","status":"online","load":6,"ips":[{"id":917210,"created_at":"2023-06-06 12:10:06","updated_at":"2023-06-06 12:10:06","server_id":956615,"ip_id":106580,"type":"entry","ip":{"id":106580,"ip":"37.120.203.195","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956618,"created_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 07:16:36","name":"Norway #146","station":"37.120.203.203","ipv6_station":"","hostname":"no146.nordvpn.com","status":"online","load":9,"ips":[{"id":917168,"created_at":"2023-06-06 12:09:17","updated_at":"2023-06-06 12:09:17","server_id":956618,"ip_id":106586,"type":"entry","ip":{"id":106586,"ip":"37.120.203.203","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956621,"created_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 07:16:36","name":"Norway #147","station":"37.120.203.211","ipv6_station":"","hostname":"no147.nordvpn.com","status":"online","load":7,"ips":[{"id":917126,"created_at":"2023-06-06 12:08:21","updated_at":"2023-06-06 12:08:21","server_id":956621,"ip_id":106592,"type":"entry","ip":{"id":106592,"ip":"37.120.203.211","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956624,"created_at":"2020-03-05 13:10:50","updated_at":"2025-02-24 07:16:36","name":"Norway #148","station":"37.120.203.219","ipv6_station":"","hostname":"no148.nordvpn.com","status":"online","load":9,"ips":[{"id":917084,"created_at":"2023-06-06 12:07:34","updated_at":"2023-06-06 12:07:34","server_id":956624,"ip_id":106598,"type":"entry","ip":{"id":106598,"ip":"37.120.203.219","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956627,"created_at":"2020-03-05 13:10:50","updated_at":"2025-02-24 07:16:36","name":"Norway #149","station":"95.174.66.27","ipv6_station":"","hostname":"no149.nordvpn.com","status":"online","load":7,"ips":[{"id":917042,"created_at":"2023-06-06 12:07:05","updated_at":"2023-06-06 12:07:05","server_id":956627,"ip_id":106604,"type":"entry","ip":{"id":106604,"ip":"95.174.66.27","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956636,"created_at":"2020-03-06 10:50:34","updated_at":"2025-02-24 07:08:37","name":"United Kingdom #1785","station":"194.35.233.75","ipv6_station":"","hostname":"uk1785.nordvpn.com","status":"online","load":13,"ips":[{"id":1031597,"created_at":"2023-07-19 06:16:16","updated_at":"2023-07-19 06:16:16","server_id":956636,"ip_id":70750,"type":"entry","ip":{"id":70750,"ip":"194.35.233.75","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[45]},{"id":956693,"created_at":"2020-03-10 11:07:25","updated_at":"2025-02-24 07:12:36","name":"Hungary #49","station":"217.138.192.83","ipv6_station":"","hostname":"hu49.nordvpn.com","status":"online","load":6,"ips":[{"id":1038770,"created_at":"2023-07-19 09:30:35","updated_at":"2023-07-19 09:30:35","server_id":956693,"ip_id":86595,"type":"entry","ip":{"id":86595,"ip":"217.138.192.83","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejXY="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[247]},{"id":956696,"created_at":"2020-03-10 12:25:51","updated_at":"2025-02-24 07:16:36","name":"France #536","station":"217.138.207.139","ipv6_station":"","hostname":"fr536.nordvpn.com","status":"online","load":12,"ips":[{"id":966083,"created_at":"2023-06-27 13:02:36","updated_at":"2023-06-27 13:02:36","server_id":956696,"ip_id":107162,"type":"entry","ip":{"id":107162,"ip":"217.138.207.139","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956699,"created_at":"2020-03-10 12:25:51","updated_at":"2025-02-24 07:16:36","name":"France #537","station":"217.138.207.147","ipv6_station":"","hostname":"fr537.nordvpn.com","status":"online","load":9,"ips":[{"id":966116,"created_at":"2023-06-27 13:02:44","updated_at":"2023-06-27 13:02:44","server_id":956699,"ip_id":107168,"type":"entry","ip":{"id":107168,"ip":"217.138.207.147","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956702,"created_at":"2020-03-10 12:25:51","updated_at":"2025-02-24 07:16:36","name":"France #538","station":"217.138.207.155","ipv6_station":"","hostname":"fr538.nordvpn.com","status":"online","load":12,"ips":[{"id":966149,"created_at":"2023-06-27 13:02:52","updated_at":"2023-06-27 13:02:52","server_id":956702,"ip_id":107174,"type":"entry","ip":{"id":107174,"ip":"217.138.207.155","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956705,"created_at":"2020-03-10 12:25:52","updated_at":"2025-02-24 07:16:36","name":"France #539","station":"217.138.207.163","ipv6_station":"","hostname":"fr539.nordvpn.com","status":"online","load":17,"ips":[{"id":966182,"created_at":"2023-06-27 13:02:59","updated_at":"2023-06-27 13:02:59","server_id":956705,"ip_id":107180,"type":"entry","ip":{"id":107180,"ip":"217.138.207.163","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956708,"created_at":"2020-03-10 12:25:52","updated_at":"2025-02-24 07:16:36","name":"France #540","station":"217.138.207.195","ipv6_station":"","hostname":"fr540.nordvpn.com","status":"online","load":11,"ips":[{"id":966215,"created_at":"2023-06-27 13:03:07","updated_at":"2023-06-27 13:03:07","server_id":956708,"ip_id":107186,"type":"entry","ip":{"id":107186,"ip":"217.138.207.195","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956711,"created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 07:16:36","name":"France #541","station":"217.138.207.203","ipv6_station":"","hostname":"fr541.nordvpn.com","status":"online","load":13,"ips":[{"id":966248,"created_at":"2023-06-27 13:03:16","updated_at":"2023-06-27 13:03:16","server_id":956711,"ip_id":107192,"type":"entry","ip":{"id":107192,"ip":"217.138.207.203","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956714,"created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 07:12:36","name":"France #542","station":"217.138.207.171","ipv6_station":"","hostname":"fr542.nordvpn.com","status":"online","load":17,"ips":[{"id":966281,"created_at":"2023-06-27 13:03:24","updated_at":"2023-06-27 13:03:24","server_id":956714,"ip_id":107198,"type":"entry","ip":{"id":107198,"ip":"217.138.207.171","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956717,"created_at":"2020-03-10 12:25:54","updated_at":"2025-02-24 07:16:36","name":"France #543","station":"217.138.207.179","ipv6_station":"","hostname":"fr543.nordvpn.com","status":"online","load":18,"ips":[{"id":966314,"created_at":"2023-06-27 13:03:35","updated_at":"2023-06-27 13:03:35","server_id":956717,"ip_id":107204,"type":"entry","ip":{"id":107204,"ip":"217.138.207.179","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956720,"created_at":"2020-03-10 12:25:54","updated_at":"2025-02-24 07:16:36","name":"France #544","station":"217.138.207.187","ipv6_station":"","hostname":"fr544.nordvpn.com","status":"online","load":17,"ips":[{"id":966347,"created_at":"2023-06-27 13:03:42","updated_at":"2023-06-27 13:03:42","server_id":956720,"ip_id":107210,"type":"entry","ip":{"id":107210,"ip":"217.138.207.187","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956732,"created_at":"2020-03-12 13:04:17","updated_at":"2025-02-24 07:16:36","name":"Switzerland #221","station":"91.132.136.235","ipv6_station":"","hostname":"ch221.nordvpn.com","status":"online","load":14,"ips":[{"id":938321,"created_at":"2023-06-19 10:48:33","updated_at":"2023-06-19 10:48:33","server_id":956732,"ip_id":107477,"type":"entry","ip":{"id":107477,"ip":"91.132.136.235","version":4}}],"specifications":[{"id":8,"title":"Version","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[107]}],"groups":[{"id":11,"created_at":"2017-06-13 13:43:00","updated_at":"2017-06-13 13:43:00","title":"Standard VPN servers","identifier":"legacy_standard","type":{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-13 13:40:23","title":"Legacy category","identifier":"legacy_group_category"}},{"id":15,"created_at":"2017-06-13 13:43:38","updated_at":"2017-06-13 13:43:38","title":"P2P","identifier":"legacy_p2p","type":{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-13 13:40:23","title":"Legacy category","identifier":"legacy_group_category"}},{"id":19,"created_at":"2017-10-27 14:17:17","updated_at":"2017-10-27 14:17:17","title":"Europe","identifier":"europe","type":{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"2017-10-27 14:16:30","title":"Regions","identifier":"regions"}},{"id":21,"created_at":"2017-10-27 14:23:03","updated_at":"2017-10-30 08:09:48","title":"The Americas","identifier":"the_americas","type":{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"2017-10-27 14:16:30","title":"Regions","identifier":"regions"}},{"id":9,"created_at":"2017-06-13 13:42:36","updated_at":"2018-08-22 12:54:48","title":"Dedicated IP","identifier":"legacy_dedicated_ip","type":{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-13 13:40:23","title":"Legacy category","identifier":"legacy_group_category"}},{"id":23,"created_at":"2017-10-27 14:23:51","updated_at":"2017-10-30 08:09:57","title":"Asia Pacific","identifier":"asia_pacific","type":{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"2017-10-27 14:16:30","title":"Regions","identifier":"regions"}}],"services":[{"id":1,"name":"VPN","identifier":"vpn","created_at":"2017-03-21 12:00:45","updated_at":"2017-05-25 13:12:31"},{"id":5,"name":"Proxy","identifier":"proxy","created_at":"2017-05-29 19:38:30","updated_at":"2017-05-29 19:38:30"}],"locations":[{"id":367,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":52.25,"longitude":21,"country":{"id":174,"name":"Poland","code":"PL","city":{"id":6863429,"name":"Warsaw","latitude":52.25,"longitude":21,"dns_name":"warsaw","hub_score":0}}},{"id":247,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":47.5,"longitude":19.083333,"country":{"id":98,"name":"Hungary","code":"HU","city":{"id":3348344,"name":"Budapest","latitude":47.5,"longitude":19.083333,"dns_name":"budapest","hub_score":0}}},{"id":51,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":34.0522222,"longitude":-118.2427778,"country":{"id":228,"name":"United States","code":"US","city":{"id":8761958,"name":"Los Angeles","latitude":34.0522222,"longitude":-118.2427778,"dns_name":"los-angeles","hub_score":0}}},{"id":205,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":48.2,"longitude":16.366667,"country":{"id":14,"name":"Austria","code":"AT","city":{"id":448799,"name":"Vienna","latitude":48.2,"longitude":16.366667,"dns_name":"vienna","hub_score":0}}},{"id":107,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":47.366667,"longitude":8.55,"country":{"id":209,"name":"Switzerland","code":"CH","city":{"id":1171814,"name":"Zurich","latitude":47.366667,"longitude":8.55,"dns_name":"zurich","hub_score":0}}},{"id":169,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":55.666667,"longitude":12.583333,"country":{"id":58,"name":"Denmark","code":"DK","city":{"id":2382515,"name":"Copenhagen","latitude":55.666667,"longitude":12.583333,"dns_name":"copenhagen","hub_score":0}}},{"id":97,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":59.916667,"longitude":10.75,"country":{"id":163,"name":"Norway","code":"NO","city":{"id":6127364,"name":"Oslo","latitude":59.916667,"longitude":10.75,"dns_name":"oslo","hub_score":0}}},{"id":45,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":51.514125,"longitude":-0.093689,"country":{"id":227,"name":"United Kingdom","code":"GB","city":{"id":2989907,"name":"London","latitude":51.514125,"longitude":-0.093689,"dns_name":"london","hub_score":0}}},{"id":87,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":48.866667,"longitude":2.333333,"country":{"id":74,"name":"France","code":"FR","city":{"id":2886284,"name":"Paris","latitude":48.866667,"longitude":2.333333,"dns_name":"paris","hub_score":0}}},{"id":133,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":50.116667,"longitude":8.683333,"country":{"id":81,"name":"Germany","code":"DE","city":{"id":2215709,"name":"Frankfurt","latitude":50.116667,"longitude":8.683333,"dns_name":"frankfurt","hub_score":0}}},{"id":19,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":42.8863889,"longitude":-78.8786111,"country":{"id":228,"name":"United States","code":"US","city":{"id":8963153,"name":"Buffalo","latitude":42.8863889,"longitude":-78.8786111,"dns_name":"buffalo","hub_score":0}}},{"id":3990,"created_at":"2018-06-18 14:58:07","updated_at":"2018-06-18 14:58:07","latitude":50.833333,"longitude":4.333333,"country":{"id":21,"name":"Belgium","code":"BE","city":{"id":654293,"name":"Brussels","latitude":50.833333,"longitude":4.333333,"dns_name":"brussels","hub_score":0}}},{"id":79,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":32.7833333,"longitude":-96.8,"country":{"id":228,"name":"United States","code":"US","city":{"id":9080300,"name":"Dallas","latitude":32.7833333,"longitude":-96.8,"dns_name":"dallas","hub_score":0}}},{"id":5,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":52.35,"longitude":4.916667,"country":{"id":153,"name":"Netherlands","code":"NL","city":{"id":6076868,"name":"Amsterdam","latitude":52.35,"longitude":4.916667,"dns_name":"amsterdam","hub_score":0}}},{"id":3984,"created_at":"2018-06-18 14:45:14","updated_at":"2018-06-18 14:45:14","latitude":35.685,"longitude":139.751389,"country":{"id":108,"name":"Japan","code":"JP","city":{"id":4633349,"name":"Tokyo","latitude":35.685,"longitude":139.751389,"dns_name":"tokyo","hub_score":0}}},{"id":113,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":40.408566,"longitude":-3.69222,"country":{"id":202,"name":"Spain","code":"ES","city":{"id":2619989,"name":"Madrid","latitude":40.408566,"longitude":-3.69222,"dns_name":"madrid","hub_score":0}}},{"id":3978,"created_at":"2018-06-18 11:48:51","updated_at":"2018-06-18 11:48:51","latitude":45.466667,"longitude":9.2,"country":{"id":106,"name":"Italy","code":"IT","city":{"id":4542737,"name":"Milan","latitude":45.466667,"longitude":9.2,"dns_name":"milan","hub_score":0}}},{"id":305,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":40.7141667,"longitude":-74.0063889,"country":{"id":228,"name":"United States","code":"US","city":{"id":8971718,"name":"New York","latitude":40.7141667,"longitude":-74.0063889,"dns_name":"new-york","hub_score":0}}},{"id":143,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":50.083333,"longitude":14.466667,"country":{"id":57,"name":"Czech Republic","code":"CZ","city":{"id":2144945,"name":"Prague","latitude":50.083333,"longitude":14.466667,"dns_name":"prague","hub_score":0}}},{"id":65,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":44.433333,"longitude":26.1,"country":{"id":179,"name":"Romania","code":"RO","city":{"id":6953096,"name":"Bucharest","latitude":44.433333,"longitude":26.1,"dns_name":"bucharest","hub_score":0}}},{"id":259,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":42.6833333,"longitude":23.3166667,"country":{"id":33,"name":"Bulgaria","code":"BG","city":{"id":777368,"name":"Sofia","latitude":42.6833333,"longitude":23.3166667,"dns_name":"sofia","hub_score":0}}}],"technologies":[{"id":1,"name":"IKEv2/IPSec","identifier":"ikev2","created_at":"2017-03-21 12:00:24","updated_at":"2017-09-05 14:20:16","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":3,"name":"OpenVPN UDP","identifier":"openvpn_udp","created_at":"2017-05-04 08:03:24","updated_at":"2017-05-09 19:27:37","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":5,"name":"OpenVPN TCP","identifier":"openvpn_tcp","created_at":"2017-05-09 19:28:14","updated_at":"2017-05-09 19:28:14","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":21,"name":"HTTP Proxy (SSL)","identifier":"proxy_ssl","created_at":"2017-10-02 12:45:14","updated_at":"2017-10-02 12:45:14","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":23,"name":"HTTP CyberSec Proxy (SSL)","identifier":"proxy_ssl_cybersec","created_at":"2017-10-02 12:50:49","updated_at":"2017-10-02 12:50:49","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":35,"name":"Wireguard","identifier":"wireguard_udp","created_at":"2019-02-14 14:08:43","updated_at":"2019-02-14 14:08:43","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":51,"name":"NordWhisper","identifier":"nordwhisper","created_at":"2024-10-07 10:17:17","updated_at":"2024-10-07 10:17:17","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":42,"name":"OpenVPN UDP Dedicated","identifier":"openvpn_dedicated_udp","created_at":"2019-09-19 14:49:18","updated_at":"2019-09-19 14:49:18","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id":45,"name":"OpenVPN TCP Dedicated","identifier":"openvpn_dedicated_tcp","created_at":"2019-09-19 14:49:54","updated_at":"2019-09-19 14:49:54","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status":""}}]}

---

_**Assistant**_

<think>I need to analyze the user's query and the NordVPN API response to understand what's causing the validation issues. Let's break this down:

1. The user is reporting Pydantic validation errors about missing fields in the API response. Specifically, these errors are related to:
   - `technologies.3.created_at` and `technologies.3.updated_at` for objects with `id: 42`
   - `technologies.4.name`, `technologies.4.identifier`, `technologies.4.created_at` and `technologies.4.updated_at` for objects with `id: 45`

2. The user provided an API response from `https://api.nordvpn.com/v2/servers` showing the actual structure of data returned by the NordVPN API.

Looking at the API response, we can see that the `technologies` array in the response contains objects with some, but not all, of the fields that are required by the `Technology` TypedDict in our code.

Taking a specific example from the API response:
```json
"technologies":[
  {"id":3,"status":"online"},
  {"id":5,"status":"online"},
  {"id":35,"metadata":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},
  {"id":42,"status":"online"},
  {"id":45,"status":"online"}
]
```

Notice that most of the technology objects just have `id` and `status`, but our `Technology` TypedDict in the code is requiring more fields.

Looking at the current `Technology` TypedDict in the code:

```python
class Technology(TypedDict):
    """Server technology information."""
    id: int
    status: str
    metadata: NotRequired[list[TechnologyMetadata]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
```

We've already made `created_at` and `updated_at` optional using `NotRequired`, but we're still getting validation errors. It seems that the server data we're getting for technologies with IDs 42 and 45 is missing more fields that what we're expecting.

The error messages mention fields like `name` and `identifier` which should also be added as optional fields in the `Technology` TypedDict.

We need to update our `Technology` TypedDict to make more fields optional to better match the actual API response structure.

Also, looking at the full API response, there's a `technologies` array at the end of the response that contains the complete information about each technology, including `name`, `identifier`, `created_at`, etc. This suggests that the API is separating the technology definitions (full objects with all fields) from the technology references used in the server objects (which only contain minimal information).

Let's modify the `Technology` TypedDict to make all fields except `id` and `status` optional, which should resolve the validation errors:

```python
class Technology(TypedDict):
    """Server technology information."""
    id: int
    status: str
    name: NotRequired[str]
    identifier: NotRequired[str]
    metadata: NotRequired[list[TechnologyMetadata]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
```

This should allow the TypedDict to handle the minimal technology objects that only have `id` and `status`.</think>Looking at the API response from `https://api.nordvpn.com/v2/servers`, I can see the source of the validation errors. The `technologies` arrays in the server entries only contain minimal information, with many technologies missing the required fields. I need to update the `Technology` TypedDict to accommodate the actual structure of the API response.

Let's modify the `Technology` TypedDict to make all fields except `id` and `status` optional:

---

_****_

```diff
      id: int
      status: str
+     name: NotRequired[str]
+     identifier: NotRequired[str]
      metadata: NotRequired[list[TechnologyMetadata]]
      created_at: NotRequired[str]
```

---

_****_



---



---

