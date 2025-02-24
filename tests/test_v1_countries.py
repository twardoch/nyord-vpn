"""Tests for the NordVPN v1 countries API module.

this_file: tests/test_v1_countries.py

This module contains tests for the v1_countries module, which provides
access to country and server location information from the NordVPN v1 API.
"""

import pytest
from unittest.mock import MagicMock, patch

from nyord_vpn.api.v1_countries import (
    NordVPNCountriesV1,
    get_country_by_code,
    get_countries_by_min_servers,
    get_city_by_name,
    Country,
)


@pytest.fixture
def sample_city() -> dict:
    """Create a sample city for testing."""
    return {
        "id": 1,
        "name": "New York",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "dns_name": "new-york",
        "hub_score": 100,
        "server_count": 50,
    }


@pytest.fixture
def sample_country(sample_city) -> dict:
    """Create a sample country for testing."""
    return {
        "id": 1,
        "name": "United States",
        "code": "US",
        "server_count": 100,
        "cities": [sample_city],
    }


@pytest.fixture
def sample_countries(sample_country) -> list[dict]:
    """Create a list of sample countries for testing."""
    return [
        sample_country,
        {
            "id": 2,
            "name": "Germany",
            "code": "DE",
            "server_count": 80,
            "cities": [
                {
                    "id": 2,
                    "name": "Frankfurt",
                    "latitude": 50.1109,
                    "longitude": 8.6821,
                    "dns_name": "frankfurt",
                    "hub_score": 90,
                    "server_count": 40,
                }
            ],
        },
    ]


def test_fetch_countries(sample_countries) -> None:
    """Test fetching countries from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_countries
        mock_get.return_value = mock_response

        client = NordVPNCountriesV1()
        countries = client.fetch_countries()

        assert len(countries) == 2
        assert countries[0].name == "United States"
        assert countries[0].code == "US"
        assert countries[0].server_count == 100
        assert len(countries[0].cities) == 1
        assert countries[0].cities[0].name == "New York"


def test_get_country_by_code(sample_countries) -> None:
    """Test finding a country by its code."""
    countries = [Country.model_validate(c) for c in sample_countries]

    # Test finding existing country
    us = get_country_by_code(countries, "US")
    assert us.name == "United States"
    assert us.code == "US"

    # Test case insensitivity
    de = get_country_by_code(countries, "de")
    assert de.name == "Germany"
    assert de.code == "DE"

    # Test non-existent country
    with pytest.raises(ValueError):
        get_country_by_code(countries, "XX")


def test_get_countries_by_min_servers(sample_countries) -> None:
    """Test filtering countries by minimum server count."""
    countries = [Country.model_validate(c) for c in sample_countries]

    # Test finding countries with at least 90 servers
    large_countries = get_countries_by_min_servers(countries, 90)
    assert len(large_countries) == 1
    assert large_countries[0].name == "United States"

    # Test finding countries with at least 70 servers
    medium_countries = get_countries_by_min_servers(countries, 70)
    assert len(medium_countries) == 2

    # Test finding countries with at least 200 servers (none)
    no_countries = get_countries_by_min_servers(countries, 200)
    assert len(no_countries) == 0


def test_get_city_by_name(sample_countries) -> None:
    """Test finding a city by name within a country."""
    us = Country.model_validate(sample_countries[0])
    de = Country.model_validate(sample_countries[1])

    # Test finding existing city
    nyc = get_city_by_name(us, "New York")
    assert nyc.name == "New York"
    assert nyc.dns_name == "new-york"

    frankfurt = get_city_by_name(de, "Frankfurt")
    assert frankfurt.name == "Frankfurt"
    assert frankfurt.dns_name == "frankfurt"

    # Test case insensitivity
    nyc_lower = get_city_by_name(us, "new york")
    assert nyc_lower.name == "New York"

    # Test non-existent city
    with pytest.raises(ValueError):
        get_city_by_name(us, "Chicago")
