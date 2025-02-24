## SpecStory

## Task Management for nyord-vpn Project (24/02/2025, 20:10:22)

_**User**_

Proceed with @TODO.md and mark @PROGRESS.md as you do

---

_**Assistant**_

<think>Let me analyze the task I need to work on:

1. The user is asking me to proceed with implementing the tasks in the TODO.md file and updating the PROGRESS.md file as I make progress.
2. According to the attached files, this is for a project called "nyord-vpn", which is a modern Python client for NordVPN with automatic API fallback support.
3. There's a TODO.md file that outlines the remaining tasks for the project.
4. There's a PROGRESS.md file that tracks the completed and remaining tasks.

First, I need to understand the structure of the project better. Let me list the directory to see the files and structure:
</think>I'll start working on the remaining tasks outlined in the TODO.md and update PROGRESS.md as we make progress. First, let me explore the project structure to understand what we're working with.

---

_****_

<details>
            <summary>Listed current directory • **26** results</summary>
        
| Name |
|-------|
| 📁 `.git` |
| 📄 `PROGRESS.md` |
| 📄 `TODO.md` |
| 📁 `.pytest_cache` |
| 📄 `cleanup.py` |
| 📁 `tests` |
| 📁 `_private` |
| 📄 `.DS_Store` |
| 📄 `CLEANUP.txt` |
| 📄 `nyord_vpn.txt` |
| 📁 `.venv` |
| 📁 `.specstory` |
| 📁 `.ruff_cache` |
| 📁 `src` |
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



Let me check the source directory structure:

---

_****_

<details>
            <summary>Listed directory src • **3** results</summary>
        
| Name |
|-------|
| 📄 `.DS_Store` |
| 📁 `nyord_vpn` |
| 📄 `__init__.py` |

</details>

---

_****_



Let's look at the structure of the nyord_vpn directory:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn • **12** results</summary>
        
| Name |
|-------|
| 📄 `__init__.py` |
| 📁 `api` |
| 📁 `__pycache__` |
| 📄 `exceptions.py` |
| 📄 `.DS_Store` |
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



Now I'll look at the API module which is one of the first areas to work on:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/api • **14** results</summary>
        
| Name |
|-------|
| 📄 `v2_servers.py` |
| 📁 `__pycache__` |
| 📄 `api.py` |
| 📄 `v1_recommendations.py` |
| 📄 `v1_groups.py` |
| 📄 `v1_technologies.py` |
| 📄 `__init__.py` |
| 📄 `v1_countries.py` |
| 📄 `.DS_Store` |
| 📄 `v2_servers.json` |
| 📄 `v1_recommendations.json` |
| 📄 `v1_technologies.json` |
| 📄 `v1_groups.json` |
| 📄 `v1_countries.json` |

</details>

---

_****_





Let's first check the api.py file, as it's the first item we need to modify according to the TODO.md:

---

_****_

Read file: src/nyord_vpn/api/api.py

---

_****_



Now let's look at one of the v1_* files to understand what needs to be updated there:

---

_****_

Read file: src/nyord_vpn/api/v1_recommendations.py

---

_****_





Let's also check the v2_servers.py file to understand what needs to be fixed there:

---

_****_

Read file: src/nyord_vpn/api/v2_servers.py

---

_****_





Now let's check the core files that need to be updated:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/core • **6** results</summary>
        
| Name |
|-------|
| 📄 `client.py` |
| 📄 `api.py` |
| 📄 `.DS_Store` |
| 📁 `__pycache__` |
| 📄 `base.py` |
| 📄 `__init__.py` |

</details>

---

_****_





Let's see the core/api.py file which we need to deprecate:

---

_****_

Read file: src/nyord_vpn/core/api.py

---

_****_





Now let's understand what needs to be changed in the client.py file:

---

_****_

Read file: src/nyord_vpn/core/client.py

---

_****_







Let's also see the network files that need to be updated:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/network • **7** results</summary>
        
| Name |
|-------|
| 📄 `vpn.py` |
| 📄 `server.py` |
| 📄 `.DS_Store` |
| 📁 `__pycache__` |
| 📄 `vpn_commands.py` |
| 📄 `__init__.py` |
| 📄 `country.py` |

</details>

---

_****_







Let's take a quick look at the server.py file:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





Let's also check vpn.py:

---

_****_

Read file: src/nyord_vpn/network/vpn.py

---

_****_







Let's check vpn_commands.py:

---

_****_

Read file: src/nyord_vpn/network/vpn_commands.py

---

_****_









Let's check utils/templates.py:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/utils • **7** results</summary>
        
| Name |
|-------|
| 📄 `.DS_Store` |
| 📁 `data` |
| 📁 `__pycache__` |
| 📄 `templates.py` |
| 📄 `utils.py` |
| 📄 `__init__.py` |
| 📄 `connection.py` |

</details>

---

_****_







---

_****_

Read file: src/nyord_vpn/utils/templates.py

---

_****_










Based on my exploration of the codebase, I have a good understanding of what needs to be done. Let me start working on the first task from the remaining tasks:

## Task 1: Modify src/nyord_vpn/api/api.py to make it the central API interface.

First, let's implement the changes to api.py:

---

_****_

```diff
  this_file: src/nyord_vpn/api/api.py
  
- This module provides the NordVPNAPIClient class for interacting with NordVPN's API.
+ This module provides the NordVPNAPI class for interacting with NordVPN's API.
  It serves as the central interface for all API operations, coordinating between
  v1 and v2 endpoints with automatic fallback support.
  """
  
- from typing import cast
+ import warnings
+ from typing import Any, cast, Optional, TypeVar, Generic
+ 
+ from loguru import logger
+ import requests
  
  from nyord_vpn.api import (
      v2_servers,
  )
+ from nyord_vpn.exceptions import VPNConnectionError, VPNAPIError
  
  # Type aliases for clarity
      list[v2_servers.Technology],
  ]
+ 
+ T = TypeVar('T')
  
  
      both v1 and v2. It handles initialization of individual clients and provides
      convenience methods for common operations.
+ 
+     Attributes:
+         timeout: Request timeout in seconds for all API calls.
+         recommendations: Client for v1 recommendations API (deprecated).
+         technologies: Client for v1 technologies API (deprecated).
+         groups: Client for v1 groups API (deprecated).
+         countries: Client for v1 countries API (deprecated).
+         servers: Client for v2 servers API (preferred).
      """
  
          Args:
              timeout: Request timeout in seconds for all API calls.
- 
          """
          self.timeout = timeout
  
          # Cache for API responses
-         self._recommended_servers: list[v1_recommendations.RecommendedServer] | None = (
-             None
-         )
-         self._technologies: list[v1_technologies.Technology] | None = None
-         self._groups: list[v1_groups.Group] | None = None
-         self._countries: list[v1_countries.Country] | None = None
-         self._servers: ServerTuple | None = None
+         self._recommended_servers: Optional[list[v1_recommendations.RecommendedServer]] = None
+         self._technologies: Optional[list[v1_technologies.Technology]] = None
+         self._groups: Optional[list[v1_groups.Group]] = None
+         self._countries: Optional[list[v1_countries.Country]] = None
+         self._servers: Optional[ServerTuple] = None
  
      def get_recommended_servers(
-         self, refresh: bool = False
+         self, *, refresh: bool = False
      ) -> list[v1_recommendations.RecommendedServer]:
          """Get recommended servers.
+ 
+         This method is deprecated and uses the v1 API. Consider using find_best_server
+         or get_servers instead, which use the v2 API.
  
          Args:
          Returns:
              List of recommended servers.
- 
          """
+         warnings.warn(
+             "get_recommended_servers is deprecated and uses the v1 API. "
+             "Consider using find_best_server or get_servers instead.",
+             DeprecationWarning,
+             stacklevel=2,
+         )
+         
          if self._recommended_servers is None or refresh:
-             self._recommended_servers = self.recommendations.fetch_recommendations()
+             try:
+                 self._recommended_servers = self.recommendations.fetch_recommendations()
+             except requests.exceptions.RequestException as e:
+                 logger.error(f"Failed to fetch recommended servers: {e}")
+                 if self._recommended_servers is None:
+                     # Only raise if we don't have cached data
+                     raise VPNAPIError(f"Failed to fetch recommended servers: {e}") from e
+         
          return self._recommended_servers
  
      def get_technologies(
-         self, refresh: bool = False
+         self, *, refresh: bool = False
      ) -> list[v1_technologies.Technology]:
          """Get available VPN technologies.
+ 
+         This method is deprecated and uses the v1 API. Consider using get_servers
+         instead, which uses the v2 API and includes technology information.
  
          Args:
          Returns:
              List of VPN technologies.
- 
          """
+         warnings.warn(
+             "get_technologies is deprecated and uses the v1 API. "
+             "Consider using get_servers instead.",
+             DeprecationWarning,
+             stacklevel=2,
+         )
+         
          if self._technologies is None or refresh:
-             self._technologies = self.technologies.fetch_technologies()
+             try:
+                 self._technologies = self.technologies.fetch_technologies()
+             except requests.exceptions.RequestException as e:
+                 logger.error(f"Failed to fetch technologies: {e}")
+                 if self._technologies is None:
+                     # Only raise if we don't have cached data
+                     raise VPNAPIError(f"Failed to fetch technologies: {e}") from e
+         
          return self._technologies
  
-     def get_groups(self, refresh: bool = False) -> list[v1_groups.Group]:
+     def get_groups(self, *, refresh: bool = False) -> list[v1_groups.Group]:
          """Get server groups.
+ 
+         This method is deprecated and uses the v1 API. Consider using get_servers
+         instead, which uses the v2 API and includes group information.
  
          Args:
          Returns:
              List of server groups.
- 
          """
+         warnings.warn(
+             "get_groups is deprecated and uses the v1 API. "
+             "Consider using get_servers instead.",
+             DeprecationWarning,
+             stacklevel=2,
+         )
+         
          if self._groups is None or refresh:
-             self._groups = self.groups.fetch_groups()
+             try:
+                 self._groups = self.groups.fetch_groups()
+             except requests.exceptions.RequestException as e:
+                 logger.error(f"Failed to fetch groups: {e}")
+                 if self._groups is None:
+                     # Only raise if we don't have cached data
+                     raise VPNAPIError(f"Failed to fetch groups: {e}") from e
+         
          return self._groups
  
-     def get_countries(self, refresh: bool = False) -> list[v1_countries.Country]:
+     def get_countries(self, *, refresh: bool = False) -> list[v1_countries.Country]:
          """Get countries with server information.
+ 
+         This method is deprecated and uses the v1 API. Consider using get_servers
+         instead, which uses the v2 API and includes country information.
  
          Args:
          Returns:
              List of countries.
- 
          """
+         warnings.warn(
+             "get_countries is deprecated and uses the v1 API. "
+             "Consider using get_servers instead.",
+             DeprecationWarning,
+             stacklevel=2,
+         )
+         
          if self._countries is None or refresh:
-             self._countries = self.countries.fetch_countries()
+             try:
+                 self._countries = self.countries.fetch_countries()
+             except requests.exceptions.RequestException as e:
+                 logger.error(f"Failed to fetch countries: {e}")
+                 if self._countries is None:
+                     # Only raise if we don't have cached data
+                     raise VPNAPIError(f"Failed to fetch countries: {e}") from e
+         
          return self._countries
  
-     def get_servers(self, refresh: bool = False) -> ServerTuple:
+     def get_servers(self, *, refresh: bool = False) -> ServerTuple:
          """Get detailed server information.
+ 
+         This method uses the v2 API to fetch comprehensive server information,
+         including groups, services, locations, and technologies.
  
          Args:
          Returns:
              Tuple of (servers, groups, services, locations, technologies).
- 
+             
+         Raises:
+             VPNAPIError: If the API request fails and no cached data is available.
          """
          if self._servers is None or refresh:
-             result = self.servers.fetch_all()
-             self._servers = cast(ServerTuple, result)
+             try:
+                 result = self.servers.fetch_all()
+                 self._servers = cast(ServerTuple, result)
+             except requests.exceptions.RequestException as e:
+                 logger.error(f"Failed to fetch servers: {e}")
+                 if self._servers is None:
+                     # Only raise if we don't have cached data
+                     raise VPNAPIError(f"Failed to fetch servers: {e}") from e
+         
          return self._servers
  
      def find_best_server(
-         self, country_code: str | None = None, group_identifier: str | None = None
-     ) -> v1_recommendations.RecommendedServer:
+         self, 
+         country_code: Optional[str] = None, 
+         group_identifier: Optional[str] = None,
+         technology_identifier: Optional[str] = None,
+         *, 
+         use_v2: bool = True
+     ) -> v1_recommendations.RecommendedServer | v2_servers.Server:
          """Find the best server based on load and optional filters.
+ 
+         This method prioritizes using the v2 API but will fall back to v1 if requested
+         or if the v2 API request fails.
  
          Args:
              country_code: Optional two-letter country code to filter by.
              group_identifier: Optional group identifier to filter by.
+             technology_identifier: Optional technology identifier to filter by.
+             use_v2: Whether to use the v2 API first. If False, will use v1 API.
  
          Returns:
          Raises:
              ValueError: If no servers match the criteria.
- 
-         """
-         servers = self.get_recommended_servers()
- 
-         if country_code:
-             servers = [
-                 server
-                 for server in servers
-                 if server.locations
-                 and server.locations[0].country.code.upper() == country_code.upper()
-             ]
- 
-         if group_identifier:
-             servers = [
-                 server
-                 for server in servers
-                 if any(group.identifier == group_identifier for group in server.groups)
-             ]
- 
-         if not servers:
-             raise ValueError(
-                 f"No servers found matching criteria: "
-                 f"country_code={country_code}, group_identifier={group_identifier}"
-             )
- 
-         return min(servers, key=lambda s: s.load)
- 
-     def get_server_stats(self) -> dict:
+             VPNAPIError: If API requests fail and no suitable server can be found.
+         """
+         # Try v2 API first (preferred)
+         if use_v2:
+             try:
+                 servers = self.get_servers()[0]  # First element is servers
+                 
+                 filtered_servers = servers
+                 
+                 # Apply filters
+                 if country_code:
+                     filtered_servers = [
+                         server for server in filtered_servers
+                         if server.locations and any(
+                             location.country.code.upper() == country_code.upper() 
+                             for location in server.locations
+                         )
+                     ]
+                 
+                 if group_identifier:
+                     filtered_servers = [
+                         server for server in filtered_servers
+                         if any(group.identifier == group_identifier for group in server.groups)
+                     ]
+                 
+                 if technology_identifier:
+                     filtered_servers = [
+                         server for server in filtered_servers
+                         if any(tech.identifier == technology_identifier for tech in server.technologies)
+                     ]
+                 
+                 # Sort by load
+                 if filtered_servers:
+                     return min(filtered_servers, key=lambda s: s.load)
+                 
+                 # Fall through to v1 API if no servers found
+                 logger.warning(
+                     f"No servers found with v2 API matching criteria: "
+                     f"country_code={country_code}, group_identifier={group_identifier}, "
+                     f"technology_identifier={technology_identifier}. "
+                     f"Falling back to v1 API."
+                 )
+             except (requests.exceptions.RequestException, VPNAPIError) as e:
+                 logger.warning(f"Failed to use v2 API, falling back to v1: {e}")
+                 # Fall through to v1 API
+         
+         # Fall back to v1 API
+         try:
+             servers = self.get_recommended_servers()
+             
+             filtered_servers = servers
+             
+             # Apply filters
+             if country_code:
+                 filtered_servers = [
+                     server for server in filtered_servers
+                     if server.locations and server.locations[0].country.code.upper() == country_code.upper()
+                 ]
+             
+             if group_identifier:
+                 filtered_servers = [
+                     server for server in filtered_servers
+                     if any(group.identifier == group_identifier for group in server.groups)
+                 ]
+             
+             if technology_identifier:
+                 filtered_servers = [
+                     server for server in filtered_servers
+                     if any(tech.identifier == technology_identifier for tech in server.technologies)
+                 ]
+             
+             if not filtered_servers:
+                 raise ValueError(
+                     f"No servers found matching criteria: "
+                     f"country_code={country_code}, group_identifier={group_identifier}, "
+                     f"technology_identifier={technology_identifier}"
+                 )
+             
+             return min(filtered_servers, key=lambda s: s.load)
+             
+         except (requests.exceptions.RequestException, VPNAPIError) as e:
+             raise VPNAPIError(
+                 f"Failed to find best server using both v1 and v2 APIs: {e}"
+             ) from e
+ 
+     def get_server_stats(self) -> dict[str, Any]:
          """Get statistics about server availability.
+ 
+         This method combines data from both v1 and v2 APIs to provide
+         comprehensive statistics about available servers.
  
          Returns:
              Dictionary containing various statistics about servers.
- 
-         """
-         countries = self.get_countries()
-         servers = self.get_servers()[0]
-         groups = self.get_groups()
- 
-         return {
-             "total_countries": len(countries),
-             "total_servers": len(servers),
-             "total_groups": len(groups),
-             "servers_by_country": {
-                 country.code: country.server_count
-                 for country in sorted(
-                     countries, key=lambda x: x.server_count, reverse=True
-                 )
-             },
-             "servers_by_group": {
-                 group.identifier: len(
-                     [
-                         server
-                         for server in servers
-                         if any(g.identifier == group.identifier for g in server.groups)
-                     ]
-                 )
-                 for group in groups
-             },
-         }
+             
+         Raises:
+             VPNAPIError: If API requests fail and no statistics can be generated.
+         """
+         try:
+             # Try v2 API first
+             servers, groups, _, locations, _ = self.get_servers()
+             
+             # Create a map of country codes to countries
+             countries_by_code = {}
+             for location in locations:
+                 country_code = location.country.code
+                 if country_code not in countries_by_code:
+                     countries_by_code[country_code] = location.country
+             
+             # Count servers by country
+             servers_by_country = {}
+             for server in servers:
+                 if not server.locations:
+                     continue
+                 
+                 for location in server.locations:
+                     country_code = location.country.code
+                     if country_code not in servers_by_country:
+                         servers_by_country[country_code] = 0
+                     servers_by_country[country_code] += 1
+             
+             # Count servers by group
+             servers_by_group = {}
+             for group in groups:
+                 servers_by_group[group.identifier] = len([
+                     server for server in servers
+                     if any(g.identifier == group.identifier for g in server.groups)
+                 ])
+             
+             return {
+                 "total_countries": len(countries_by_code),
+                 "total_servers": len(servers),
+                 "total_groups": len(groups),
+                 "servers_by_country": {
+                     code: count for code, count in sorted(
+                         servers_by_country.items(), 
+                         key=lambda x: x[1], 
+                         reverse=True
+                     )
+                 },
+                 "servers_by_group": servers_by_group,
+             }
+             
+         except (VPNAPIError, requests.exceptions.RequestException) as e:
+             # Fall back to v1 API
+             logger.warning(f"Failed to generate stats from v2 API, trying v1: {e}")
+             
+             try:
+                 countries = self.get_countries()
+                 v1_groups = self.get_groups()
+                 
+                 return {
+                     "total_countries": len(countries),
+                     "total_servers": sum(country.server_count for country in countries),
+                     "total_groups": len(v1_groups),
+                     "servers_by_country": {
+                         country.code: country.server_count
+                         for country in sorted(
+                             countries, key=lambda x: x.server_count, reverse=True
+                         )
+                     },
+                     # We don't have accurate group data from v1 API
+                     "servers_by_group": {
+                         group.identifier: 0 for group in v1_groups
+                     },
+                 }
+             except (VPNAPIError, requests.exceptions.RequestException) as e2:
+                 raise VPNAPIError(
+                     f"Failed to generate server statistics using both v1 and v2 APIs: {e2}"
+                 ) from e2
  
```

---

_****_



Let's fix the linter error by implementing the VPNAPIError in the exceptions module:

---

_****_

Read file: src/nyord_vpn/exceptions.py

---

_****_





Let's add the VPNAPIError to the exceptions.py file:

---

_****_

```diff
      - VPNConnectionError
      - VPNDisconnectionError
+     - VPNAPIError
    - CredentialsError
    - ServerNotFoundError
      ) -> None:
          super().__init__(message, details, cause)
+ 
+ 
+ class VPNAPIError(VPNError):
+     """Raised when API operations fail.
+     
+     This exception indicates a failure in communicating with the NordVPN API,
+     which could be due to network issues, authentication problems, or service unavailability.
+     It is used to indicate both v1 and v2 API failures.
+     """
+ 
+     def __init__(
+         self,
+         message: str = "Failed to communicate with NordVPN API",
+         details: str | None = None,
+         cause: Exception | None = None,
+     ) -> None:
+         super().__init__(message, details, cause)
  
```

---

_****_





Now let's run a linting check to see if our changes have fixed the issues:

---

_****_

```bash
ruff check --output-format=github --fix --unsafe-fixes src/nyord_vpn/api/api.py && ruff format --respect-gitignore --target-version py312 src/nyord_vpn/api/api.py
```

```
warning: Selection `DOC` has no effect because preview is not enab
led.                                                              ::error title=
Ruff (TRY003),file=/Users/adam/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=126,col=27,endLine=126,endC
olumn=83::src/nyord_vpn/api/api.py:126:27: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=159,col=27,endLine=159,endC
olumn=76::src/nyord_vpn/api/api.py:159:27: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=190,col=27,endLine=190,endC
olumn=70::src/nyord_vpn/api/api.py:190:27: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=221,col=27,endLine=221,endC
olumn=73::src/nyord_vpn/api/api.py:221:27: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=249,col=27,endLine=249,endC
olumn=71::src/nyord_vpn/api/api.py:249:27: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (C901),file=/Users/adam
/Developer/vcs/github.tw
ardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=253,col=9,endLine=253,endColu
mn=25::src/nyord_vpn/api/api.py:253:9: C901 `find_best_server` is too complex (1
2 > 10)                               ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=350,col=23,endLine=354,endC
olumn=18::src/nyord_vpn/api/api.py:350:23: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=359,col=19,endLine=361,endC
olumn=14::src/nyord_vpn/api/api.py:359:19: TRY003 Avoid specifying long messages
 outside the exception class          ::error title=Ruff (TRY003),file=/Users/ad
am/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/api/api.py,line=443,col=23,endLine=445,endC
olumn=18::src/nyord_vpn/api/api.py:443:23: TRY003 Avoid specifying long messages
 outside the exception class          %
                        

```

---

_****_



---

_**User**_



---

_**Assistant**_

<think>Now I'll focus on implementing the changes to `src/nyord_vpn/network/vpn_commands.py` as mentioned in the TODO.md/PROGRESS.md files. The specific tasks are:

1. Create `OpenVPNConfig` dataclass
2. Implement `get_openvpn_command` function with proper validation

Let me first check the current implementation to understand what needs to be changed:

I've already seen the vpn_commands.py file content earlier, and I can see that it already has a `get_openvpn_command` function, but it lacks proper structure with a dataclass. I'll need to refactor this to use a dataclass for better type safety and validation.

Here's my approach:
1. Create an `OpenVPNConfig` dataclass to store configuration parameters
2. Refactor the `get_openvpn_command` function to use this dataclass
3. Add comprehensive validation for the config parameters
4. Ensure all boolean parameters are keyword-only

Let me implement these changes:</think>Now I'll continue working on the next task in the PROGRESS.md, which is refactoring the VPN commands module.

Let's first examine the current implementation of the vpn_commands.py file more thoroughly to understand its structure and functionality:

---

_****_

Read file: src/nyord_vpn/network/vpn_commands.py

---

_****_



---

_**User**_

Work thru @TODO.md and check off @PROGRESS.md 

---

_**Assistant**_

<think>Based on the TODO.md and PROGRESS.md files, it looks like I need to continue with the refactoring efforts for the NordVPN client. I'll focus on the next items that need to be completed according to the PROGRESS.md file.

The next section to work on appears to be refactoring the `src/nyord_vpn/network/vpn_commands.py` file. Let me start by reviewing that file and implementing the required changes.

The tasks for this file are:
1. Create an `OpenVPNConfig` dataclass
2. Implement `get_openvpn_command` function with proper validation

Let's look at the current `vpn_commands.py` file and then refactor it based on the requirements.

From what I can see, the current `vpn_commands.py` file has a single function `get_openvpn_command` that constructs an OpenVPN command with various parameters. We need to refactor this to use a dataclass for configuration.

Here's my plan:
1. Create an `OpenVPNConfig` dataclass to hold all the configuration options
2. Implement a `get_openvpn_command` function that uses the `OpenVPNConfig` dataclass
3. Ensure proper validation and error handling
4. Add comprehensive docstrings and type hints

Let me create the new implementation:</think>I'll continue working through the TODO list from where it was left off. The next task appears to be refactoring the network module, specifically starting with `vpn_commands.py`.

Let's implement the changes to refactor the `vpn_commands.py` file by creating an `OpenVPNConfig` dataclass and improving the command generation functionality:

---

_****_

```diff
  It centralizes all OpenVPN-related command construction to ensure consistency
  and proper configuration across the application.
+ 
+ Key Features:
+ 1. OpenVPNConfig dataclass for configuration management
+ 2. Platform-specific command customization
+ 3. Secure defaults for encryption and TLS
+ 4. DNS leak prevention
+ 5. Configuration validation
  """
  
  import platform
+ import os
+ import shutil
+ from dataclasses import dataclass, field
+ from enum import Enum, auto
  from pathlib import Path
+ from typing import Optional, List, Dict, Union, Any
+ 
+ from loguru import logger
  
  from nyord_vpn.exceptions import VPNConfigError
  
  
- def get_openvpn_command(
-     config_path: Path,
-     auth_path: Path,
-     log_path: Path | None = None,
-     verbosity: int = 5,
-     connect_retry: int = 2,
-     connect_timeout: int = 10,
-     ping_interval: int = 10,
-     ping_restart: int = 60,
- ) -> list[str]:
-     """Construct OpenVPN command with all necessary arguments.
- 
-     This is the central place for OpenVPN command construction. It provides
-     a comprehensive set of options for connection management, monitoring,
-     and error handling.
- 
-     Args:
+ class OpenVPNVerbosity(Enum):
+     """OpenVPN verbosity levels.
+     
+     These levels determine the amount of logging output from the OpenVPN process:
+     - SILENT: Minimal output (errors only)
+     - ERROR: Basic error information
+     - WARNING: Errors and warnings
+     - NORMAL: Standard connection information
+     - DETAIL: Detailed connection information (default)
+     - DEBUG: Comprehensive debugging information
+     """
+     SILENT = 1
+     ERROR = 2
+     WARNING = 3
+     NORMAL = 4
+     DETAIL = 5
+     DEBUG = 6
+ 
+ 
+ @dataclass
+ class OpenVPNConfig:
+     """Configuration for OpenVPN connection.
+     
+     This dataclass encapsulates all configuration parameters needed for establishing
+     an OpenVPN connection, ensuring type safety and validation. It serves as a central
+     place for all OpenVPN configuration parameters.
+     
+     Attributes:
          config_path: Path to OpenVPN config file
          auth_path: Path to authentication file
          ping_interval: Interval between ping tests in seconds
          ping_restart: Time without ping response before restart
- 
-     Returns:
-         List of command arguments for OpenVPN
- 
-     Raises:
-         VPNConfigError: If required files don't exist or aren't accessible
- 
-     Note:
-         The command includes security-focused defaults and robust
-         error handling parameters to ensure stable VPN connections.
- 
-     """
-     # Validate required files
-     if not config_path.exists():
-         raise VPNConfigError(f"OpenVPN config file not found: {config_path}")
-     if not auth_path.exists():
-         raise VPNConfigError(f"OpenVPN auth file not found: {auth_path}")
- 
-     # Validate file permissions (should be readable)
-     try:
-         config_path.read_bytes()
-         auth_path.read_bytes()
-     except (PermissionError, OSError) as e:
-         raise VPNConfigError(f"Cannot read OpenVPN files: {e}")
- 
-     # Create log directory if needed
-     if log_path:
-         log_path.parent.mkdir(parents=True, exist_ok=True)
- 
-     # Validate verbosity level
-     if not 1 <= verbosity <= 6:
-         raise VPNConfigError(f"Invalid verbosity level: {verbosity} (must be 1-6)")
- 
+         ciphers: List of encryption ciphers to use
+         tls_ciphers: List of TLS cipher suites to use
+         tls_min_version: Minimum TLS version to use
+         auth_retry_behavior: Authentication retry behavior
+         dns_servers: DNS servers to use (platform-specific)
+         extra_options: Additional OpenVPN command-line options
+     """
+     # Required paths
+     config_path: Path
+     auth_path: Path
+     
+     # Optional paths
+     log_path: Optional[Path] = None
+     
+     # Connection parameters
+     verbosity: Union[OpenVPNVerbosity, int] = OpenVPNVerbosity.DETAIL
+     connect_retry: int = 2
+     connect_timeout: int = 10
+     ping_interval: int = 10
+     ping_restart: int = 60
+     
+     # Security parameters
+     ciphers: List[str] = field(default_factory=lambda: [
+         "AES-256-GCM", 
+         "AES-128-GCM", 
+         "CHACHA20-POLY1305", 
+         "AES-256-CBC"
+     ])
+     tls_ciphers: List[str] = field(default_factory=lambda: [
+         "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384",
+         "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"
+     ])
+     tls_min_version: str = "1.2"
+     auth_retry_behavior: str = "nointeract"
+     
+     # DNS configuration
+     dns_servers: List[str] = field(default_factory=lambda: [
+         "103.86.96.100",  # NordVPN DNS
+         "103.86.99.100"   # NordVPN DNS backup
+     ])
+     
+     # Additional options
+     extra_options: Dict[str, Any] = field(default_factory=dict)
+     
+     def __post_init__(self) -> None:
+         """Validate the configuration after initialization.
+         
+         Performs various validation checks on the configuration to ensure it is valid,
+         including checking file existence, permissions, and parameter constraints.
+         
+         Raises:
+             VPNConfigError: If any validation check fails
+         """
+         # Validate paths
+         self._validate_paths()
+         
+         # Validate verbosity
+         self._validate_verbosity()
+         
+         # Validate numeric parameters
+         self._validate_numeric_params()
+         
+     def _validate_paths(self) -> None:
+         """Validate file paths.
+         
+         Checks that required files exist and are accessible.
+         
+         Raises:
+             VPNConfigError: If any path validation fails
+         """
+         # Convert to Path objects if strings were provided
+         if isinstance(self.config_path, str):
+             self.config_path = Path(self.config_path)
+         if isinstance(self.auth_path, str):
+             self.auth_path = Path(self.auth_path)
+         if isinstance(self.log_path, str):
+             self.log_path = Path(self.log_path)
+             
+         # Check if config file exists
+         if not self.config_path.exists():
+             raise VPNConfigError(f"OpenVPN config file not found: {self.config_path}")
+         
+         # Check if auth file exists
+         if not self.auth_path.exists():
+             raise VPNConfigError(f"OpenVPN auth file not found: {self.auth_path}")
+             
+         # Validate file permissions (should be readable)
+         try:
+             self.config_path.read_bytes()
+             self.auth_path.read_bytes()
+         except (PermissionError, OSError) as e:
+             raise VPNConfigError(f"Cannot read OpenVPN files: {e}")
+             
+         # Create log directory if needed
+         if self.log_path:
+             self.log_path.parent.mkdir(parents=True, exist_ok=True)
+     
+     def _validate_verbosity(self) -> None:
+         """Validate verbosity level.
+         
+         Ensures the verbosity level is either a valid enum value or an integer in the range 1-6.
+         
+         Raises:
+             VPNConfigError: If verbosity validation fails
+         """
+         # Convert integer to enum if needed
+         if isinstance(self.verbosity, int):
+             if not 1 <= self.verbosity <= 6:
+                 raise VPNConfigError(f"Invalid verbosity level: {self.verbosity} (must be 1-6)")
+             # Convert to enum for consistent handling
+             try:
+                 self.verbosity = OpenVPNVerbosity(self.verbosity)
+             except ValueError:
+                 # Keep as int if enum conversion fails (shouldn't happen with range check)
+                 pass
+     
+     def _validate_numeric_params(self) -> None:
+         """Validate numeric parameters.
+         
+         Ensures that numeric parameters are within acceptable ranges.
+         
+         Raises:
+             VPNConfigError: If any numeric parameter validation fails
+         """
+         # Connect retry should be positive
+         if self.connect_retry < 1:
+             raise VPNConfigError(f"Invalid connect_retry value: {self.connect_retry} (must be >= 1)")
+             
+         # Connect timeout should be positive
+         if self.connect_timeout < 1:
+             raise VPNConfigError(f"Invalid connect_timeout value: {self.connect_timeout} (must be >= 1)")
+             
+         # Ping interval should be positive
+         if self.ping_interval < 1:
+             raise VPNConfigError(f"Invalid ping_interval value: {self.ping_interval} (must be >= 1)")
+             
+         # Ping restart should be greater than ping interval
+         if self.ping_restart <= self.ping_interval:
+             raise VPNConfigError(
+                 f"Invalid ping_restart value: {self.ping_restart} "
+                 f"(must be > ping_interval {self.ping_interval})"
+             )
+ 
+ 
+ def get_openvpn_command(config: OpenVPNConfig) -> List[str]:
+     """Construct OpenVPN command with all necessary arguments.
+ 
+     This is the central place for OpenVPN command construction. It provides
+     a comprehensive set of options for connection management, monitoring,
+     and error handling.
+ 
+     Args:
+         config: OpenVPN configuration object
+ 
+     Returns:
+         List of command arguments for OpenVPN
+ 
+     Raises:
+         VPNConfigError: If OpenVPN executable is not found in PATH
+     """
+     # Check if openvpn is installed
+     if not shutil.which("openvpn"):
+         raise VPNConfigError(
+             "OpenVPN executable not found in PATH. "
+             "Please install OpenVPN first."
+         )
+     
      # Base command with common options
      cmd = [
          "openvpn",
-         "--config",
-         str(config_path),
-         "--auth-user-pass",
-         str(auth_path),
-         "--verb",
-         str(verbosity),
-         "--connect-retry",
-         str(connect_retry),
-         "--connect-timeout",
-         str(connect_timeout),
-         "--resolv-retry",
-         "infinite",
-         "--ping",
-         str(ping_interval),
-         "--ping-restart",
-         str(ping_restart),
-         "--script-security",
-         "2",
+         "--config", str(config.config_path),
+         "--auth-user-pass", str(config.auth_path),
+         "--verb", str(config.verbosity.value if isinstance(config.verbosity, OpenVPNVerbosity) else config.verbosity),
+         "--connect-retry", str(config.connect_retry),
+         "--connect-timeout", str(config.connect_timeout),
+         "--resolv-retry", "infinite",
+         "--ping", str(config.ping_interval),
+         "--ping-restart", str(config.ping_restart),
+         "--script-security", "2",
          "--persist-tun",
          "--persist-key",
          "--nobind",
          "--fast-io",
-         "--data-ciphers",
-         "AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC",
-         "--data-ciphers-fallback",
-         "AES-256-CBC",
-         "--auth-retry",
-         "nointeract",
+     ]
+     
+     # Add security parameters
+     cmd.extend([
+         "--data-ciphers", ":".join(config.ciphers),
+         "--data-ciphers-fallback", config.ciphers[-1],  # Last cipher as fallback
+         "--auth-retry", config.auth_retry_behavior,
          "--auth-nocache",
-         "--pull-filter",
-         "ignore",
-         "auth-token",
-         "--tls-version-min",
-         "1.2",
-         "--tls-cipher",
-         "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256",
-     ]
- 
+         "--pull-filter", "ignore", "auth-token",
+         "--tls-version-min", config.tls_min_version,
+         "--tls-cipher", ":".join(config.tls_ciphers),
+     ])
+     
      # Platform-specific options
      system = platform.system().lower()
      if system == "darwin":  # macOS
-         cmd.extend(
-             [
-                 # Basic routing
-                 "--redirect-gateway",
-                 "def1",
-                 # DNS configuration
-                 "--dhcp-option",
-                 "DNS",
-                 "103.86.96.100",  # NordVPN DNS
-                 "--dhcp-option",
-                 "DNS",
-                 "103.86.99.100",  # NordVPN DNS backup
-             ]
-         )
-     else:  # Linux and others
-         # Use standard Linux DNS update scripts if available
-         resolv_conf_script = Path("/etc/openvpn/update-resolv-conf")
-         if resolv_conf_script.exists():
-             cmd.extend(
-                 [
-                     "--up",
-                     str(resolv_conf_script),
-                     "--down",
-                     str(resolv_conf_script),
-                 ]
-             )
- 
-         cmd.extend(
-             [
-                 # Enable routing
-                 "--redirect-gateway",  # Redirect all traffic through VPN
-                 "def1",  # Use default gateway
-                 "bypass-dhcp",  # Don't redirect DHCP
-                 "bypass-dns",  # Don't redirect DNS
-             ]
-         )
- 
+         # Add macOS-specific options
+         _add_macos_options(cmd, config)
+     elif system == "linux":  # Linux
+         # Add Linux-specific options
+         _add_linux_options(cmd, config)
+     elif system == "windows":  # Windows
+         # Add Windows-specific options
+         _add_windows_options(cmd, config)
+     else:
+         logger.warning(f"Unsupported platform: {system}. Using generic options.")
+         # Add generic options for other platforms
+         _add_generic_options(cmd, config)
+     
      # Add log file if specified
-     if log_path:
-         cmd.extend(["--log", str(log_path)])
- 
+     if config.log_path:
+         cmd.extend(["--log", str(config.log_path)])
+     
+     # Add any extra options
+     for key, value in config.extra_options.items():
+         if value is True:
+             # Boolean flag (--flag)
+             cmd.append(f"--{key}")
+         elif value is not None:
+             # Option with value (--option value)
+             cmd.append(f"--{key}")
+             cmd.append(str(value))
+     
      return cmd
+ 
+ 
+ def _add_macos_options(cmd: List[str], config: OpenVPNConfig) -> None:
+     """Add macOS-specific OpenVPN options.
+     
+     Args:
+         cmd: Command list to extend
+         config: OpenVPN configuration
+     """
+     cmd.extend([
+         # Basic routing
+         "--redirect-gateway", "def1",
+     ])
+     
+     # Add DNS configuration
+     for dns_server in config.dns_servers:
+         cmd.extend(["--dhcp-option", "DNS", dns_server])
+ 
+ 
+ def _add_linux_options(cmd: List[str], config: OpenVPNConfig) -> None:
+     """Add Linux-specific OpenVPN options.
+     
+     Args:
+         cmd: Command list to extend
+         config: OpenVPN configuration
+     """
+     # Use standard Linux DNS update scripts if available
+     resolv_conf_script = Path("/etc/openvpn/update-resolv-conf")
+     if resolv_conf_script.exists():
+         cmd.extend([
+             "--up", str(resolv_conf_script),
+             "--down", str(resolv_conf_script),
+         ])
+     
+     cmd.extend([
+         # Enable routing
+         "--redirect-gateway",  # Redirect all traffic through VPN
+         "def1",               # Use default gateway
+         "bypass-dhcp",        # Don't redirect DHCP
+         "bypass-dns",         # Don't redirect DNS
+     ])
+     
+     # Add DNS configuration (if update-resolv-conf is not available)
+     if not resolv_conf_script.exists():
+         for dns_server in config.dns_servers:
+             cmd.extend(["--dhcp-option", "DNS", dns_server])
+ 
+ 
+ def _add_windows_options(cmd: List[str], config: OpenVPNConfig) -> None:
+     """Add Windows-specific OpenVPN options.
+     
+     Args:
+         cmd: Command list to extend
+         config: OpenVPN configuration
+     """
+     cmd.extend([
+         # Basic routing
+         "--redirect-gateway", "def1",
+     ])
+     
+     # Add DNS configuration
+     for dns_server in config.dns_servers:
+         cmd.extend(["--dhcp-option", "DNS", dns_server])
+ 
+ 
+ def _add_generic_options(cmd: List[str], config: OpenVPNConfig) -> None:
+     """Add generic OpenVPN options for unsupported platforms.
+     
+     Args:
+         cmd: Command list to extend
+         config: OpenVPN configuration
+     """
+     cmd.extend([
+         # Basic routing
+         "--redirect-gateway", "def1",
+     ])
+     
+     # Add DNS configuration
+     for dns_server in config.dns_servers:
+         cmd.extend(["--dhcp-option", "DNS", dns_server])
+ 
+ 
+ # Example usage
+ def create_default_config(config_path: Path, auth_path: Path, log_path: Optional[Path] = None) -> OpenVPNConfig:
+     """Create a default OpenVPN configuration.
+     
+     This is a helper function to create a default configuration with reasonable values.
+     
+     Args:
+         config_path: Path to OpenVPN config file
+         auth_path: Path to authentication file
+         log_path: Optional path to log file
+         
+     Returns:
+         A configured OpenVPNConfig object
+         
+     Raises:
+         VPNConfigError: If validation fails
+     """
+     return OpenVPNConfig(
+         config_path=config_path,
+         auth_path=auth_path,
+         log_path=log_path,
+         verbosity=OpenVPNVerbosity.DETAIL,
+         connect_retry=2,
+         connect_timeout=10,
+         ping_interval=10,
+         ping_restart=60
+     )
  
```

---

_****_



Now, let's run a linting check to ensure our changes are consistent with the project's style:

---

_****_

```bash
ruff check --output-format=github --fix --unsafe-fixes src/nyord_vpn/network/vpn_commands.py && ruff format --respect-gitignore --target-version py312 src/nyord_vpn/network/vpn_commands.py
```

```
warning: Selection `DOC` has no effect because preview is not enab
led.                                                              ::error title=
Ruff (TRY003),file=/Users/adam/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=150,col=19,end
Line=150,endColumn=87::src/nyord_vpn/network/vpn_commands.py:150:19: TRY003 Avoi
d specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=154,col=19,end
Line=154,endColumn=83::src/nyord_vpn/network/vpn_commands.py:154:19: TRY003 Avoi
d specifying long messages outside the exception class
                        ::error title=Ruff (B904),file=/Users/adam/Developer/vcs
/github.tw
ardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=161,col=13,endLi
ne=161,endColumn=68::src/nyord_vpn/network/vpn_commands.py:161:13: B904 Within a
n `except` clause, raise exceptions with `raise ... from err` or `raise ... from
 None` to distinguish them from errors in exception handling
          ::error title=Ruff (TRY003),file=/Users/adam/Developer/vcs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=161,col=19,end
Line=161,endColumn=68::src/nyord_vpn/network/vpn_commands.py:161:19: TRY003 Avoi
d specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=179,col=23,end
Line=179,endColumn=97::src/nyord_vpn/network/vpn_commands.py:179:23: TRY003 Avoi
d specifying long messages outside the exception class
                        ::error title=Ruff (SIM105),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=181,col=13,end
Line=185,endColumn=21::src/nyord_vpn/network/vpn_commands.py:181:13: SIM105 Use
`contextlib.suppress(ValueError)` instead of `try`-`except`-`pass`
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=198,col=19,end
Line=198,endColumn=102::src/nyord_vpn/network/vpn_commands.py:198:19: TRY003 Avo
id specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=202,col=19,end
Line=202,endColumn=106::src/nyord_vpn/network/vpn_commands.py:202:19: TRY003 Avo
id specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=206,col=19,end
Line=206,endColumn=102::src/nyord_vpn/network/vpn_commands.py:206:19: TRY003 Avo
id specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=210,col=19,end
Line=213,endColumn=14::src/nyord_vpn/network/vpn_commands.py:210:19: TRY003 Avoi
d specifying long messages outside the exception class
                        ::error title=Ruff (TRY003),file=/Users/adam/Developer/v
cs/github.
twardoch/pub/nyord_vpn/src/nyord_vpn/network/vpn_commands.py,line=235,col=15,end
Line=238,endColumn=10::src/nyord_vpn/network/vpn_commands.py:235:15: TRY003 Avoi
d specifying long messages outside the exception class
                        %
          

```

---

_****_





Let's fix the linting issues in the vpn_commands.py file:

---

_****_

```diff
  
  import platform
+ import os
  import shutil
  from dataclasses import dataclass, field
- from enum import Enum
+ from enum import Enum, auto
  from pathlib import Path
- from typing import Any
+ import contextlib
+ from typing import Optional, List, Dict, Union, Any
  
  from loguru import logger
  
  from nyord_vpn.exceptions import VPNConfigError
+ 
+ 
+ # Error message constants to avoid TRY003 linting issues
+ CONFIG_FILE_NOT_FOUND = "OpenVPN config file not found"
+ AUTH_FILE_NOT_FOUND = "OpenVPN auth file not found"
+ CANNOT_READ_FILES = "Cannot read OpenVPN files"
+ INVALID_VERBOSITY = "Invalid verbosity level (must be 1-6)"
+ INVALID_CONNECT_RETRY = "Invalid connect_retry value (must be >= 1)"
+ INVALID_CONNECT_TIMEOUT = "Invalid connect_timeout value (must be >= 1)"
+ INVALID_PING_INTERVAL = "Invalid ping_interval value (must be >= 1)"
+ INVALID_PING_RESTART = "Invalid ping_restart value (must be > ping_interval)"
+ OPENVPN_NOT_FOUND = "OpenVPN executable not found in PATH"
  
  
  
      # Optional paths
-     log_path: Path | None = None
+     log_path: Optional[Path] = None
  
      # Connection parameters
-     verbosity: OpenVPNVerbosity | int = OpenVPNVerbosity.DETAIL
+     verbosity: Union[OpenVPNVerbosity, int] = OpenVPNVerbosity.DETAIL
      connect_retry: int = 2
      connect_timeout: int = 10
  
      # Security parameters
-     ciphers: list[str] = field(default_factory=lambda: [
+     ciphers: List[str] = field(default_factory=lambda: [
          "AES-256-GCM",
          "AES-128-GCM",
          "CHACHA20-POLY1305",
          "AES-256-CBC"
      ])
-     tls_ciphers: list[str] = field(default_factory=lambda: [
+     tls_ciphers: List[str] = field(default_factory=lambda: [
          "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384",
          "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"
  
      # DNS configuration
-     dns_servers: list[str] = field(default_factory=lambda: [
+     dns_servers: List[str] = field(default_factory=lambda: [
          "103.86.96.100",  # NordVPN DNS
          "103.86.99.100"   # NordVPN DNS backup
      ])
  
      # Additional options
-     extra_options: dict[str, Any] = field(default_factory=dict)
+     extra_options: Dict[str, Any] = field(default_factory=dict)
  
      def __post_init__(self) -> None:
          # Check if config file exists
          if not self.config_path.exists():
-             raise VPNConfigError(f"OpenVPN config file not found: {self.config_path}")
+             raise VPNConfigError(f"{CONFIG_FILE_NOT_FOUND}: {self.config_path}")
  
          # Check if auth file exists
          if not self.auth_path.exists():
-             raise VPNConfigError(f"OpenVPN auth file not found: {self.auth_path}")
+             raise VPNConfigError(f"{AUTH_FILE_NOT_FOUND}: {self.auth_path}")
  
          # Validate file permissions (should be readable)
              self.auth_path.read_bytes()
          except (PermissionError, OSError) as e:
-             raise VPNConfigError(f"Cannot read OpenVPN files: {e}")
+             raise VPNConfigError(f"{CANNOT_READ_FILES}: {e}") from e
  
          # Create log directory if needed
          if isinstance(self.verbosity, int):
              if not 1 <= self.verbosity <= 6:
-                 raise VPNConfigError(f"Invalid verbosity level: {self.verbosity} (must be 1-6)")
+                 raise VPNConfigError(f"{INVALID_VERBOSITY}: {self.verbosity}")
              # Convert to enum for consistent handling
-             try:
+             with contextlib.suppress(ValueError):
                  self.verbosity = OpenVPNVerbosity(self.verbosity)
-             except ValueError:
-                 # Keep as int if enum conversion fails (shouldn't happen with range check)
-                 pass
  
      def _validate_numeric_params(self) -> None:
          # Connect retry should be positive
          if self.connect_retry < 1:
-             raise VPNConfigError(f"Invalid connect_retry value: {self.connect_retry} (must be >= 1)")
+             raise VPNConfigError(f"{INVALID_CONNECT_RETRY}: {self.connect_retry}")
  
          # Connect timeout should be positive
          if self.connect_timeout < 1:
-             raise VPNConfigError(f"Invalid connect_timeout value: {self.connect_timeout} (must be >= 1)")
+             raise VPNConfigError(f"{INVALID_CONNECT_TIMEOUT}: {self.connect_timeout}")
  
          # Ping interval should be positive
          if self.ping_interval < 1:
-             raise VPNConfigError(f"Invalid ping_interval value: {self.ping_interval} (must be >= 1)")
+             raise VPNConfigError(f"{INVALID_PING_INTERVAL}: {self.ping_interval}")
  
          # Ping restart should be greater than ping interval
          if self.ping_restart <= self.ping_interval:
              raise VPNConfigError(
-                 f"Invalid ping_restart value: {self.ping_restart} "
-                 f"(must be > ping_interval {self.ping_interval})"
+                 f"{INVALID_PING_RESTART}: {self.ping_restart} (ping_interval: {self.ping_interval})"
              )
  
  
- def get_openvpn_command(config: OpenVPNConfig) -> list[str]:
+ def get_openvpn_command(config: OpenVPNConfig) -> List[str]:
      """Construct OpenVPN command with all necessary arguments.
  
      # Check if openvpn is installed
      if not shutil.which("openvpn"):
-         raise VPNConfigError(
-             "OpenVPN executable not found in PATH. "
-             "Please install OpenVPN first."
-         )
+         raise VPNConfigError(f"{OPENVPN_NOT_FOUND}. Please install OpenVPN first.")
  
      # Base command with common options
  
  
- def _add_macos_options(cmd: list[str], config: OpenVPNConfig) -> None:
+ def _add_macos_options(cmd: List[str], config: OpenVPNConfig) -> None:
      """Add macOS-specific OpenVPN options.
  
  
  
- def _add_linux_options(cmd: list[str], config: OpenVPNConfig) -> None:
+ def _add_linux_options(cmd: List[str], config: OpenVPNConfig) -> None:
      """Add Linux-specific OpenVPN options.
  
  
  
- def _add_windows_options(cmd: list[str], config: OpenVPNConfig) -> None:
+ def _add_windows_options(cmd: List[str], config: OpenVPNConfig) -> None:
      """Add Windows-specific OpenVPN options.
  
  
  
- def _add_generic_options(cmd: list[str], config: OpenVPNConfig) -> None:
+ def _add_generic_options(cmd: List[str], config: OpenVPNConfig) -> None:
      """Add generic OpenVPN options for unsupported platforms.
  
  
  # Example usage
- def create_default_config(config_path: Path, auth_path: Path, log_path: Path | None = None) -> OpenVPNConfig:
+ def create_default_config(config_path: Path, auth_path: Path, log_path: Optional[Path] = None) -> OpenVPNConfig:
      """Create a default OpenVPN configuration.
  
```

---

_****_



---



---

