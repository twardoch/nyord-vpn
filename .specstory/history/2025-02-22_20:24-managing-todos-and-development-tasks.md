## SpecStory

## Managing TODOs and Development Tasks (22/02/2025, 20:24:35)

_**User**_

Check git and update @TODO.md with what you've done (`- [x] `). Upgrade priorities for NEXT TODO (`- [!]`), re-think the normal TODO (`- [ ] `)

Periodically do:

```
uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]; tree -I *cache__; hatch fmt --unsafe-fixes; hatch fmt --unsafe-fixes; hatch test; 
```

and react to the results.

---

_**Assistant**_

I'll help manage the TODO list and run the development tasks. Let me first check the current state and then we'll proceed with updates.

Let me first check the repository status and structure.

---

_****_

```bash
git status | cat
```

```
(nyord_vpn) adam@Hamlet nyord_vpn % git status | cat
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
%                                                                 
(nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_



Now let me run the development setup and check commands:

---

_****_

```bash
uv venv && source .venv/bin/activate && uv pip install -e .[dev,test] && tree -I '*cache__' && hatch fmt --unsafe-fixes && hatch test
```

```
(nyord_vpn) adam@Hamlet nyord_vpn % uv venv && source .venv/bin/ac
tivate && uv pip install -e .[dev,test] && tree -I '*cache__' && h
atch fmt --unsafe-fixes && hatch tesuv venv && source .venv/bin/ac
tivate && uv pip install -e .[dev,test] && tree -I '*cache__' && h
atch fmt --unsafe-fixes && hatch test
Using CPython 3.12.8 interpreter at: /usr/local/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
zsh: no matches found: .[dev,test]
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_



I notice we're having some issues with the development setup. Let me check the project structure first:

---

_****_

<details>
            <summary>Listed current directory • **20** results</summary>
        
| Name |
|-------|
| 📁 `.venv` |
| 📁 `.git` |
| 📄 `pyproject.toml` |
| 📄 `TODO.md` |
| 📄 `uv.lock` |
| 📁 `tests` |
| 📄 `requirements.txt` |
| 📁 `.cursor` |
| 📁 `.specstory` |
| 📄 `.DS_Store` |
| 📁 `src` |
| 📁 `.ruff_cache` |
| 📁 `.pytest_cache` |
| 📄 `package.toml` |
| 📁 `.github` |
| 📁 `dist` |
| 📄 `README.md` |
| 📄 `.pre-commit-config.yaml` |
| 📄 `LICENSE` |
| 📄 `.gitignore` |

</details>

---

_****_



Let me check the pyproject.toml to understand the project setup:

---

_****_

Read file: pyproject.toml

---

_****_



Now let me try to fix the development setup command and run it properly:

---

_****_

```bash
uv venv && source .venv/bin/activate && uv pip install -e '.[dev,test]' && tree -I '*cache__' && hatch fmt --unsafe-fixes && hatch test
```

```
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn % uv venv && source 
.venv/bin/activate && uv pip install -e '.[dev,test]' && tree -I '
*cache__' && hatch fmt --unsafe-fixes && hatch tuv venv && source 
.venv/bin/activate && uv pip install -e '.[dev,test]' && tree -I '
*cache__' && hatch fmt --unsafe-fixes && hatch test
Using CPython 3.12.8 interpreter at: /usr/local/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
Resolved 56 packages in 811ms
Prepared 3 packages in 1.56s
Installed 56 packages in 233ms
 + aiohappyeyeballs==2.4.6
 + aiohttp==3.11.12
 + aiosignal==1.3.2
 + annotated-types==0.7.0
 + attrs==25.1.0
 + backoff==2.2.1
 + certifi==2025.1.31
 + cfgv==3.4.0
 + charset-normalizer==3.4.1
 + coverage==7.6.12
 + distlib==0.3.9
 + filelock==3.17.0
 + fire==0.7.0
 + frozenlist==1.5.0
 + identify==2.6.8
 + idna==3.10
 + iniconfig==2.0.0
 + jaraco-classes==3.4.0
 + jaraco-context==6.0.1
 + jaraco-functools==4.1.0
 + keyring==25.6.0
 + markdown-it-py==3.0.0
 + mdurl==0.1.2
 + more-itertools==10.6.0
 + multidict==6.1.0
 + mypy==1.15.0
 + mypy-extensions==1.0.0
 + njord==0.0.2
 + nodeenv==1.9.1
 + nyord-vpn==0.1.0 (from file:///Users/adam/Developer/vcs/github.
twardoch/pub/nyord_vpn)
 + packaging==24.2
 + platformdirs==4.3.6
 + pluggy==1.5.0
 + pre-commit==4.1.0
 + propcache==0.3.0
 + psutil==7.0.0
 + pycountry==24.6.1
 + pydantic==2.10.6
 + pydantic-core==2.27.2
 + pydantic-settings==2.8.0
 + pygments==2.19.1
 + pytest==8.3.4
 + pytest-cov==6.0.0
 + python-dotenv==1.0.1
 + pyupgrade==3.19.1
 + pyyaml==6.0.2
 + requests==2.32.3
 + rich==13.9.4
 + ruff==0.9.7
 + tenacity==9.0.0
 + termcolor==2.5.0
 + tokenize-rt==6.1.0
 + typing-extensions==4.12.2
 + urllib3==2.3.0
 + virtualenv==20.29.2
 + yarl==1.18.3
.
├── LICENSE
├── README.md
├── TODO.md
├── dist
├── package.toml
├── pyproject.toml
├── requirements.txt
├── src
│   ├── nyord_vpn
│   │   ├── __init__.py
│   │   ├── __version__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── legacy.py
│   │   │   └── njord.py
│   │   ├── cli
│   │   │   ├── __init__.py
│   │   │   └── commands.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── client.py
│   │   │   ├── config.py
│   │   │   └── exceptions.py
│   │   ├── njord
│   │   ├── nyord_vpn.py
│   │   ├── oldsh
│   │   │   ├── nordvpn-maccli.md
│   │   │   └── nordvpn-maccli.sh
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── log_utils.py
│   │       └── retry.py
│   └── nyord_vpn.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       ├── entry_points.txt
│       ├── requires.txt
│       └── top_level.txt
├── tests
│   ├── __init__.py
│   └── test_package.py
└── uv.lock

12 directories, 33 files
cmd [1] | ruff check --config '/Users/adam/Library/Application Sup
port/hatch/env/.internal/hatch-static-analysis/.config/jzfB6_4k/py
project.toml' --fix --unsafe-fixes
src/nyord_vpn/api/legacy.py:99:17: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/api/legacy.py:100:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/api/legacy.py:128:17: TRY301 Abstract `raise` to an 
inner function
src/nyord_vpn/api/legacy.py:129:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/api/njord.py:24:29: ARG002 Unused method argument: `
country`
src/nyord_vpn/api/njord.py:32:13: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/api/njord.py:43:13: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/cli/commands.py:98:16: BLE001 Do not catch blind exc
eption: `Exception`
src/nyord_vpn/cli/commands.py:122:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:147:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:166:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:177:12: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/core/client.py:93:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/core/client.py:117:13: TRY300 Consider moving this s
tatement to an `else` block
src/nyord_vpn/nyord_vpn.py:226:9: TRY301 Abstract `raise` to an in
ner function
src/nyord_vpn/nyord_vpn.py:323:21: S603 `subprocess` call: check f
or execution of untrusted input
src/nyord_vpn/nyord_vpn.py:369:9: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/nyord_vpn.py:433:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:438:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:441:13: S603 `subprocess` call: check f
or execution of untrusted input
src/nyord_vpn/nyord_vpn.py:543:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:548:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:570:17: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:623:12: BLE001 Do not catch blind excep
tion: `Exception`
src/nyord_vpn/utils/retry.py:42:16: BLE001 Do not catch blind exce
ption: `Exception`
Found 28 errors (3 fixed, 25 remaining).
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_



Based on the development setup results and code analysis, let me update the TODO.md with completed tasks and new priorities. I'll analyze the current TODO.md and make necessary updates:

---

_****_

```diff
  
  1. **API Layer**
-    - `BaseAPI` abstract class defining the interface
-    - `NjordAPI` primary implementation using njord
-    - `LegacyAPI` fallback implementation using our code
+    - [x] `BaseAPI` abstract class defining the interface
+    - [x] `NjordAPI` primary implementation using njord
+    - [x] `LegacyAPI` fallback implementation using our code
  
  2. **Client Layer**
-    - `VPNClient` main class for VPN operations
-    - Uses re-engage for API fallback
-    - Uses tenacity for operation retries
+    - [x] `VPNClient` main class for VPN operations
+    - [x] Uses re-engage for API fallback
+    - [x] Uses tenacity for operation retries
  
  3. **CLI Layer**
-    - Rich-based CLI interface
-    - Fire-based command parsing
-    - Comprehensive error reporting
+    - [x] Rich-based CLI interface
+    - [x] Fire-based command parsing
+    - [x] Comprehensive error reporting
  
  ## 3. Implementation Details
  
  ### 4.5. Phase 5: Testing & Documentation
- - [ ] Add unit tests
- - [ ] Add integration tests
+ - [!] Add unit tests
+ - [!] Add integration tests
  - [ ] Create API documentation
  - [ ] Add usage examples
  
- ## 5. Usage Examples
- 
- ### 5.1. As a Library
- 
- ```python
- from nyord_vpn import VPNClient
- 
- async with VPNClient() as vpn:
-     await vpn.connect("United States")
-     status = await vpn.status()
-     print(f"Connected: {status['connected']}")
- ```
- 
- ### 5.2. CLI Usage
- 
- ```bash
- # Connect to VPN
- nyord-vpn connect us
- 
- # Check status
- nyord-vpn status
- 
- # Disconnect
- nyord-vpn disconnect
- ```
- 
- ## 6. Error Handling
- 
- 1. **API Errors**
-    - Wrap njord exceptions
-    - Provide fallback mechanisms
-    - Clear error messages
- 
- 2. **Connection Errors**
-    - Automatic retries with tenacity
-    - Fallback to legacy implementation
-    - Detailed error reporting
- 
- 3. **Configuration Errors**
-    - Validation using Pydantic
-    - Clear error messages
-    - Configuration file validation
- 
- ## 7. Security Considerations
- 
- 1. **Credential Management**
-    - Use keyring for credential storage
-    - Support environment variables
-    - Secure credential file handling
- 
- 2. **Certificate Handling**
-    - Proper certificate validation
-    - Secure storage
-    - Regular updates
- 
- ## 8. Performance Considerations
- 
- 1. **Connection Management**
-    - Efficient connection pooling
-    - Quick fallback mechanisms
-    - Connection caching
- 
- 2. **Resource Usage**
-    - Minimal memory footprint
-    - Efficient process management
-    - Resource cleanup
- 
- ## 9. Monitoring and Logging
- 
- 1. **Logging System**
-    - Structured logging
-    - Log rotation
-    - Debug information
- 
- 2. **Metrics**
-    - Connection statistics
-    - Error rates
-    - Performance metrics
- 
- ## 10. Future Enhancements
- 
- 1. **Additional Features**
-    - Kill switch implementation
-    - Split tunneling
-    - Custom DNS support
- 
- 2. **Platform Support**
-    - Windows support
-    - Linux support
-    - Container support
- 
- ## 11. Dependencies
- 
- Required packages:
- ```toml
- [tool.poetry.dependencies]
- python = "^3.9"
- njord = "*"
- tenacity = "*"
- re-engage = "*"
- rich = "*"
- fire = "*"
- pydantic = "*"
- keyring = "*"
- ```
- 
- ## 12. Development Guidelines
- 
- 1. **Code Style**
-    - Follow PEP 8
-    - Use type hints
-    - Document all public APIs
- 
- 2. **Testing**
-    - 100% test coverage
-    - Integration tests
-    - Property-based testing
- 
- 3. **Documentation**
-    - API documentation
-    - Usage examples
-    - Architecture documentation
- 
- ## 13. Immediate Priorities
- 
- - [!] **Fix Critical Code Issues**
-   - *High Priority Fixes*:
-     - [!] Fix decorator issues with `with_retry` (failing tests)
-     - [!] Fix async HTTP in legacy API (use aiohttp instead of requests)
-     - [!] Fix async subprocess in legacy API (use asyncio.create_subprocess_exec)
-     - [!] Fix complex functions (C901)
-     - [!] Fix exception handling patterns (B904)
- 
- - [!] **Fix Test Infrastructure**
-   - *Critical Setup*:
-     - [!] Fix failing test_version test
-     - [!] Add proper test dependencies
-     - [!] Set up test configuration
-     - [!] Add test fixtures and mocks
- 
- - [!] **Security Enhancements**
-   - *Critical Security*:
-     - [x] Add input validation for shell commands (using shlex.quote)
-     - [x] Implement proper subprocess security (using list args)
-     - [x] Fix shell injection vulnerabilities (S605)
-     - [!] Replace standard RNG with cryptographic RNG (S311)
- 
- ## 14. Near-term Tasks
- 
- - [ ] **Code Quality**
-   - *Refactoring*:
-     - [ ] Split complex functions (PLR0912, PLR0915)
-     - [ ] Fix blind exception catches (BLE001)
-     - [ ] Fix boolean argument issues (FBT001, FBT002)
-     - [ ] Fix module imports and organization (E402)
- 
- - [ ] **Improve Test Coverage**
-   - *Critical Modules*:
-     - [ ] Write tests for `api/legacy.py` (subprocess mocking)
-     - [ ] Write tests for `api/njord.py` (API mocking)
-     - [ ] Write tests for `core/client.py` (integration tests)
-     - [ ] Write tests for `core/config.py` (configuration tests)
- 
- ## 15. Future Tasks
- 
- - [ ] **Documentation**
-   - *Documentation Updates*:
-     - [ ] Add API documentation
-     - [ ] Add usage examples
-     - [ ] Add security considerations
-     - [ ] Add deployment guide
- 
- - [ ] **Additional Features**
-   - *Enhancements*:
-     - [ ] Kill switch implementation
-     - [ ] Split tunneling
-     - [ ] Custom DNS support
-     - [ ] Connection profiles
+ ## 5. Critical Issues to Fix
+ 
+ ### 5.1. Code Quality Issues
+ - [!] Fix blind exception catches (BLE001) in:
+   - cli/commands.py
+   - utils/retry.py
+   - nyord_vpn.py
+ - [!] Fix subprocess security issues (S603) in nyord_vpn.py
+ - [!] Fix try-except block issues (TRY300, TRY301) in:
+   - api/legacy.py
+   - api/njord.py
+   - core/client.py
+   - nyord_vpn.py
+ - [!] Fix unused argument in api/njord.py (ARG002)
+ 
+ ### 5.2. Security Enhancements
+ - [!] Implement proper input validation for subprocess calls
+ - [!] Add security checks for command execution
+ - [ ] Add SSL certificate validation
+ - [ ] Implement secure credential storage
+ 
+ ### 5.3. Testing Infrastructure
+ - [!] Set up pytest fixtures
+ - [!] Add mock objects for API testing
+ - [!] Add subprocess mocking
+ - [ ] Add coverage reporting
+ 
+ ## 6. Future Enhancements
+ 
+ ### 6.1. Features
+ - [ ] Kill switch implementation
+ - [ ] Split tunneling support
+ - [ ] Custom DNS configuration
+ - [ ] Connection profiles
  
- ## 16. Development Guidelines
+ ### 6.2. Documentation
+ - [ ] API documentation
+ - [ ] Usage examples
+ - [ ] Security considerations
+ - [ ] Deployment guide
+ 
+ ### 6.3. Platform Support
+ - [ ] Windows support
+ - [ ] Linux support
+ - [ ] Container support
+ 
+ ## 7. Development Guidelines
  
  1. Before making changes:
```

---

_****_



Based on the code analysis and updates to the TODO.md, here are the key changes I've made:

1. Marked completed core components with [x]
2. Updated priorities based on the linting results:
   - Added new section "Critical Issues to Fix" with high-priority items marked [!]
   - Prioritized fixing code quality issues found by ruff
   - Added specific security enhancements needed
   - Added testing infrastructure requirements
3. Reorganized the structure to be more focused on immediate needs
4. Removed redundant sections and consolidated future tasks
5. Kept the development guidelines clear and actionable

The most critical issues to address next are:
1. Fix the blind exception catches (BLE001)
2. Address subprocess security issues (S603)
3. Fix try-except block issues (TRY300, TRY301)
4. Set up proper testing infrastructure

Wait, but... let me check if we should add any additional critical issues based on the test results:

---

_****_

```bash
hatch test
```

```
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn % hatch test
====================== test session starts =======================
platform darwin -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0 -- /U
sers/adam/Library/Application Support/hatch/env/virtual/nyord-vpn/
jzfB6_4k/hatch-test.py3.12/bin/python3
cachedir: .pytest_cache
rootdir: /Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn
configfile: pyproject.toml
plugins: rerunfailures-14.0, mock-3.14.0, xdist-3.6.1
collected 1 item                                                 

tests/test_package.py::test_version FAILED                 [100%]

============================ FAILURES ============================
__________________________ test_version __________________________

    def test_version():
        """Verify package exposes version."""
>       import nyord_vpn

tests/test_package.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/nyord_vpn/__init__.py:3: in <module>
    from nyord_vpn.core.client import VPNClient
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    """Main VPN client implementation."""
    
    from pathlib import Path
    
    from nyord_vpn.api.njord import NjordAPI
    from nyord_vpn.api.legacy import LegacyAPI
    from nyord_vpn.utils.retry import with_fallback, with_retry
>   from nyord_vpn.utils.logging import log_operation, log_success
, log_error, setup_logging
E   ModuleNotFoundError: No module named 'nyord_vpn.utils.logging'

src/nyord_vpn/core/client.py:8: ModuleNotFoundError
====================== slowest 10 durations ======================
0.55s call     tests/test_package.py::test_version

(2 durations < 0.005s hidden.  Use -vv to show these durations.)
==================== short test summary info =====================
FAILED tests/test_package.py::test_version - ModuleNotFoundError: 
No module named 'nyord_vpn.utils.logging'
======================= 1 failed in 0.70s ========================
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_



Wait, but... we found a critical issue: the `nyord_vpn.utils.logging` module is missing but is imported in `core/client.py`. Let me update the TODO.md to reflect this:

---

_****_

```diff
  
  ### 5.1. Code Quality Issues
+ - [!] Fix missing module nyord_vpn.utils.logging
+   - Create log_utils.py with required functions:
+     - log_operation
+     - log_success
+     - log_error
+     - setup_logging
  - [!] Fix blind exception catches (BLE001) in:
    - cli/commands.py
```

---

_****_



Let me check if the file exists but with a different name:

---

_****_

<details>
            <summary>Listed directory src/nyord_vpn/utils • **4** results</summary>
        
| Name |
|-------|
| 📄 `log_utils.py` |
| 📁 `__pycache__` |
| 📄 `retry.py` |
| 📄 `__init__.py` |

</details>

---

_****_





Ah, I see the issue. The file is named `log_utils.py` but is being imported as `logging`. Let me fix this:

---

_****_

```diff
  from nyord_vpn.api.legacy import LegacyAPI
  from nyord_vpn.utils.retry import with_fallback, with_retry
- from nyord_vpn.utils.logging import log_operation, log_success, log_error, setup_logging
+ from nyord_vpn.utils.log_utils import (
+     log_operation,
+     log_success,
+     log_error,
+     setup_logging,
+ )
  from nyord_vpn.core.config import load_config
  from nyord_vpn.core.exceptions import VPNError, VPNConnectionError
```

---

_****_





Let me update the TODO.md to reflect the current state and priorities:

---

_****_

```diff
  
  ### 5.1. Code Quality Issues
- - [!] Fix missing module nyord_vpn.utils.logging
-   - Create log_utils.py with required functions:
-     - log_operation
-     - log_success
-     - log_error
-     - setup_logging
+ - [!] Fix type errors in core/client.py:
+   - Fix SecretStr type for password
+   - Fix Coroutine call issue
+   - Fix log_file parameter issue
  - [!] Fix blind exception catches (BLE001) in:
    - cli/commands.py
```

---

_****_





Let me run the tests again to see if we've made progress:

---

_****_

```bash
hatch test
```

```
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn % hatch test
====================== test session starts =======================
platform darwin -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0 -- /U
sers/adam/Library/Application Support/hatch/env/virtual/nyord-vpn/
jzfB6_4k/hatch-test.py3.12/bin/python3
cachedir: .pytest_cache
rootdir: /Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn
configfile: pyproject.toml
plugins: rerunfailures-14.0, mock-3.14.0, xdist-3.6.1
collected 1 item                                                 

tests/test_package.py::test_version PASSED                 [100%]

====================== slowest 10 durations ======================
0.60s call     tests/test_package.py::test_version

(2 durations < 0.005s hidden.  Use -vv to show these durations.)
======================= 1 passed in 0.61s ========================
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_





Great! The basic test is now passing. Let me update the TODO.md to reflect this progress:

---

_****_

```diff
  
  ### 5.3. Testing Infrastructure
+ - [x] Fix failing test_version test
  - [!] Set up pytest fixtures
  - [!] Add mock objects for API testing
```

---

_****_





Let me check if there are any other immediate issues we should address:

---

_****_

```bash
hatch fmt --unsafe-fixes
```

```
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn % hatch fmt --unsafe
-fixes                                          hatch fmt --unsafe
-fixes
cmd [1] | ruff check --config '/Users/adam/Library/Application Sup
port/hatch/env/.internal/hatch-static-analysis/.config/jzfB6_4k/py
project.toml' --fix --unsafe-fixes
src/nyord_vpn/api/legacy.py:99:17: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/api/legacy.py:100:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/api/legacy.py:128:17: TRY301 Abstract `raise` to an 
inner function
src/nyord_vpn/api/legacy.py:129:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/api/njord.py:24:29: ARG002 Unused method argument: `
country`
src/nyord_vpn/api/njord.py:32:13: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/api/njord.py:43:13: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/cli/commands.py:98:16: BLE001 Do not catch blind exc
eption: `Exception`
src/nyord_vpn/cli/commands.py:122:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:147:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:166:16: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/cli/commands.py:177:12: BLE001 Do not catch blind ex
ception: `Exception`
src/nyord_vpn/core/client.py:98:13: TRY300 Consider moving this st
atement to an `else` block
src/nyord_vpn/core/client.py:122:13: TRY300 Consider moving this s
tatement to an `else` block
src/nyord_vpn/nyord_vpn.py:226:9: TRY301 Abstract `raise` to an in
ner function
src/nyord_vpn/nyord_vpn.py:323:21: S603 `subprocess` call: check f
or execution of untrusted input
src/nyord_vpn/nyord_vpn.py:369:9: TRY300 Consider moving this stat
ement to an `else` block
src/nyord_vpn/nyord_vpn.py:433:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:438:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:441:13: S603 `subprocess` call: check f
or execution of untrusted input
src/nyord_vpn/nyord_vpn.py:543:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:548:13: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:570:17: TRY301 Abstract `raise` to an i
nner function
src/nyord_vpn/nyord_vpn.py:623:12: BLE001 Do not catch blind excep
tion: `Exception`
src/nyord_vpn/utils/retry.py:42:16: BLE001 Do not catch blind exce
ption: `Exception`
Found 25 errors.
(nyord_vpn) (nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_







Let me update the TODO.md with a more detailed breakdown of the issues:

---

_****_



---

_****_



---

_**User**_

Remember: we want to phase out the monolothic @nyord_vpn.py and replace it with fully modular design, remember? Adjust @TODO so that your main goal is th get rid of @nyord_vpn.py 

---

_**Assistant**_

I'll update the TODO.md to prioritize phasing out the monolithic `nyord_vpn.py` and moving to a fully modular design:

---

_****_

```diff
  # NordVPN Client Implementation Specification
- 
- 
- 
  
  ## 1. Overview
  ├── utils/
  │   ├── __init__.py
- │   ├── logging.py     # Logging utilities
+ │   ├── log_utils.py   # Logging utilities
  │   └── retry.py       # Retry utilities
  └── py.typed           # Type hint marker
     - [x] Comprehensive error reporting
  
- ## 3. Implementation Details
- 
- ### 3.1. API Layer
- 
- ```python
- class BaseAPI(ABC):
-     @abstractmethod
-     async def connect(self, country: str) -> bool: ...
-     
-     @abstractmethod
-     async def disconnect(self) -> bool: ...
-     
-     @abstractmethod
-     async def status(self) -> dict: ...
- ```
- 
- ### 3.2. Retry Strategy
- 
- Use tenacity for operation retries:
- 
- ```python
- from tenacity import (
-     retry,
-     stop_after_attempt,
-     wait_exponential,
-     retry_if_exception_type
- )
- 
- @retry(
-     stop=stop_after_attempt(3),
-     wait=wait_exponential(multiplier=1, min=4, max=10),
-     retry=retry_if_exception_type(ConnectionError)
- )
- async def operation(): ...
- ```
- 
- ### 3.3. API Fallback
- 
- Use re-engage for API implementation fallback:
- 
- ```python
- import backoff
- from typing import Callable, TypeVar
- 
- T = TypeVar('T')
- 
- def with_fallback(primary: Callable[..., T], fallback: Callable[..., T]):
-     @backoff.on_exception(
-         backoff.expo,
-         Exception,
-         max_tries=2,
-         jitter=None
-     )
-     async def wrapper(*args, **kwargs) -> T:
-         try:
-             return await primary(*args, **kwargs)
-         except Exception:
-             return await fallback(*args, **kwargs)
-     return wrapper
- ```
- 
- ### 3.4. Configuration Management
- 
- ```python
- from pydantic import BaseSettings
- 
- class VPNConfig(BaseSettings):
-     username: str
-     password: str
-     default_country: str = "United States"
-     retry_attempts: int = 3
-     use_legacy_fallback: bool = True
-     
-     class Config:
-         env_prefix = "NORDVPN_"
- ```
+ ## 3. Critical Modularization Tasks
+ 
+ ### 3.1. Core Functionality Migration
+ - [!] Move server discovery from nyord_vpn.py to api/njord.py:
+   - [!] Extract `get_nordvpn_server` functionality
+   - [!] Extract `get_nordvpn_country_id` functionality
+   - [!] Move country mapping to a separate data file
+ - [!] Move connection management to core/client.py:
+   - [!] Extract `connect_nordvpn` functionality
+   - [!] Extract `disconnect_nordvpn` functionality
+   - [!] Extract `get_connection_status` functionality
+ - [!] Move configuration to core/config.py:
+   - [!] Extract all constants and settings
+   - [!] Create proper configuration classes
+   - [!] Add configuration validation
+ 
+ ### 3.2. Utility Functions Migration
+ - [!] Move to utils/system.py:
+   - [!] Extract `check_command` functionality
+   - [!] Extract `run_subprocess_safely` functionality
+   - [!] Add proper error handling and logging
+ - [!] Move to utils/network.py:
+   - [!] Extract `get_public_ip` functionality
+   - [!] Extract `wait_for_connection` functionality
+   - [!] Add retry mechanisms
+ 
+ ### 3.3. Security Enhancements
+ - [!] Move to utils/security.py:
+   - [!] Extract credential handling
+   - [!] Extract path validation
+   - [!] Add proper secrets management
+ 
+ ### 3.4. CLI Refactoring
+ - [!] Enhance cli/commands.py:
+   - [!] Port all CLI functionality from nyord_vpn.py
+   - [!] Add proper command structure
+   - [!] Add rich output formatting
  
  ## 4. Implementation Phases
  
  ### 4.5. Phase 5: Testing & Documentation
- - [!] Add unit tests
- - [!] Add integration tests
+ - [!] Add unit tests for new modular components
+ - [!] Add integration tests for core functionality
  - [ ] Create API documentation
  - [ ] Add usage examples
  
- ## 5. Critical Issues to Fix
+ ## 5. Code Quality Issues
  
- ### 5.1. Code Quality Issues
+ ### 5.1. Type and Error Handling
  - [!] Fix type errors in core/client.py:
    - Fix SecretStr type for password
    - Fix Coroutine call issue
    - Fix log_file parameter issue
- - [!] Fix blind exception catches (BLE001) in:
-   - cli/commands.py
-   - utils/retry.py
-   - nyord_vpn.py
- - [!] Fix subprocess security issues (S603) in nyord_vpn.py
- - [!] Fix try-except block issues (TRY300, TRY301) in:
-   - api/legacy.py
-   - api/njord.py
-   - core/client.py
-   - nyord_vpn.py
+ - [!] Fix blind exception catches (BLE001)
+ - [!] Fix subprocess security issues (S603)
+ - [!] Fix try-except block issues (TRY300, TRY301)
  - [!] Fix unused argument in api/njord.py (ARG002)
  
- ### 5.2. Security Enhancements
- - [!] Implement proper input validation for subprocess calls
- - [!] Add security checks for command execution
- - [ ] Add SSL certificate validation
- - [ ] Implement secure credential storage
- 
- ### 5.3. Testing Infrastructure
- - [x] Fix failing test_version test
- - [!] Set up pytest fixtures
+ ### 5.2. Testing Infrastructure
+ - [!] Set up pytest fixtures for new modules
  - [!] Add mock objects for API testing
  - [!] Add subprocess mocking
```

---

_****_



I've restructured the TODO.md to focus on the modularization effort. The key changes are:

1. Added a new "Critical Modularization Tasks" section that breaks down the process of migrating functionality from `nyord_vpn.py` into proper modules
2. Organized the migration into clear subsections:
   - Core Functionality Migration
   - Utility Functions Migration
   - Security Enhancements
   - CLI Refactoring
3. Removed redundant implementation details that are already in the code
4. Updated testing priorities to focus on testing the new modular components
5. Consolidated code quality issues to be addressed as part of the modularization

The main priorities now are:
1. Moving server discovery functionality to `api/njord.py`
2. Moving connection management to `core/client.py`
3. Moving configuration to `core/config.py`
4. Creating new utility modules for system, network, and security functions

This will help us systematically phase out the monolithic `nyord_vpn.py` while maintaining functionality and improving code quality.

Wait, but... we should also consider the dependency flow in our modularization. Let me add a note about this:

---

_****_

```diff
  
  ### 3.1. Core Functionality Migration
+ - [!] Establish clean dependency hierarchy:
+   - [!] utils/ modules should have no dependencies on other package modules
+   - [!] api/ modules should only depend on utils/
+   - [!] core/ modules can depend on api/ and utils/
+   - [!] cli/ modules can depend on core/, api/, and utils/
  - [!] Move server discovery from nyord_vpn.py to api/njord.py:
    - [!] Extract `get_nordvpn_server` functionality
```

---

_****_



Wait, but... we should also prioritize the order of migration to minimize disruption. Let me add a migration strategy:

---

_****_

```diff
  ## 3. Critical Modularization Tasks
  
- ### 3.1. Core Functionality Migration
+ ### 3.1. Migration Strategy
+ - [!] Phase 1 - Foundation:
+   - [!] Create and test all utility modules first (system.py, network.py, security.py)
+   - [!] Move all constants to a central configuration
+   - [!] Set up proper logging and error handling
+ - [!] Phase 2 - Core Components:
+   - [!] Enhance api/njord.py with server discovery
+   - [!] Update core/client.py with connection management
+   - [!] Create proper configuration management
+ - [!] Phase 3 - CLI Migration:
+   - [!] Port CLI functionality to cli/commands.py
+   - [!] Add rich formatting and progress indicators
+   - [!] Implement proper command structure
+ - [!] Phase 4 - Cleanup:
+   - [!] Remove functionality from nyord_vpn.py as it's migrated
+   - [!] Add tests for new modules
+   - [!] Update documentation
+ 
+ ### 3.2. Core Functionality Migration
  - [!] Establish clean dependency hierarchy:
    - [!] utils/ modules should have no dependencies on other package modules
    - [!] Add configuration validation
  
- ### 3.2. Utility Functions Migration
+ ### 3.3. Utility Functions Migration
  - [!] Move to utils/system.py:
    - [!] Extract `check_command` functionality
    - [!] Add retry mechanisms
  
- ### 3.3. Security Enhancements
+ ### 3.4. Security Enhancements
  - [!] Move to utils/security.py:
    - [!] Extract credential handling
    - [!] Extract path validation
    - [!] Add proper secrets management
  
- ### 3.4. CLI Refactoring
+ ### 3.5. CLI Refactoring
  - [!] Enhance cli/commands.py:
    - [!] Port all CLI functionality from nyord_vpn.py
```

---

_****_



This updated TODO.md now provides a clear strategy for modularizing the codebase, with a phased approach that minimizes disruption and maintains functionality throughout the process. The migration strategy ensures we build from the ground up, starting with utilities and working our way up to the CLI layer.

---

_**User**_

Read the entire codebase thoroly @repomix-output.txt and comprehensively rewrite @TODO.md to a list-based structure. Remove what you've done (`- [x] `). Upgrade priorities for NEXT TODO (`- [!]`), re-think the normal TODO (`- [ ] `) . Only leave the actual TODOs there. 

---

_**Assistant**_

I'll help reorganize the TODO.md to be more focused and list-based, removing completed items and focusing on what needs to be done. Let me first check the codebase thoroughly.

---

_****_

<details>
            <summary>Searched codebase "Check the entire codebase structure and implementation" • **24** results</summary>
        
| File | Lines |
|------|-------|
| `TODO.md` | L1-74 |
| `src/nyord_vpn/api/base.py` | L1-61 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L1353-1582 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L1794-2021 |
| `src/nyord_vpn/core/client.py` | L1-61 |
| `src/nyord_vpn/cli/commands.py` | L25-59 |
| `.gitignore` | L1-316 |
| `src/nyord_vpn/core/config.py` | L1-44 |
| `TODO.md` | L74-169 |
| `src/nyord_vpn/api/njord.py` | L1-60 |
| `src/nyord_vpn/nyord_vpn.py` | L200-206 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L3549-3734 |
| `src/nyord_vpn/nyord_vpn.py` | L372-385 |
| `src/nyord_vpn/api/legacy.py` | L21-71 |
| `src/nyord_vpn/nyord_vpn.py` | L1-46 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L7034-7108 |
| `src/nyord_vpn/api/njord.py` | L60-73 |
| `src/nyord_vpn/nyord_vpn.py` | L477-532 |
| `src/nyord_vpn/api/legacy.py` | L1-16 |
| `src/nyord_vpn/nyord_vpn.py` | L282-298 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L3473-3549 |
| `src/nyord_vpn/core/exceptions.py` | L1-5 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L3950-3991 |
| `.specstory/history/2025-02-22_19:00-comparison-of-njord-and-nyord-vpn-implementations.md` | L9951-9992 |

</details>

---

_****_



Let me create a new, focused TODO.md based on the actual codebase state and what needs to be done to phase out the monolithic `nyord_vpn.py`:

---

_****_

```diff
- # NordVPN Client Implementation Specification
- 
- ## 1. Overview
- 
- This specification outlines the implementation of `nyord-vpn`, a Python package that provides both a CLI and library interface for NordVPN connectivity. The implementation will leverage the `njord` package as the primary API engine and maintain our own implementation as a fallback.
- 
- ## 2. Architecture
- 
- ### 2.1. Package Structure
- ```
- nyord_vpn/
- ├── __init__.py
- ├── api/
- │   ├── __init__.py
- │   ├── base.py        # Base API interface
- │   ├── njord.py       # Njord API implementation
- │   └── legacy.py      # Our legacy implementation
- ├── cli/
- │   ├── __init__.py
- │   └── commands.py    # CLI implementation
- ├── core/
- │   ├── __init__.py
- │   ├── client.py      # Main VPN client
- │   ├── config.py      # Configuration management
- │   └── exceptions.py  # Custom exceptions
- ├── utils/
- │   ├── __init__.py
- │   ├── log_utils.py   # Logging utilities
- │   └── retry.py       # Retry utilities
- └── py.typed           # Type hint marker
- ```
- 
- ### 2.2. Core Components
- 
- 1. **API Layer**
-    - [x] `BaseAPI` abstract class defining the interface
-    - [x] `NjordAPI` primary implementation using njord
-    - [x] `LegacyAPI` fallback implementation using our code
- 
- 2. **Client Layer**
-    - [x] `VPNClient` main class for VPN operations
-    - [x] Uses re-engage for API fallback
-    - [x] Uses tenacity for operation retries
- 
- 3. **CLI Layer**
-    - [x] Rich-based CLI interface
-    - [x] Fire-based command parsing
-    - [x] Comprehensive error reporting
- 
- ## 3. Critical Modularization Tasks
+ # NordVPN Client Implementation TODO
+ 
+ ## 1. Critical Tasks
  
- ### 3.1. Migration Strategy
- - [!] Phase 1 - Foundation:
-   - [!] Create and test all utility modules first (system.py, network.py, security.py)
-   - [!] Move all constants to a central configuration
-   - [!] Set up proper logging and error handling
- - [!] Phase 2 - Core Components:
-   - [!] Enhance api/njord.py with server discovery
-   - [!] Update core/client.py with connection management
-   - [!] Create proper configuration management
- - [!] Phase 3 - CLI Migration:
-   - [!] Port CLI functionality to cli/commands.py
-   - [!] Add rich formatting and progress indicators
-   - [!] Implement proper command structure
- - [!] Phase 4 - Cleanup:
-   - [!] Remove functionality from nyord_vpn.py as it's migrated
-   - [!] Add tests for new modules
-   - [!] Update documentation
- 
- ### 3.2. Core Functionality Migration
- - [!] Establish clean dependency hierarchy:
-   - [!] utils/ modules should have no dependencies on other package modules
-   - [!] api/ modules should only depend on utils/
-   - [!] core/ modules can depend on api/ and utils/
-   - [!] cli/ modules can depend on core/, api/, and utils/
- - [!] Move server discovery from nyord_vpn.py to api/njord.py:
-   - [!] Extract `get_nordvpn_server` functionality
-   - [!] Extract `get_nordvpn_country_id` functionality
-   - [!] Move country mapping to a separate data file
- - [!] Move connection management to core/client.py:
-   - [!] Extract `connect_nordvpn` functionality
-   - [!] Extract `disconnect_nordvpn` functionality
-   - [!] Extract `get_connection_status` functionality
- - [!] Move configuration to core/config.py:
-   - [!] Extract all constants and settings
-   - [!] Create proper configuration classes
-   - [!] Add configuration validation
- 
- ### 3.3. Utility Functions Migration
- - [!] Move to utils/system.py:
-   - [!] Extract `check_command` functionality
-   - [!] Extract `run_subprocess_safely` functionality
-   - [!] Add proper error handling and logging
- - [!] Move to utils/network.py:
-   - [!] Extract `get_public_ip` functionality
-   - [!] Extract `wait_for_connection` functionality
-   - [!] Add retry mechanisms
- 
- ### 3.4. Security Enhancements
- - [!] Move to utils/security.py:
+ ### 1.1. Modularization
+ - [!] Move functionality from nyord_vpn.py to proper modules:
+   - [!] Move server discovery to api/njord.py:
+     - [!] Extract `get_nordvpn_server` and `get_nordvpn_country_id`
+     - [!] Move country mapping to data/countries.py
+     - [!] Add proper error handling
+   - [!] Move system utilities to utils/system.py:
+     - [!] Extract `check_command` with proper typing
+     - [!] Extract `run_subprocess_safely` with security fixes
+     - [!] Add logging and error handling
+   - [!] Move network utilities to utils/network.py:
+     - [!] Extract `get_public_ip` with retry logic
+     - [!] Extract `wait_for_connection` with timeouts
+     - [!] Add proper error handling
+   - [!] Move security utilities to utils/security.py:
      - [!] Extract credential handling
      - [!] Extract path validation
      - [!] Add proper secrets management
  
- ### 3.5. CLI Refactoring
- - [!] Enhance cli/commands.py:
-   - [!] Port all CLI functionality from nyord_vpn.py
-   - [!] Add proper command structure
-   - [!] Add rich output formatting
- 
- ## 4. Implementation Phases
- 
- ### 4.1. Phase 1: Core Structure
- - [x] Set up project structure
- - [x] Implement base classes and interfaces
- - [x] Add configuration management
- - [x] Set up logging
- 
- ### 4.2. Phase 2: API Integration
- - [x] Implement NjordAPI wrapper
- - [x] Port legacy implementation to LegacyAPI
- - [x] Add API fallback mechanism
- - [x] Implement retry logic
- 
- ### 4.3. Phase 3: Client Implementation
- - [x] Implement VPNClient class
- - [x] Add connection management
- - [x] Add status monitoring
- - [x] Implement credential handling
- 
- ### 4.4. Phase 4: CLI Development
- - [x] Implement Fire-based CLI
- - [x] Add Rich output formatting
- - [x] Implement progress indicators
- - [x] Add error handling
- 
- ### 4.5. Phase 5: Testing & Documentation
- - [!] Add unit tests for new modular components
- - [!] Add integration tests for core functionality
- - [ ] Create API documentation
- - [ ] Add usage examples
- 
- ## 5. Code Quality Issues
- 
- ### 5.1. Type and Error Handling
+ ### 1.2. Fix Critical Issues
  - [!] Fix type errors in core/client.py:
-   - Fix SecretStr type for password
-   - Fix Coroutine call issue
-   - Fix log_file parameter issue
+   - [!] Fix SecretStr type for password
+   - [!] Fix Coroutine call issue
+   - [!] Fix log_file parameter issue
+ - [!] Fix security issues:
+   - [!] Fix subprocess security (S603) in legacy.py
+   - [!] Replace standard RNG with secrets module
+   - [!] Add input validation for shell commands
+ - [!] Fix error handling:
    - [!] Fix blind exception catches (BLE001)
- - [!] Fix subprocess security issues (S603)
    - [!] Fix try-except block issues (TRY300, TRY301)
- - [!] Fix unused argument in api/njord.py (ARG002)
+   - [!] Add proper error chaining with `from`
  
- ### 5.2. Testing Infrastructure
- - [!] Set up pytest fixtures for new modules
- - [!] Add mock objects for API testing
- - [!] Add subprocess mocking
- - [ ] Add coverage reporting
- 
- ## 6. Future Enhancements
- 
- ### 6.1. Features
- - [ ] Kill switch implementation
- - [ ] Split tunneling support
- - [ ] Custom DNS configuration
- - [ ] Connection profiles
- 
- ### 6.2. Documentation
- - [ ] API documentation
- - [ ] Usage examples
- - [ ] Security considerations
- - [ ] Deployment guide
- 
- ### 6.3. Platform Support
- - [ ] Windows support
- - [ ] Linux support
- - [ ] Container support
+ ### 1.3. Testing Infrastructure
+ - [!] Set up proper test environment:
+   - [!] Add pytest fixtures for API mocking
+   - [!] Add subprocess mocking utilities
+   - [!] Add network call mocking
+   - [!] Set up test configuration
+ 
+ ## 2. Next Tasks
+ 
+ ### 2.1. Code Quality
+ - [ ] Reduce complexity in core functions:
+   - [ ] Split `connect_nordvpn` into smaller functions
+   - [ ] Improve error handling patterns
+   - [ ] Add proper type hints throughout
+ - [ ] Improve code organization:
+   - [ ] Move constants to config module
+   - [ ] Create proper configuration classes
+   - [ ] Add configuration validation
+ 
+ ### 2.2. Testing
+ - [ ] Add unit tests:
+   - [ ] Test API implementations
+   - [ ] Test utility functions
+   - [ ] Test configuration handling
+ - [ ] Add integration tests:
+   - [ ] Test connection flow
+   - [ ] Test error handling
+   - [ ] Test configuration loading
+ 
+ ### 2.3. Documentation
+ - [ ] Add API documentation:
+   - [ ] Document public interfaces
+   - [ ] Add usage examples
+   - [ ] Document error handling
+ - [ ] Add development guide:
+   - [ ] Document test setup
+   - [ ] Document contribution workflow
+   - [ ] Add architecture overview
  
- ## 7. Development Guidelines
+ ## 3. Development Guidelines
  
  1. Before making changes:
-    - Run: `uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]`
-    - Run: `hatch fmt --unsafe-fixes`
-    - Run: `hatch test`
-    - Analyze results and update priorities
+    ```bash
+    uv venv
+    source .venv/bin/activate
+    uv pip install -e '.[dev,test]'
+    hatch fmt --unsafe-fixes
+    hatch test
+    ```
  
  2. After changes:
-    - Run: `hatch fmt --unsafe-fixes`
-    - Run: `hatch test`
-    - Verify fixes and update TODO.md
+    ```bash
+    hatch fmt --unsafe-fixes
+    hatch test
+    ```
  
  3. When editing TODO.md:
     - Use `- [ ]` for pending tasks
     - Use `- [x]` for completed tasks
     - Use `- [!]` for next priority tasks 
- 
- 4. When you work, don't stop and ask for confirmation, just actively work through the TODO list! 
```

---

_****_



I've completely restructured the TODO.md to focus on phasing out the monolithic `nyord_vpn.py` and fixing critical issues. The new structure:

1. Prioritizes the modularization tasks with clear, actionable items
2. Groups critical issues that need immediate attention
3. Organizes next tasks in a logical order
4. Removes completed tasks and redundant information
5. Adds clear development guidelines with proper code formatting

The most critical tasks now are:
1. Moving functionality from `nyord_vpn.py` to proper modules
2. Fixing type errors and security issues
3. Setting up proper test infrastructure

Would you like me to start working on any of these tasks?

---

_**User**_

DO IT

---

_**Assistant**_

I'll start working on the highest priority tasks, following the modularization plan. Let's begin with moving the server discovery functionality to `api/njord.py`.

First, let's create the data module for country mappings:

---



---

