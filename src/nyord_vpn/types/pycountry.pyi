"""Type stubs for pycountry module."""

from typing import Any, Protocol, TypeVar, overload

class Country(Protocol):
    """Protocol for country objects."""

    @property
    def alpha_2(self) -> str:
        """ISO 3166-1 alpha-2 code."""
        ...

    @property
    def alpha_3(self) -> str:
        """ISO 3166-1 alpha-3 code."""
        ...

    @property
    def name(self) -> str:
        """Country name."""
        ...

    @property
    def numeric(self) -> str:
        """ISO 3166-1 numeric code."""
        ...

class Database(Protocol):
    """Protocol for pycountry database."""

    @overload
    def get(self, alpha_2: str) -> Country | None:
        """Get country by alpha-2 code."""
        ...

    @overload
    def get(self, alpha_3: str) -> Country | None:
        """Get country by alpha-3 code."""
        ...

    @overload
    def get(self, numeric: str) -> Country | None:
        """Get country by numeric code."""
        ...

    @overload
    def get(self, name: str) -> Country | None:
        """Get country by name."""
        ...

    def search_fuzzy(self, query: str) -> list[Country]:
        """Search countries by fuzzy matching."""
        ...

# Type variable for database types
_DB = TypeVar("_DB", bound=Database)

# Module level variables
countries: Database
