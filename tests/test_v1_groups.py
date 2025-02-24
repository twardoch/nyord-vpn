"""Tests for the NordVPN v1 groups API module.

this_file: tests/test_v1_groups.py

This module contains tests for the v1_groups module, which provides
access to server group information from the NordVPN v1 API.
"""

import pytest
from unittest.mock import MagicMock, patch

from nyord_vpn.api.v1_groups import (
    NordVPNGroupsV1,
    get_groups_by_type,
    get_group_by_identifier,
)


@pytest.fixture
def sample_group_type() -> dict:
    """Create a sample group type for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "title": "Legacy Groups",
        "identifier": "legacy_group_category",
    }


@pytest.fixture
def sample_group(sample_group_type) -> dict:
    """Create a sample group for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "title": "P2P",
        "identifier": "legacy_p2p",
        "type": sample_group_type,
    }


@pytest.fixture
def sample_groups(sample_group) -> list[dict]:
    """Create a list of sample groups for testing."""
    return [
        sample_group,
        {
            "id": 2,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
            "title": "Standard VPN",
            "identifier": "legacy_standard",
            "type": sample_group_type,
        },
        {
            "id": 3,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
            "title": "Europe",
            "identifier": "europe",
            "type": {
                "id": 2,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "title": "Regions",
                "identifier": "regions",
            },
        },
    ]


def test_fetch_groups(sample_groups) -> None:
    """Test fetching server groups from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_groups
        mock_get.return_value = mock_response

        client = NordVPNGroupsV1()
        groups = client.fetch_groups()

        assert len(groups) == 3
        assert groups[0].title == "P2P"
        assert groups[0].identifier == "legacy_p2p"
        assert groups[0].type.identifier == "legacy_group_category"
        assert groups[2].title == "Europe"
        assert groups[2].type.identifier == "regions"


def test_get_groups_by_type(sample_groups) -> None:
    """Test filtering groups by type identifier."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_groups
        mock_get.return_value = mock_response

        client = NordVPNGroupsV1()
        groups = client.fetch_groups()

        # Test finding legacy groups
        legacy_groups = get_groups_by_type(groups, "legacy_group_category")
        assert len(legacy_groups) == 2
        assert all(
            group.type.identifier == "legacy_group_category" for group in legacy_groups
        )
        assert {group.identifier for group in legacy_groups} == {
            "legacy_p2p",
            "legacy_standard",
        }

        # Test finding region groups
        region_groups = get_groups_by_type(groups, "regions")
        assert len(region_groups) == 1
        assert region_groups[0].identifier == "europe"

        # Test non-existent type
        unknown_groups = get_groups_by_type(groups, "unknown")
        assert len(unknown_groups) == 0


def test_get_group_by_identifier(sample_groups) -> None:
    """Test finding a group by its identifier."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_groups
        mock_get.return_value = mock_response

        client = NordVPNGroupsV1()
        groups = client.fetch_groups()

        # Test finding existing group
        p2p = get_group_by_identifier(groups, "legacy_p2p")
        assert p2p.title == "P2P"
        assert p2p.type.identifier == "legacy_group_category"

        # Test finding region group
        europe = get_group_by_identifier(groups, "europe")
        assert europe.title == "Europe"
        assert europe.type.identifier == "regions"

        # Test non-existent group
        with pytest.raises(ValueError):
            get_group_by_identifier(groups, "unknown")
