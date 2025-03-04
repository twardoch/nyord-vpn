"""Tests for the NordVPN v1 technologies API module.

this_file: tests/test_v1_technologies.py

This module contains tests for the v1_technologies module, which provides
access to server technology information from the NordVPN v1 API.
"""

from unittest.mock import MagicMock, patch

import pytest

from nyord_vpn.api.v1_technologies import (NordVPNTechnologiesV1,
                                           get_technology_by_identifier)


@pytest.fixture
def sample_technology() -> dict:
    """Create a sample technology for testing."""
    return {
        "id": 1,
        "name": "OpenVPN UDP",
        "identifier": "openvpn_udp",
        "internal_identifier": "openvpn_udp_1194",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def sample_technologies(sample_technology) -> list[dict]:
    """Create a list of sample technologies for testing."""
    return [
        sample_technology,
        {
            "id": 2,
            "name": "OpenVPN TCP",
            "identifier": "openvpn_tcp",
            "internal_identifier": "openvpn_tcp_443",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        },
        {
            "id": 3,
            "name": "IKEv2/IPSec",
            "identifier": "ikev2",
            "internal_identifier": "ikev2_default",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        },
    ]


def test_fetch_technologies(sample_technologies) -> None:
    """Test fetching server technologies from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_technologies
        mock_get.return_value = mock_response

        client = NordVPNTechnologiesV1()
        technologies = client.fetch_technologies()

        assert len(technologies) == 3
        assert technologies[0].name == "OpenVPN UDP"
        assert technologies[0].identifier == "openvpn_udp"
        assert technologies[0].internal_identifier == "openvpn_udp_1194"
        assert technologies[2].name == "IKEv2/IPSec"
        assert technologies[2].identifier == "ikev2"
        assert technologies[2].internal_identifier == "ikev2_default"


def test_get_technology_by_identifier(sample_technologies) -> None:
    """Test finding a technology by its identifier."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_technologies
        mock_get.return_value = mock_response

        client = NordVPNTechnologiesV1()
        technologies = client.fetch_technologies()

        # Test finding existing technology
        udp = get_technology_by_identifier(technologies, "openvpn_udp")
        assert udp.name == "OpenVPN UDP"
        assert udp.internal_identifier == "openvpn_udp_1194"

        # Test finding IKEv2 technology
        ikev2 = get_technology_by_identifier(technologies, "ikev2")
        assert ikev2.name == "IKEv2/IPSec"
        assert ikev2.internal_identifier == "ikev2_default"

        # Test non-existent technology
        with pytest.raises(ValueError):
            get_technology_by_identifier(technologies, "unknown")
