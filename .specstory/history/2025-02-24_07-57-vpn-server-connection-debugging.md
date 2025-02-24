## SpecStory

## VPN Server Connection Debugging (24/02/2025, 07:57:13)

_**User**_

[02/24/25 07:56:29] DEBUG    2025-02-24 07:56:29.674 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 07:56:29.678 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 07:56:29.681 | DEBUG    | nyord_vpn.network.server:get_servers_cache:305 - Fetching server list from API...      server.py:305
[02/24/25 07:56:30] DEBUG    2025-02-24 07:56:30.001 | DEBUG    | nyord_vpn.network.server:get_servers_cache:317 - Successfully fetched server data from server.py:317
                             API                                                                                                                                      
                    DEBUG    2025-02-24 07:56:30.003 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response     server.py:325
                    DEBUG    2025-02-24 07:56:30.239 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl128.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:30.240 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.242 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.244 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.245 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
...                                       
                    DEBUG    2025-02-24 07:56:30.417 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 07:56:30.418 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.420 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:30.421 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk873.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:30.422 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
...
                    DEBUG    2025-02-24 07:56:30.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 07:56:30.717 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for nl409.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:30.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.722 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 07:56:30.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 07:56:30.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de676.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:30.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:30.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
...Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.712 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:31.713 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk814.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:31.715 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.717 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:31.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 07:56:31.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:31.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk871.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:31.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:31.727 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                ...                                                           
                    DEBUG    2025-02-24 07:56:32.597 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:32.598 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch221.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 07:56:32.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:32.601 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:32.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:32.603 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:32.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 07:56:32.606 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 07:56:32.608 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 07:56:32.610 | DEBUG    | nyord_vpn.network.server:get_servers_cache:446 - No valid servers found after          server.py:446
                             filtering 100 total servers                                                                                                              
                    ERROR    2025-02-24 07:56:32.612 | ERROR    | nyord_vpn.network.server:get_servers_cache:476 - Failed to fetch servers: No valid     server.py:476
                             servers found in API response. Total servers: 100, Invalid: 100                                                                          
                             Traceback (most recent call last):                                                                                                       
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/bin/nyord-vpn", line 10, in <module>                               
                                 sys.exit(main())                                                                                                                     
                                 |   |    -> <function main at 0x108efb880>                                                                                           
                                 |   -> <built-in function exit>                                                                                                      
                                 -> <module 'sys' (built-in)>                                                                                                         
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 81, in main                             
                                 fire.Fire(CLI)                                                                                                                       
                                 |    |    -> <class 'nyord_vpn.__main__.CLI'>                                                                                        
                                 |    -> <function Fire at 0x108fa1260>                                                                                               
                                 -> <module 'fire' from                                                                                                               
                             '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/__init__...                             
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 135,              
                             in Fire                                                                                                                                  
                                 component_trace = _Fire(component, args, parsed_flag_args, context, name)                                                            
                                                   |     |          |     |                 |        -> 'nyord-vpn'                                                   
                                                   |     |          |     |                 -> {}                                                                     
                                                   |     |          |     -> Namespace(verbose=False, interactive=False, separator='-', completion=None,              
                             help=False, trace=False)                                                                                                                 
                                                   |     |          -> ['go', 'pl', '--verbose']                                                                      
                                                   |     -> <class 'nyord_vpn.__main__.CLI'>                                                                          
                                                   -> <function _Fire at 0x108fc2a20>                                                                                 
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 468,              
                             in _Fire                                                                                                                                 
                                 component, remaining_args = _CallAndUpdateTrace(                                                                                     
                                 |                           -> <function _CallAndUpdateTrace at 0x108fc2b60>                                                         
                                 -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x10915e1e0>>                                                           
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 684,              
                             in _CallAndUpdateTrace                                                                                                                   
                                 component = fn(*varargs, **kwargs)                                                                                                   
                                             |   |          -> {}                                                                                                     
                                             |   -> ['pl']                                                                                                            
                                             -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x10915e1e0>>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 46, in go                               
                                 self.client.go(country_code)                                                                                                         
                                 |    |      |  -> 'pl'                                                                                                               
                                 |    |      -> <function Client.go at 0x108efb2e0>                                                                                   
                                 |    -> <nyord_vpn.core.client.Client object at 0x10915e240>                                                                         
                                 -> <nyord_vpn.__main__.CLI object at 0x10915e1e0>                                                                                    
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 278, in go                           
                                 selected_servers = self.server_manager.select_fastest_server(                                                                        
                                                    |    |              -> <function ServerManager.select_fastest_server at 0x108e83920>                              
                                                    |    -> <nyord_vpn.network.server.ServerManager object at 0x108d269f0>                                            
                                                    -> <nyord_vpn.core.client.Client object at 0x10915e240>                                                           
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 835, in                           
                             select_fastest_server                                                                                                                    
                                 normalized_country = self._validate_country_code(country_code)                                                                       
                                                      |    |                      -> 'pl'                                                                             
                                                      |    -> <function ServerManager._validate_country_code at 0x108e834c0>                                          
                                                      -> <nyord_vpn.network.server.ServerManager object at 0x108d269f0>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 175, in                           
                             _validate_country_code                                                                                                                   
                                 country_info = self.get_country_info(normalized)                                                                                     
                                                |    |                -> 'PL'                                                                                         
                                                |    -> <function ServerManager.get_country_info at 0x108e83b00>                                                      
                                                -> <nyord_vpn.network.server.ServerManager object at 0x108d269f0>                                                     
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 1018, in                          
                             get_country_info                                                                                                                         
                                 cache = self.get_servers_cache()                                                                                                     
                                         |    -> <function ServerManager.get_servers_cache at 0x108e83600>                                                            
                                         -> <nyord_vpn.network.server.ServerManager object at 0x108d269f0>                                                            
                                                                                                                                                                      
                             > File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 449, in                           
                             get_servers_cache                                                                                                                        
                                 raise ValueError(                                                                                                                    
                                                                                                                                                                      
                             ValueError: No valid servers found in API response. Total servers: 100, Invalid: 100                                                     
                                                                                                                                                                      
                                                                                                                                                                      
                    INFO     2025-02-24 07:56:32.626 | INFO     | nyord_vpn.network.server:get_servers_cache:490 - Using fallback cache with 100 valid   server.py:490
                             servers                                                                                                                                  
                    DEBUG    2025-02-24 07:56:32.628 | DEBUG    | nyord_vpn.network.server:select_fastest_server:883 - Testing 3 servers for speed       server.py:883
                    DEBUG    2025-02-24 07:56:32.845 | DEBUG    | nyord_vpn.network.server:_test_server:683 - TCP/TLS test failed for pl125.nordvpn.com: server.py:683
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 07:56:32.847 | DEBUG    | nyord_vpn.network.server:_test_server:683 - TCP/TLS test failed for pl128.nordvpn.com: server.py:683
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 07:56:32.863 | DEBUG    | nyord_vpn.network.server:_test_server:683 - TCP/TLS test failed for pl122.nordvpn.com: server.py:683
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    ERROR    2025-02-24 07:56:32.867 | ERROR    | nyord_vpn.network.server:select_fastest_server:927 - Error selecting server: No        server.py:927
                             responsive servers found in PL                                                                                                           
Error: Failed to select servers: No responsive servers found in PL

Bullshit. Why are there "technologies" from UK and NL if we’re trying to connect to PL? 

---

_**Assistant**_

Let me analyze the logs and the issue you've pointed out.

The problem appears to be in the server selection and filtering logic. Let's break down what's happening:

1. First, the code successfully fetches server data from the API and gets 100 servers
2. However, it's logging technologies for servers from multiple countries (pl, uk, nl, ch, etc.) even though you specifically requested 'pl'
3. The error shows that all 100 servers are being marked as invalid: `No valid servers found in API response. Total servers: 100, Invalid: 100`
4. Then it falls back to a cache with 100 servers but still fails with TCP/TLS tests

Let me check the server filtering code:

---

_****_

<details>
            <summary>Searched codebase "get_servers_cache filter servers by country" • **25** results</summary>
        
| File | Lines |
|------|-------|
| `src/nyord_vpn/network/server.py` | L329-358 |
| `src/nyord_vpn/network/server.py` | L827-871 |
| `src/nyord_vpn/network/server.py` | L401-442 |
| `src/nyord_vpn/network/server.py` | L442-473 |
| `src/nyord_vpn/network/server.py` | L966-995 |
| `src/nyord_vpn/network/server.py` | L995-1054 |
| `src/nyord_vpn/network/server.py` | L911-966 |
| `src/nyord_vpn/network/server.py` | L244-275 |
| `src/nyord_vpn/network/server.py` | L358-401 |
| `src/nyord_vpn/network/server.py` | L207-244 |
| `src/nyord_vpn/network/server.py` | L275-301 |
| `src/nyord_vpn/network/server.py` | L301-329 |
| `src/nyord_vpn/network/server.py` | L117-152 |
| `src/nyord_vpn/network/server.py` | L473-497 |
| `src/nyord_vpn/network/server.py` | L179-207 |
| `src/nyord_vpn/network/server.py` | L1-70 |
| `src/nyord_vpn/network/server.py` | L733-785 |
| `src/nyord_vpn/network/server.py` | L785-827 |
| `src/nyord_vpn/network/server.py` | L598-645 |
| `src/nyord_vpn/network/server.py` | L152-179 |
| `src/nyord_vpn/network/server.py` | L871-911 |
| `src/nyord_vpn/network/server.py` | L104-117 |
| `src/nyord_vpn/network/server.py` | L645-687 |
| `src/nyord_vpn/network/server.py` | L83-104 |
| `src/nyord_vpn/network/server.py` | L70-83 |

</details>

---

_****_



After reviewing the code, I can see the issue. The problem is in the server validation logic. Let me check the specific part where servers are being filtered:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue now. The problem is in the server validation logic. Let me check the server filtering code:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the problem now. The code is looking for a technology with name exactly "OpenVPN TCP", but in the logs we can see that the actual technology names are:

1. "OpenVPN UDP"
2. "OpenVPN TCP"
3. "OpenVPN TCP Dedicated"

The code needs to be modified to accept any technology name that CONTAINS "OpenVPN TCP" rather than requiring an exact match. Let me fix this:

---

_****_

```diff
                      if (
                          isinstance(tech, dict)
-                         and tech.get("name") == "OpenVPN TCP"
+                         and isinstance(tech.get("name"), str)
+                         and "OpenVPN TCP" in tech.get("name", "")
                      ):
                          has_openvpn_tcp = True
```

---

_****_



This change should fix the issue. The code will now:

1. Check that the technology name is a string
2. Check if it contains "OpenVPN TCP" anywhere in the name
3. This will match both regular "OpenVPN TCP" and "OpenVPN TCP Dedicated" servers

Let me also add some additional logging to help diagnose these issues in the future:

---

_****_

```diff
                  has_openvpn_tcp = False
                  for tech in server.get("technologies", []):
+                     tech_name = tech.get("name", "")
                      if (
                          isinstance(tech, dict)
-                         and isinstance(tech.get("name"), str)
-                         and "OpenVPN TCP" in tech.get("name", "")
+                         and isinstance(tech_name, str)
+                         and "OpenVPN TCP" in tech_name
                      ):
+                         if self.api_client.verbose:
+                             self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")
                          has_openvpn_tcp = True
                          break
                      if self.api_client.verbose:
                          self.logger.debug(
-                             f"Skipping server without OpenVPN TCP: {server.get('hostname')}"
+                             f"Skipping server without OpenVPN TCP: {server.get('hostname')}. "
+                             f"Available technologies: {[t.get('name') for t in server.get('technologies', [])]}"
                          )
                      continue
```

---

_****_



These changes will:

1. Fix the OpenVPN TCP detection by matching any technology name containing "OpenVPN TCP"
2. Add more detailed logging showing:
   - When OpenVPN TCP support is found and what type it is
   - When a server is skipped, showing all available technologies

The issue should be resolved now. The code will properly detect both regular OpenVPN TCP and OpenVPN TCP Dedicated servers, and provide better logging to help diagnose any similar issues in the future.

Wait, but let me also check if there are any other places in the code that might need similar fixes:

---

_****_

<details>
            <summary>Grep search for "OpenVPN TCP" • **12** files</summary>
        
| File | Line | Match |
|------|------|-------|
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6209 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6244 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6325 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6507 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6527 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L724 | `+                 if any(tech["name"] == "OpenVPN TCP" for tech in server["technologies"])` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L760 | `2. Moved the OpenVPN TCP filtering to Python code instead of API parameters` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L829 | `-                 if any(tech["name"] == "OpenVPN TCP" for tech in server["technologies"])` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L845 | `+             # Filter for OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L881 | `- Then filter for OpenVPN TCP support in the code` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L1069 | `-             # Filter for OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L19 | `DEBUG    2025-02-24 07:56:30.244 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L34 | `DEBUG    2025-02-24 07:56:30.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L39 | `DEBUG    2025-02-24 07:56:30.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L45 | `DEBUG    2025-02-24 07:56:30.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L50 | `DEBUG    2025-02-24 07:56:30.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L61 | `DEBUG    2025-02-24 07:56:31.717 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L83 | `DEBUG    2025-02-24 07:56:32.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L275 | `I see the problem now. The code is looking for a technology with name exactly "OpenVPN TCP", but in the logs we can see that the actual technology names are:` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L278 | `2. "OpenVPN TCP"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L279 | `3. "OpenVPN TCP Dedicated"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L281 | `The code needs to be modified to accept any technology name that CONTAINS "OpenVPN TCP" rather than requiring an exact match. Let me fix this:` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_02-15-python-virtual-environment-setup-and-testing.md` | L6075 | `>       if any(tech["name"] == "OpenVPN TCP" for tech in server["t` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L452 | `+         id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L528 | `+         1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L2159 | `+ 4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-22_20-24-managing-todos-and-development-tasks.md` | L2794 | `if any(tech["name"] == "OpenVPN TCP" for tech in serve` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-09-executing-python-vpn-connection-command.md` | L4080 | `2. Filter for online OpenVPN TCP servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2766 | `2. Added filtering for OpenVPN TCP servers in the API request` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2849 | `+                 # Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3441 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3453 | `+                             f"Skipping server without OpenVPN TCP: {server.get('hostname')}"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L11308 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L11322 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L41 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L76 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L184 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L363 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L382 | `and "OpenVPN TCP" in tech_name` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L385 | `self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L392 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}. "` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L863 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L865 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L867 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L869 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L871 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L873 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L875 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L877 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L879 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L881 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L883 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L885 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L887 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L889 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L891 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L893 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L895 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L897 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L899 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L901 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L903 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L905 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L907 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L909 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L911 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L913 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L915 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L917 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L919 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L921 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L923 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L925 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L927 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L929 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L931 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L933 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L935 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L937 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L939 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L941 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L943 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L945 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L947 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L949 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L951 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L953 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L955 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L957 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L959 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L961 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L963 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L965 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L967 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L969 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L971 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L973 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L975 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L977 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-36-fixing-importerror-in-nyord-vpn-code.md` | L979 | `⟪ 99 characters skipped ⟫ers_cache:382 - Skipping server without OpenVPN TCP:  server.py:382` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L41 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L76 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L184 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L363 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L382 | `and "OpenVPN TCP" in tech_name` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L385 | `self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L392 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}. "` |

</details>

---

_****_



Let me check the `fetch_server_info` method as well since it also deals with OpenVPN TCP:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



The `fetch_server_info` method uses the API's built-in filtering with `filters[servers_technologies][identifier]": "openvpn_tcp"`, which is correct. The API handles this properly and returns both regular and dedicated OpenVPN TCP servers.

So the only place that needed fixing was the local server validation in `get_servers_cache`. The changes we made should resolve the issue.

To summarize what was happening:

1. The code was fetching servers from the API correctly
2. The API was returning servers with both regular "OpenVPN TCP" and "OpenVPN TCP Dedicated" technologies
3. The local validation in `get_servers_cache` was too strict, only accepting exact matches for "OpenVPN TCP"
4. This caused all servers to be marked as invalid since none matched exactly
5. We fixed this by changing the check to look for "OpenVPN TCP" as a substring
6. We also added more detailed logging to help diagnose similar issues

The code should now work correctly with both regular and dedicated OpenVPN TCP servers. Try running it again and it should properly detect and use the available servers.

Wait, but let me also check if we need to update any tests to match this change:

---

_****_

<details>
            <summary>Searched codebase "test OpenVPN TCP server validation" • **25** results</summary>
        
| File | Lines |
|------|-------|
| `tests/test_legacy_api.py` | L79-87 |
| `tests/conftest.py` | L15-23 |
| `tests/test_legacy_api.py` | L48-58 |
| `tests/test_client.py` | L1-19 |
| `tests/test_legacy_api.py` | L73-79 |
| `tests/conftest.py` | L35-44 |
| `tests/integration/test_errors.py` | L47-70 |
| `tests/test_client.py` | L19-33 |
| `tests/integration/test_config_loading.py` | L165-212 |
| `tests/integration/test_validation_integration.py` | L30-39 |
| `tests/integration/test_validation_integration.py` | L18-24 |
| `tests/conftest.py` | L44-67 |
| `tests/test_legacy_api.py` | L1-17 |
| `tests/integration/test_connection.py` | L1-36 |
| `tests/test_legacy_api.py` | L42-48 |
| `tests/test_legacy_api.py` | L17-29 |
| `tests/integration/test_errors.py` | L277-294 |
| `tests/test_legacy_api.py` | L29-42 |
| `tests/integration/test_connection.py` | L67-91 |
| `tests/test_client.py` | L56-73 |
| `tests/test_client.py` | L42-56 |
| `tests/integration/test_errors.py` | L184-192 |
| `tests/test_legacy_api.py` | L58-73 |
| `tests/test_legacy_api.py` | L97-107 |
| `tests/integration/test_errors.py` | L1-47 |

</details>

---

_****_



Let me also check if there are any tests specifically for the server manager:

---

_****_

<details>
            <summary>Searched codebase "test server manager OpenVPN technology validation" • **25** results</summary>
        
| File | Lines |
|------|-------|
| `tests/test_legacy_api.py` | L79-87 |
| `tests/conftest.py` | L15-23 |
| `tests/test_legacy_api.py` | L48-58 |
| `tests/test_client.py` | L1-19 |
| `tests/conftest.py` | L35-44 |
| `tests/test_client.py` | L56-73 |
| `tests/conftest.py` | L44-67 |
| `tests/test_legacy_api.py` | L73-79 |
| `tests/integration/test_errors.py` | L47-70 |
| `tests/test_client.py` | L19-33 |
| `tests/test_legacy_api.py` | L42-48 |
| `tests/integration/test_validation_integration.py` | L30-39 |
| `tests/test_legacy_api.py` | L1-17 |
| `tests/integration/test_validation_integration.py` | L18-24 |
| `tests/test_client.py` | L42-56 |
| `tests/integration/test_connection.py` | L1-36 |
| `tests/test_legacy_api.py` | L17-29 |
| `tests/test_legacy_api.py` | L29-42 |
| `tests/integration/test_config_loading.py` | L262-281 |
| `tests/integration/test_connection.py` | L67-91 |
| `tests/integration/test_config_loading.py` | L165-212 |
| `tests/test_legacy_api.py` | L97-107 |
| `tests/test_legacy_api.py` | L87-97 |
| `tests/integration/test_errors.py` | L277-294 |
| `tests/integration/test_errors.py` | L184-192 |

</details>

---

_****_



I see that we don't have any specific tests for the server manager's technology validation. Let me add some:

---

_****_

```diff
- 
+ #!/usr/bin/env -S uv run -s
+ # /// script
+ # dependencies = ["pytest"]
+ # ///
+ # this_file: tests/test_server_manager.py
+ 
+ """Tests for server manager functionality."""
+ 
+ import pytest
+ from unittest.mock import MagicMock
+ 
+ from nyord_vpn.network.server import ServerManager
+ from nyord_vpn.core.api import NordVPNAPIClient
+ 
+ 
+ @pytest.fixture
+ def mock_api_client():
+     """Create a mock API client."""
+     client = MagicMock(spec=NordVPNAPIClient)
+     client.verbose = True
+     client.logger = MagicMock()
+     return client
+ 
+ 
+ @pytest.fixture
+ def server_manager(mock_api_client):
+     """Create a server manager instance."""
+     return ServerManager(mock_api_client)
+ 
+ 
+ def test_openvpn_tcp_validation(server_manager):
+     """Test OpenVPN TCP technology validation."""
+     # Test regular OpenVPN TCP
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is True
+ 
+     # Test OpenVPN TCP Dedicated
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is True
+ 
+     # Test server without OpenVPN TCP
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 3, "name": "OpenVPN UDP", "status": "online"},
+             {"id": 35, "name": "Wireguard", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with invalid technology format
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 5},  # Missing name
+             {"name": "OpenVPN TCP"},  # Missing id
+             None,  # Invalid technology
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with empty technologies
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with invalid hostname
+     server = {
+         "hostname": "test.example.com",  # Not a nordvpn.com domain
+         "status": "online",
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with invalid status
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "offline",  # Should be online
+         "load": 50,
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with invalid load
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 150,  # Should be 0-100
+         "country": {"code": "US", "name": "United States"},
+         "technologies": [
+             {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False
+ 
+     # Test server with invalid country code
+     server = {
+         "hostname": "test.nordvpn.com",
+         "status": "online",
+         "load": 50,
+         "country": {"code": "USA", "name": "United States"},  # Should be 2 letters
+         "technologies": [
+             {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+         ],
+     }
+     assert server_manager._is_valid_server(server) is False 
```

---

_****_



I've created a new test file `tests/test_server_manager.py` that specifically tests the server validation logic, including:

1. Regular OpenVPN TCP servers
2. OpenVPN TCP Dedicated servers
3. Servers without OpenVPN TCP
4. Various invalid server configurations

Let me also add a test for the server filtering logic:

---

_****_

```diff
      }
      assert server_manager._is_valid_server(server) is False
+ 
+ 
+ def test_server_filtering(server_manager, mock_api_client):
+     """Test server filtering in get_servers_cache."""
+     # Mock API response with various server types
+     mock_api_client.get.return_value.json.return_value = [
+         {
+             "hostname": "tcp1.nordvpn.com",
+             "status": "online",
+             "load": 50,
+             "country": {"code": "US", "name": "United States"},
+             "technologies": [
+                 {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+             ],
+         },
+         {
+             "hostname": "tcp2.nordvpn.com",
+             "status": "online",
+             "load": 60,
+             "country": {"code": "US", "name": "United States"},
+             "technologies": [
+                 {"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},
+             ],
+         },
+         {
+             "hostname": "udp1.nordvpn.com",
+             "status": "online",
+             "load": 40,
+             "country": {"code": "US", "name": "United States"},
+             "technologies": [
+                 {"id": 3, "name": "OpenVPN UDP", "status": "online"},
+             ],
+         },
+         {
+             "hostname": "offline1.nordvpn.com",
+             "status": "offline",
+             "load": 30,
+             "country": {"code": "US", "name": "United States"},
+             "technologies": [
+                 {"id": 5, "name": "OpenVPN TCP", "status": "online"},
+             ],
+         },
+     ]
+ 
+     # Get filtered servers
+     cache = server_manager.get_servers_cache()
+     servers = cache.get("servers", [])
+ 
+     # Should only include online servers with OpenVPN TCP
+     assert len(servers) == 2
+     assert any(s["hostname"] == "tcp1.nordvpn.com" for s in servers)
+     assert any(s["hostname"] == "tcp2.nordvpn.com" for s in servers)
+ 
+     # Verify logging
+     mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP")
+     mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP Dedicated")
+     mock_api_client.logger.debug.assert_any_call(
+         "Skipping server without OpenVPN TCP: udp1.nordvpn.com. "
+         "Available technologies: ['OpenVPN UDP']"
+     ) 
```

---

_****_





I've added a test for the server filtering logic that:

1. Mocks an API response with various server types:
   - Regular OpenVPN TCP server
   - OpenVPN TCP Dedicated server
   - OpenVPN UDP server (should be filtered out)
   - Offline server (should be filtered out)

2. Verifies that only the appropriate servers are included:
   - Only online servers
   - Only servers with OpenVPN TCP or OpenVPN TCP Dedicated

3. Verifies that the correct logging messages are generated:
   - When OpenVPN TCP support is found
   - When a server is skipped due to missing OpenVPN TCP

Let me also fix the mock setup to properly handle the API calls:

---

_****_



---

_****_



---

_**User**_

[02/24/25 08:00:42] DEBUG    2025-02-24 08:00:42.886 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:00:42.895 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 08:00:42.899 | DEBUG    | nyord_vpn.network.server:get_servers_cache:305 - Fetching server list from API...      server.py:305
[02/24/25 08:00:43] DEBUG    2025-02-24 08:00:43.232 | DEBUG    | nyord_vpn.network.server:get_servers_cache:317 - Successfully fetched server data from server.py:317
                             API                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.234 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response     server.py:325
                    DEBUG    2025-02-24 08:00:43.466 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl128.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.467 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.469 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.470 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.472 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.473 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.475 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.476 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.479 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu48.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:43.480 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.481 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.483 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.484 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.485 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.487 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.488 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.491 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5063.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.492 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.493 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.496 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.498 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.499 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.501 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.503 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for at86.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:43.505 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.506 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.508 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.509 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.510 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.512 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.513 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.515 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch217.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.517 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.519 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.522 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.523 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.524 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.526 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.528 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for dk152.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.530 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.531 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.534 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.536 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.537 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.539 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no151.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.543 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.544 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.546 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.547 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.549 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.550 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.551 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.554 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch218.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.556 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.560 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.562 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.563 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.564 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.567 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1784.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.569 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.570 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.573 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.575 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.576 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.578 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.579 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr555.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.583 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.584 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.585 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.587 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.590 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.591 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.593 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.594 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch219.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.596 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.598 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.601 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.604 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.608 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5064.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.609 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.611 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.613 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.614 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.616 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.617 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.619 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.622 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk765.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.623 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.625 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.626 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.627 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.629 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.631 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.632 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.633 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.635 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk812.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.636 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.637 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.639 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.640 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.642 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.643 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.644 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk813.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.650 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.652 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.653 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.655 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.657 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.658 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.660 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.662 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.664 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk814.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.665 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.666 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.668 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.669 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.671 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.672 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.674 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.675 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.676 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk871.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.678 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.679 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.681 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.682 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.684 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.685 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.687 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.688 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.689 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk873.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.691 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.692 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.693 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.695 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.697 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.700 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.702 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.703 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk875.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.706 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.709 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.711 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.713 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.715 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de507.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.722 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.727 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.729 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.730 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de508.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.732 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.733 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.735 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.736 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.738 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.739 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de509.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.742 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.743 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.745 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.746 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.747 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.749 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de510.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.753 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.754 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.756 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.757 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.759 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.760 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk877.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.762 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.763 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.765 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.766 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.769 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.770 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.772 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.774 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2920.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.775 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.777 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.779 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.783 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.784 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.786 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2921.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.787 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.789 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.791 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.792 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.794 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:43.795 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk879.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.799 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.801 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.803 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.804 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.806 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.807 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.810 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.812 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2924.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.828 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.967 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.993 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
[02/24/25 08:00:44] DEBUG    2025-02-24 08:00:44.016 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.020 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.026 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2925.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.036 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.043 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.052 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.057 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.060 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.063 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.065 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk884.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.068 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.071 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.073 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.076 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.078 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.081 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.085 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.088 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2929.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.090 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.092 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.094 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.096 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.098 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.101 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.104 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2930.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.111 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.119 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.123 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.127 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk886.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.132 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.134 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.137 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.147 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.150 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.153 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.156 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.159 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.162 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for be149.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.166 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.169 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.170 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.172 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.175 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.177 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.179 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.181 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.183 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1806.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.225 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.231 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.233 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.235 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.237 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.239 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.241 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.243 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.244 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk888.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.246 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.248 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.251 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.252 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.255 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.257 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.259 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.261 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.262 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk890.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.264 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.265 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.267 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.268 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.270 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.271 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.273 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.274 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.276 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2939.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.277 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.280 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.282 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.283 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.285 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.287 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.289 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2940.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.290 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.292 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.294 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.296 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.298 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.300 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.301 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de655.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.303 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.304 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.305 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.307 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.309 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.310 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.312 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk892.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.313 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.314 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.316 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.317 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.319 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.321 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.322 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.323 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.325 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk894.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.326 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.328 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.330 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.332 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.334 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.335 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.337 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.339 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.341 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk896.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.342 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.344 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.345 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.347 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.348 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.350 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.351 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.353 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.354 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk898.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.355 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.357 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.358 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.360 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.361 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.363 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.364 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.365 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.367 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2943.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.368 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.369 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.371 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.372 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.373 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.375 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.376 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2944.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.378 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.381 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.383 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.384 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.386 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.388 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.389 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2945.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.391 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.392 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.394 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.395 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.397 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.398 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.400 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2946.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.401 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.402 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.404 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.405 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.407 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.408 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.410 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for nl408.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.411 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.413 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.414 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.416 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.418 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.419 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.420 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for nl409.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.422 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.423 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.424 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.426 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.427 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.429 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.431 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de676.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.433 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.434 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.436 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.438 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.440 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.441 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.443 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5055.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.444 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.446 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.447 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.449 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.450 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.451 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.453 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.454 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.456 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2949.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.457 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.459 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.460 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.462 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.463 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.465 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.466 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2950.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.468 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.469 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.470 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.472 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.473 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.474 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.476 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr439.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.479 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.481 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.483 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.484 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.486 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.488 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr440.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.491 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.493 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.494 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.497 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.498 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for jp429.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.500 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.501 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.504 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.505 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.507 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.508 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.509 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.511 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for es114.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.512 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.514 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.517 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.518 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.521 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.523 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.524 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for it132.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.525 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.529 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.531 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.535 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.537 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.538 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4735.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.543 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.545 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.547 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.548 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.550 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.551 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.554 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl122.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.555 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.560 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.561 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.563 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.565 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.568 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for cz93.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.569 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.570 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.573 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.575 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.576 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.578 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.583 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for at80.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.584 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.586 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.587 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.589 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.591 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.592 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.594 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.597 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ro59.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.598 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.601 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.604 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.609 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.610 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch198.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.611 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.613 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.615 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.616 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.617 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.619 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.620 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.623 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for bg38.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.624 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.625 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.627 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.630 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.632 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.634 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.636 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.638 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.640 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu47.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.642 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.644 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.645 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.651 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.652 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.654 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.655 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr452.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.657 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.659 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.661 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.662 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.664 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.666 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.667 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.669 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.670 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for jp454.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.671 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.673 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.674 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.675 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.677 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.679 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.681 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.683 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.685 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4951.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.687 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.688 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.690 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.692 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.693 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.695 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.697 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for dk150.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.698 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.700 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.701 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.702 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.704 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.709 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.711 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de750.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.712 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.713 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.715 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.722 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4953.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.730 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.732 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.733 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.735 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4954.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.737 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.739 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.742 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.744 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:44.745 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.747 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl125.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.749 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.753 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.755 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.756 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.758 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.759 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.761 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5057.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.762 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.764 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.765 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.767 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.770 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.771 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.772 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.774 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5058.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.775 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.776 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.779 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.783 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.785 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.787 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.789 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.791 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5059.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.793 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.794 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.796 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.799 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.801 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.802 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.804 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.806 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5060.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.807 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.810 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.811 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.814 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.815 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.816 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.818 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.819 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no141.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.820 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.822 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.823 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.824 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.826 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.828 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.831 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.832 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.834 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no142.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.836 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.838 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.839 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.841 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.843 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.845 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.847 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.848 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.850 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no143.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.851 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.853 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.854 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.855 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.857 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.859 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.860 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.862 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.863 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no144.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.865 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.867 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.868 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.870 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.871 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.872 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.874 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.875 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.878 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no145.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.880 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.882 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.884 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.887 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.889 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.891 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.893 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.895 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.897 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no146.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.898 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.900 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.902 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.904 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.906 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.908 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.910 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.912 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.915 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no147.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.917 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.919 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.921 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.922 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.924 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.927 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.929 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.932 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.934 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no148.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.936 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.939 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.941 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.943 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.945 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.947 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.948 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.950 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.951 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no149.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:44.953 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.955 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.957 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.959 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.962 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.965 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.967 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.969 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.971 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1785.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:44.973 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.975 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.977 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.981 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.984 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.987 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.989 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:44.991 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:44.994 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu49.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:44.996 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:44.998 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
[02/24/25 08:00:45] DEBUG    2025-02-24 08:00:45.000 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.001 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.003 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.005 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.007 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.009 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.011 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr536.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.013 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.014 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.017 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.019 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.020 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.022 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.024 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.026 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.029 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr537.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.033 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.035 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.038 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.040 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.042 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.044 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.046 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.048 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr538.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.050 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.052 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.053 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.055 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.057 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.059 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.061 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.062 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.064 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr539.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.067 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.069 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.071 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.073 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.075 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.076 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.079 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.085 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr540.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.088 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.090 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.092 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.094 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.096 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.098 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.100 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.102 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.104 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr541.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.118 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.120 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.124 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.129 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.132 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.134 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr542.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.136 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.139 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.141 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.143 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.145 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.148 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.150 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.153 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.154 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr543.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.157 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.159 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.161 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.164 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.166 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.168 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.170 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.171 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.173 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr544.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.175 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.177 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.180 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.182 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.184 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.187 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.189 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.191 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.193 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch221.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.195 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.197 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.199 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.201 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.203 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.205 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.207 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.210 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.212 | DEBUG    | nyord_vpn.network.server:get_servers_cache:451 - No valid servers found after          server.py:451
                             filtering 100 total servers                                                                                                              
                    ERROR    2025-02-24 08:00:45.214 | ERROR    | nyord_vpn.network.server:get_servers_cache:481 - Failed to fetch servers: No valid     server.py:481
                             servers found in API response. Total servers: 100, Invalid: 100                                                                          
                             Traceback (most recent call last):                                                                                                       
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/bin/nyord-vpn", line 10, in <module>                               
                                 sys.exit(main())                                                                                                                     
                                 |   |    -> <function main at 0x109db7880>                                                                                           
                                 |   -> <built-in function exit>                                                                                                      
                                 -> <module 'sys' (built-in)>                                                                                                         
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 81, in main                             
                                 fire.Fire(CLI)                                                                                                                       
                                 |    |    -> <class 'nyord_vpn.__main__.CLI'>                                                                                        
                                 |    -> <function Fire at 0x109e5d260>                                                                                               
                                 -> <module 'fire' from                                                                                                               
                             '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/__init__...                             
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 135,              
                             in Fire                                                                                                                                  
                                 component_trace = _Fire(component, args, parsed_flag_args, context, name)                                                            
                                                   |     |          |     |                 |        -> 'nyord-vpn'                                                   
                                                   |     |          |     |                 -> {}                                                                     
                                                   |     |          |     -> Namespace(verbose=False, interactive=False, separator='-', completion=None,              
                             help=False, trace=False)                                                                                                                 
                                                   |     |          -> ['go', 'pl', '--verbose']                                                                      
                                                   |     -> <class 'nyord_vpn.__main__.CLI'>                                                                          
                                                   -> <function _Fire at 0x109e7ea20>                                                                                 
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 468,              
                             in _Fire                                                                                                                                 
                                 component, remaining_args = _CallAndUpdateTrace(                                                                                     
                                 |                           -> <function _CallAndUpdateTrace at 0x109e7eb60>                                                         
                                 -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                                           
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 684,              
                             in _CallAndUpdateTrace                                                                                                                   
                                 component = fn(*varargs, **kwargs)                                                                                                   
                                             |   |          -> {}                                                                                                     
                                             |   -> ['pl']                                                                                                            
                                             -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 46, in go                               
                                 self.client.go(country_code)                                                                                                         
                                 |    |      |  -> 'pl'                                                                                                               
                                 |    |      -> <function Client.go at 0x109db72e0>                                                                                   
                                 |    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                                         
                                 -> <nyord_vpn.__main__.CLI object at 0x109a7c410>                                                                                    
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 278, in go                           
                                 selected_servers = self.server_manager.select_fastest_server(                                                                        
                                                    |    |              -> <function ServerManager.select_fastest_server at 0x109d43920>                              
                                                    |    -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                            
                                                    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                           
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 835, in                           
                             select_fastest_server                                                                                                                    
                                 servers = self.get_servers_cache().get("servers", [])                                                                                
                                           |    -> <function ServerManager.get_servers_cache at 0x109d43600>                                                          
                                           -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                                          
                                                                                                                                                                      
                             > File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 454, in                           
                             get_servers_cache                                                                                                                        
                                 raise ValueError(                                                                                                                    
                                                                                                                                                                      
                             ValueError: No valid servers found in API response. Total servers: 100, Invalid: 100                                                     
                                                                                                                                                                      
                                                                                                                                                                      
                    INFO     2025-02-24 08:00:45.233 | INFO     | nyord_vpn.network.server:get_servers_cache:495 - Using fallback cache with 100 valid   server.py:495
                             servers                                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.237 | DEBUG    | nyord_vpn.network.server:get_servers_cache:305 - Fetching server list from API...      server.py:305
                    DEBUG    2025-02-24 08:00:45.398 | DEBUG    | nyord_vpn.network.server:get_servers_cache:317 - Successfully fetched server data from server.py:317
                             API                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.400 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response     server.py:325
                    DEBUG    2025-02-24 08:00:45.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl128.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.497 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.500 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.504 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.506 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.509 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.511 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.513 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.515 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu48.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:45.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.518 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.523 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.525 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.530 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.535 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5063.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.538 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.545 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.547 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.549 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.551 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.555 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for at86.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:45.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.561 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.563 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.568 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.570 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.574 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch217.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.576 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.578 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.584 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.588 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.590 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.593 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.597 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for dk152.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.601 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.603 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.610 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.611 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.614 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.616 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no151.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.618 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.620 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.622 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.624 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.625 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.628 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.630 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.633 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.635 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch218.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.637 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.639 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.642 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.644 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.646 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.648 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.651 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.653 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1784.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.655 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.657 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.659 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.660 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.663 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.665 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.667 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.669 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.670 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr555.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.672 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.674 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.675 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.678 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.681 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.683 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.685 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.687 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.689 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch219.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.691 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.693 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.695 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.697 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.699 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.701 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.703 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.707 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5064.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.710 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.712 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.714 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk765.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.729 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.731 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.733 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.736 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.738 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.742 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk812.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.744 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.746 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.748 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.754 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.755 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.757 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.759 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk813.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.761 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.763 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.765 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.766 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.770 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.771 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.773 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.775 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk814.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.776 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.779 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.783 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.785 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.787 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.789 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.791 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.793 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk871.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.795 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.796 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.800 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.802 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.803 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.805 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.807 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk873.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.810 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.812 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.814 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.815 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.817 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.819 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.820 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.822 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.823 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk875.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.825 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.827 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.829 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.831 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.833 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.836 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.838 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.840 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.842 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de507.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.844 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.846 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.847 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.849 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.851 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.853 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.854 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de508.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.856 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.858 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.860 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.862 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.864 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.866 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.867 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de509.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.869 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.871 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.872 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.874 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.876 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.879 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.881 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de510.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.882 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.885 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.887 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.889 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.891 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.893 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.895 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk877.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.896 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.898 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.900 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.902 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.906 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.908 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.910 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.911 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.913 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2920.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.915 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.917 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.919 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.921 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.922 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.924 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.926 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2921.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.927 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.930 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.932 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.934 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.937 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.939 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.941 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk879.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.943 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.945 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.947 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.949 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.951 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.953 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.954 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.956 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.958 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2924.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.960 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.963 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.965 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.967 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.970 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.972 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.974 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2925.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:45.976 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.978 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.980 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.981 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.983 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:45.985 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.987 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk884.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:45.989 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.991 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.992 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:45.995 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:45.997 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:45.999 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
[02/24/25 08:00:46] DEBUG    2025-02-24 08:00:46.000 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.002 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.004 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2929.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.005 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.007 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.009 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.012 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.014 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.016 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.018 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2930.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.021 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.023 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.025 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.027 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.029 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.033 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk886.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.035 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.037 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.039 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.041 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.043 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.045 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.047 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.050 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.051 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for be149.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.053 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.055 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.057 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.059 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.062 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.064 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.066 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.068 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.071 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1806.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.072 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.075 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.077 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.078 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.080 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.082 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.084 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.086 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.088 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk888.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.089 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.091 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.093 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.095 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.097 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.099 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.103 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.105 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk890.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.110 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.112 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.114 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.116 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.119 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.121 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.123 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2939.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.127 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.129 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.131 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.133 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.135 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.138 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.140 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2940.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.141 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.144 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.146 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.149 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.151 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.154 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.156 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de655.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.158 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.160 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.162 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.164 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.166 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.168 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.170 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk892.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.172 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.174 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.176 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.178 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.181 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.183 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.185 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.187 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.189 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk894.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.191 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.193 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.195 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.198 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.200 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.203 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.205 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.208 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.210 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk896.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.212 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.214 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.216 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.218 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.220 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.223 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.225 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.227 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.229 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk898.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.232 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.234 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.236 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.239 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.241 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.243 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.245 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.247 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.249 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2943.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.251 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.253 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.255 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.257 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.259 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.262 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.264 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2944.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.266 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.268 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.270 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.272 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.274 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.276 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.278 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2945.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.280 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.283 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.285 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.287 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.290 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.292 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.294 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2946.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.296 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.298 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.300 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.302 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.304 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.307 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.309 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for nl408.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.311 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.314 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.316 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.318 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.321 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.323 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.325 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for nl409.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.327 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.329 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.331 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.333 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.335 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.337 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.339 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de676.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.341 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.343 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.345 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.347 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.350 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.352 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.354 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5055.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.356 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.358 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.360 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.362 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.365 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.367 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.370 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.372 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.374 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2949.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.376 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.378 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.381 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.383 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.385 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.387 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.389 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us2950.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.391 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.393 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.396 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.399 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.401 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.403 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.406 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr439.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.408 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.410 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.412 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.414 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.416 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.418 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.420 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr440.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.422 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.424 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.426 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.428 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.430 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.432 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.434 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for jp429.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.436 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.438 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.440 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.442 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.445 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.447 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.450 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.452 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.454 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for es114.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.457 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.459 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.461 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.463 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.465 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.467 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.469 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.471 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.473 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for it132.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.475 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.480 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.482 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.484 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.487 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.491 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.493 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4735.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.497 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.499 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.501 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.503 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.505 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.507 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.510 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.512 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl122.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.514 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.518 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.522 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.524 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.526 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.528 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.531 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for cz93.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.535 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.538 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.545 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.547 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.549 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.551 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for at80.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.552 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.554 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.561 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.564 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.568 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.571 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ro59.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.573 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.575 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.577 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.579 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.583 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.585 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.587 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.589 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch198.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.591 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.593 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.597 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.600 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.604 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.606 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.608 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for bg38.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.610 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.612 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.615 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.617 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.619 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.624 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.626 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.628 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu47.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.630 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.632 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.634 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.636 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.638 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.640 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.641 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.643 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.645 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr452.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.650 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.652 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.654 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.656 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.657 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.659 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.662 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for jp454.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.664 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.665 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.667 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.669 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.671 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.673 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.675 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.677 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.678 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4951.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.680 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.682 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.683 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.685 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.686 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.688 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.690 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for dk150.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.691 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.693 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.694 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.696 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.698 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.699 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.701 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.702 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.704 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for de750.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.706 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.709 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.711 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.713 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.715 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.717 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4953.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.730 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.732 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us4954.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.734 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.735 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.737 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.739 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 42, Name: OpenVPN UDP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:00:46.742 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.745 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl125.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.748 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.755 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.757 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.759 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.761 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.763 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.764 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5057.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.766 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.769 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.771 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.772 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.774 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.776 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.777 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.779 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5058.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.783 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.784 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.785 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.787 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.788 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.790 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.791 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.792 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5059.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.794 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.796 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.799 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.801 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.803 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.804 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.806 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.808 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5060.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.811 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.812 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.813 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.815 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.816 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.818 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.819 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.820 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no141.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.822 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.823 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.825 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.826 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.828 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.829 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.831 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.832 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.833 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no142.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.835 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.836 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.837 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.839 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.840 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.842 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.843 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.845 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.847 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no143.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.848 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.850 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.852 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.854 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.855 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.857 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.859 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.861 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.862 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no144.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.863 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.865 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.866 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.867 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.869 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.870 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.871 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.873 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.874 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no145.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.875 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.877 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.879 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.880 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.882 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.883 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.885 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.886 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.888 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no146.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.889 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.890 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.892 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.893 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.894 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.896 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.898 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.900 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.901 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no147.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.903 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.905 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.907 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.909 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.910 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.912 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.914 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.916 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.917 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no148.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.919 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.920 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.922 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.923 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.925 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.926 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.928 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.930 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.931 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no149.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.933 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.935 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.936 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.938 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.940 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.941 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.943 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.944 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.945 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1785.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:46.947 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.948 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.949 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.951 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.952 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.954 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.955 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.956 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.958 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu49.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:46.959 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.961 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.962 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.963 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.965 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.966 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.968 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.969 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.971 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr536.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.972 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.974 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.976 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.978 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.980 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.982 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.984 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.985 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.987 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr537.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:46.989 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.991 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.993 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.994 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:46.996 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:46.998 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:46.999 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
[02/24/25 08:00:47] DEBUG    2025-02-24 08:00:47.001 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.003 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr538.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.004 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.006 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.007 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.009 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.011 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.013 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.015 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.016 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.018 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr539.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.020 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.022 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.024 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.025 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.027 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.029 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.030 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.033 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr540.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.034 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.036 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.037 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.039 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.040 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.042 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.043 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.044 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.046 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr541.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.048 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.049 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.051 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.052 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.054 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.055 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.056 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.058 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.059 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr542.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.061 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.063 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.065 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.067 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.069 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.071 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.073 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.075 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.077 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr543.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.079 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.080 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.085 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.086 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.088 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.090 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.091 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.093 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr544.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.095 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.098 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.099 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.102 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.104 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.110 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.112 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch221.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.114 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.115 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.117 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.119 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.120 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.122 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.124 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.127 | DEBUG    | nyord_vpn.network.server:get_servers_cache:451 - No valid servers found after          server.py:451
                             filtering 100 total servers                                                                                                              
                    ERROR    2025-02-24 08:00:47.129 | ERROR    | nyord_vpn.network.server:get_servers_cache:481 - Failed to fetch servers: No valid     server.py:481
                             servers found in API response. Total servers: 100, Invalid: 100                                                                          
                             Traceback (most recent call last):                                                                                                       
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/bin/nyord-vpn", line 10, in <module>                               
                                 sys.exit(main())                                                                                                                     
                                 |   |    -> <function main at 0x109db7880>                                                                                           
                                 |   -> <built-in function exit>                                                                                                      
                                 -> <module 'sys' (built-in)>                                                                                                         
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 81, in main                             
                                 fire.Fire(CLI)                                                                                                                       
                                 |    |    -> <class 'nyord_vpn.__main__.CLI'>                                                                                        
                                 |    -> <function Fire at 0x109e5d260>                                                                                               
                                 -> <module 'fire' from                                                                                                               
                             '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/__init__...                             
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 135,              
                             in Fire                                                                                                                                  
                                 component_trace = _Fire(component, args, parsed_flag_args, context, name)                                                            
                                                   |     |          |     |                 |        -> 'nyord-vpn'                                                   
                                                   |     |          |     |                 -> {}                                                                     
                                                   |     |          |     -> Namespace(verbose=False, interactive=False, separator='-', completion=None,              
                             help=False, trace=False)                                                                                                                 
                                                   |     |          -> ['go', 'pl', '--verbose']                                                                      
                                                   |     -> <class 'nyord_vpn.__main__.CLI'>                                                                          
                                                   -> <function _Fire at 0x109e7ea20>                                                                                 
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 468,              
                             in _Fire                                                                                                                                 
                                 component, remaining_args = _CallAndUpdateTrace(                                                                                     
                                 |                           -> <function _CallAndUpdateTrace at 0x109e7eb60>                                                         
                                 -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                                           
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 684,              
                             in _CallAndUpdateTrace                                                                                                                   
                                 component = fn(*varargs, **kwargs)                                                                                                   
                                             |   |          -> {}                                                                                                     
                                             |   -> ['pl']                                                                                                            
                                             -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 46, in go                               
                                 self.client.go(country_code)                                                                                                         
                                 |    |      |  -> 'pl'                                                                                                               
                                 |    |      -> <function Client.go at 0x109db72e0>                                                                                   
                                 |    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                                         
                                 -> <nyord_vpn.__main__.CLI object at 0x109a7c410>                                                                                    
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 278, in go                           
                                 selected_servers = self.server_manager.select_fastest_server(                                                                        
                                                    |    |              -> <function ServerManager.select_fastest_server at 0x109d43920>                              
                                                    |    -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                            
                                                    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                           
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 840, in                           
                             select_fastest_server                                                                                                                    
                                 normalized_country = self._validate_country_code(country_code)                                                                       
                                                      |    |                      -> 'pl'                                                                             
                                                      |    -> <function ServerManager._validate_country_code at 0x109d434c0>                                          
                                                      -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 175, in                           
                             _validate_country_code                                                                                                                   
                                 country_info = self.get_country_info(normalized)                                                                                     
                                                |    |                -> 'PL'                                                                                         
                                                |    -> <function ServerManager.get_country_info at 0x109d43b00>                                                      
                                                -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                                     
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 1023, in                          
                             get_country_info                                                                                                                         
                                 cache = self.get_servers_cache()                                                                                                     
                                         |    -> <function ServerManager.get_servers_cache at 0x109d43600>                                                            
                                         -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                                            
                                                                                                                                                                      
                             > File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 454, in                           
                             get_servers_cache                                                                                                                        
                                 raise ValueError(                                                                                                                    
                                                                                                                                                                      
                             ValueError: No valid servers found in API response. Total servers: 100, Invalid: 100                                                     
                                                                                                                                                                      
                                                                                                                                                                      
                    INFO     2025-02-24 08:00:47.144 | INFO     | nyord_vpn.network.server:get_servers_cache:495 - Using fallback cache with 100 valid   server.py:495
                             servers                                                                                                                                  
                    DEBUG    2025-02-24 08:00:47.147 | DEBUG    | nyord_vpn.network.server:select_fastest_server:888 - Testing 3 servers for speed       server.py:888
                    DEBUG    2025-02-24 08:00:47.307 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl122.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 08:00:47.318 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl128.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 08:00:47.346 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl125.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    ERROR    2025-02-24 08:00:47.350 | ERROR    | nyord_vpn.network.server:select_fastest_server:932 - Error selecting server: No        server.py:932
                             responsive servers found in PL                                                                                                           
Error: Failed to select servers: No responsive servers found in PL

---

_**Assistant**_



---



---

