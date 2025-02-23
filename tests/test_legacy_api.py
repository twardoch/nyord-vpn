"""Tests for LegacyVPNClient implementation."""

import pytest
import requests
import os

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.api.legacy import LegacyVPNClient


def test_init(mock_env_credentials):
    """Test LegacyVPNClient initialization."""
    api = LegacyVPNClient()
    assert api.username == os.getenv("NORD_USER")
    assert isinstance(api.password, str)
    assert api.password == os.getenv("NORD_PASSWORD")


def test_connect_success(mock_subprocess):
    """Test successful connection."""
    api = LegacyVPNClient()
    assert api.connect() is True


def test_connect_failure(mock_subprocess):
    """Test connection failure."""
    mock_subprocess.side_effect = requests.RequestException("Failed to connect")
    api = LegacyVPNClient()
    with pytest.raises(VPNError, match="Failed to connect"):
        api.connect()


def test_disconnect_success(mock_subprocess):
    """Test successful disconnection."""
    api = LegacyVPNClient()
    assert api.disconnect() is True


def test_status_connected(mock_subprocess):
    """Test status when connected."""
    api = LegacyVPNClient()
    status = api.status()
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"


def test_list_countries():
    """Test listing available countries."""
    api = LegacyVPNClient()
    countries = api.list_countries()
    assert len(countries) > 0
    assert all(isinstance(c, dict) for c in countries)
    assert all("name" in c and "code" in c for c in countries)
