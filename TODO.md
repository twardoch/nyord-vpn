# NordVPN Client Implementation Specification




## 1. Overview

This specification outlines the implementation of `nyord-vpn`, a Python package that provides both a CLI and library interface for NordVPN connectivity. The implementation will leverage the `njord` package as the primary API engine and maintain our own implementation as a fallback.

## 2. Architecture

### 2.1. Package Structure
```
nyord_vpn/
├── __init__.py
├── api/
│   ├── __init__.py
│   ├── base.py        # Base API interface
│   ├── njord.py       # Njord API implementation
│   └── legacy.py      # Our legacy implementation
├── cli/
│   ├── __init__.py
│   └── commands.py    # CLI implementation
├── core/
│   ├── __init__.py
│   ├── client.py      # Main VPN client
│   ├── config.py      # Configuration management
│   └── exceptions.py  # Custom exceptions
├── utils/
│   ├── __init__.py
│   ├── logging.py     # Logging utilities
│   └── retry.py       # Retry utilities
└── py.typed           # Type hint marker
```

### 2.2. Core Components

1. **API Layer**
   - `BaseAPI` abstract class defining the interface
   - `NjordAPI` primary implementation using njord
   - `LegacyAPI` fallback implementation using our code

2. **Client Layer**
   - `VPNClient` main class for VPN operations
   - Uses re-engage for API fallback
   - Uses tenacity for operation retries

3. **CLI Layer**
   - Rich-based CLI interface
   - Fire-based command parsing
   - Comprehensive error reporting

## 3. Implementation Details

### 3.1. API Layer

```python
class BaseAPI(ABC):
    @abstractmethod
    async def connect(self, country: str) -> bool: ...
    
    @abstractmethod
    async def disconnect(self) -> bool: ...
    
    @abstractmethod
    async def status(self) -> dict: ...
```

### 3.2. Retry Strategy

Use tenacity for operation retries:

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(ConnectionError)
)
async def operation(): ...
```

### 3.3. API Fallback

Use re-engage for API implementation fallback:

```python
import backoff
from typing import Callable, TypeVar

T = TypeVar('T')

def with_fallback(primary: Callable[..., T], fallback: Callable[..., T]):
    @backoff.on_exception(
        backoff.expo,
        Exception,
        max_tries=2,
        jitter=None
    )
    async def wrapper(*args, **kwargs) -> T:
        try:
            return await primary(*args, **kwargs)
        except Exception:
            return await fallback(*args, **kwargs)
    return wrapper
```

### 3.4. Configuration Management

```python
from pydantic import BaseSettings

class VPNConfig(BaseSettings):
    username: str
    password: str
    default_country: str = "United States"
    retry_attempts: int = 3
    use_legacy_fallback: bool = True
    
    class Config:
        env_prefix = "NORDVPN_"
```

## 4. Implementation Phases

### 4.1. Phase 1: Core Structure
- [x] Set up project structure
- [x] Implement base classes and interfaces
- [x] Add configuration management
- [x] Set up logging

### 4.2. Phase 2: API Integration
- [x] Implement NjordAPI wrapper
- [x] Port legacy implementation to LegacyAPI
- [x] Add API fallback mechanism
- [x] Implement retry logic

### 4.3. Phase 3: Client Implementation
- [x] Implement VPNClient class
- [x] Add connection management
- [x] Add status monitoring
- [x] Implement credential handling

### 4.4. Phase 4: CLI Development
- [x] Implement Fire-based CLI
- [x] Add Rich output formatting
- [x] Implement progress indicators
- [x] Add error handling

### 4.5. Phase 5: Testing & Documentation
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Create API documentation
- [ ] Add usage examples

## 5. Usage Examples

### 5.1. As a Library

```python
from nyord_vpn import VPNClient

async with VPNClient() as vpn:
    await vpn.connect("United States")
    status = await vpn.status()
    print(f"Connected: {status['connected']}")
```

### 5.2. CLI Usage

```bash
# Connect to VPN
nyord-vpn connect us

# Check status
nyord-vpn status

# Disconnect
nyord-vpn disconnect
```

## 6. Error Handling

1. **API Errors**
   - Wrap njord exceptions
   - Provide fallback mechanisms
   - Clear error messages

2. **Connection Errors**
   - Automatic retries with tenacity
   - Fallback to legacy implementation
   - Detailed error reporting

3. **Configuration Errors**
   - Validation using Pydantic
   - Clear error messages
   - Configuration file validation

## 7. Security Considerations

1. **Credential Management**
   - Use keyring for credential storage
   - Support environment variables
   - Secure credential file handling

2. **Certificate Handling**
   - Proper certificate validation
   - Secure storage
   - Regular updates

## 8. Performance Considerations

1. **Connection Management**
   - Efficient connection pooling
   - Quick fallback mechanisms
   - Connection caching

2. **Resource Usage**
   - Minimal memory footprint
   - Efficient process management
   - Resource cleanup

## 9. Monitoring and Logging

1. **Logging System**
   - Structured logging
   - Log rotation
   - Debug information

2. **Metrics**
   - Connection statistics
   - Error rates
   - Performance metrics

## 10. Future Enhancements

1. **Additional Features**
   - Kill switch implementation
   - Split tunneling
   - Custom DNS support

2. **Platform Support**
   - Windows support
   - Linux support
   - Container support

## 11. Dependencies

Required packages:
```toml
[tool.poetry.dependencies]
python = "^3.9"
njord = "*"
tenacity = "*"
re-engage = "*"
rich = "*"
fire = "*"
pydantic = "*"
keyring = "*"
```

## 12. Development Guidelines

1. **Code Style**
   - Follow PEP 8
   - Use type hints
   - Document all public APIs

2. **Testing**
   - 100% test coverage
   - Integration tests
   - Property-based testing

3. **Documentation**
   - API documentation
   - Usage examples
   - Architecture documentation

## 13. Immediate Priorities

- [!] **Fix Critical Code Issues**
  - *High Priority Fixes*:
    - [!] Fix decorator issues with `with_retry` (failing tests)
    - [!] Fix async HTTP in legacy API (use aiohttp instead of requests)
    - [!] Fix async subprocess in legacy API (use asyncio.create_subprocess_exec)
    - [!] Fix complex functions (C901)
    - [!] Fix exception handling patterns (B904)

- [!] **Fix Test Infrastructure**
  - *Critical Setup*:
    - [!] Fix failing test_version test
    - [!] Add proper test dependencies
    - [!] Set up test configuration
    - [!] Add test fixtures and mocks

- [!] **Security Enhancements**
  - *Critical Security*:
    - [x] Add input validation for shell commands (using shlex.quote)
    - [x] Implement proper subprocess security (using list args)
    - [x] Fix shell injection vulnerabilities (S605)
    - [!] Replace standard RNG with cryptographic RNG (S311)

## 14. Near-term Tasks

- [ ] **Code Quality**
  - *Refactoring*:
    - [ ] Split complex functions (PLR0912, PLR0915)
    - [ ] Fix blind exception catches (BLE001)
    - [ ] Fix boolean argument issues (FBT001, FBT002)
    - [ ] Fix module imports and organization (E402)

- [ ] **Improve Test Coverage**
  - *Critical Modules*:
    - [ ] Write tests for `api/legacy.py` (subprocess mocking)
    - [ ] Write tests for `api/njord.py` (API mocking)
    - [ ] Write tests for `core/client.py` (integration tests)
    - [ ] Write tests for `core/config.py` (configuration tests)

## 15. Future Tasks

- [ ] **Documentation**
  - *Documentation Updates*:
    - [ ] Add API documentation
    - [ ] Add usage examples
    - [ ] Add security considerations
    - [ ] Add deployment guide

- [ ] **Additional Features**
  - *Enhancements*:
    - [ ] Kill switch implementation
    - [ ] Split tunneling
    - [ ] Custom DNS support
    - [ ] Connection profiles

## 16. Development Guidelines

1. Before making changes:
   - Run: `uv venv; source .venv/bin/activate; uv pip install -e .[dev,test]`
   - Run: `hatch fmt --unsafe-fixes`
   - Run: `hatch test`
   - Analyze results and update priorities

2. After changes:
   - Run: `hatch fmt --unsafe-fixes`
   - Run: `hatch test`
   - Verify fixes and update TODO.md

3. When editing TODO.md:
   - Use `- [ ]` for pending tasks
   - Use `- [x]` for completed tasks
   - Use `- [!]` for next priority tasks

4. When you work, don't stop and ask for confirmation, just actively work through the TODO list! 