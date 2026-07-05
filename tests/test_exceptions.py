"""Tests for the exception hierarchies in nyord_vpn.exceptions and nyord_vpn.storage.models.

this_file: tests/test_exceptions.py

These are pure object-construction tests: no I/O, no network, no subprocess.
"""

from nyord_vpn import exceptions as exc
from nyord_vpn.storage import models


def test_nyord_vpn_error_default_message() -> None:
    """Base error falls back to a generic message when none is given."""
    err = exc.NyordVPNError()
    assert "error occurred" in str(err).lower()


def test_nyord_vpn_error_formats_details_and_cause() -> None:
    """Details and cause are appended to the formatted message."""
    cause = ValueError("root cause")
    err = exc.NyordVPNError("Something broke", details="extra info", cause=cause)
    text = str(err)
    assert "Something broke" in text
    assert "extra info" in text
    assert "root cause" in text
    assert err.message == "Something broke"
    assert err.details == "extra info"
    assert err.cause is cause


def test_nyord_vpn_error_without_details_or_cause() -> None:
    """No Details:/Cause: sections are added when neither is provided."""
    err = exc.NyordVPNError("Plain message")
    text = str(err)
    assert text == "Plain message"
    assert "Details:" not in text
    assert "Cause:" not in text


def test_exceptions_hierarchy() -> None:
    """Each specific exception subclasses the expected base."""
    assert issubclass(exc.VPNError, exc.NyordVPNError)
    assert issubclass(exc.VPNConfigError, exc.VPNError)
    assert issubclass(exc.VPNAuthenticationError, exc.VPNError)
    assert issubclass(exc.VPNProcessError, exc.VPNError)
    assert issubclass(exc.VPNConnectionError, exc.VPNError)
    assert issubclass(exc.VPNDisconnectionError, exc.VPNError)
    assert issubclass(exc.VPNAPIError, exc.VPNError)
    assert issubclass(exc.CredentialsError, exc.NyordVPNError)
    assert issubclass(exc.ServerNotFoundError, exc.NyordVPNError)
    assert issubclass(exc.VPNServerError, exc.NyordVPNError)
    assert issubclass(exc.VPNTimeoutError, exc.NyordVPNError)


def test_exceptions_default_messages_are_non_empty() -> None:
    """Every exception class provides a sensible default message."""
    classes = [
        exc.NyordVPNError,
        exc.VPNError,
        exc.CredentialsError,
        exc.ServerNotFoundError,
        exc.VPNConfigError,
        exc.VPNServerError,
        exc.VPNAuthenticationError,
        exc.VPNTimeoutError,
        exc.VPNProcessError,
        exc.VPNConnectionError,
        exc.VPNDisconnectionError,
        exc.VPNAPIError,
    ]
    for cls in classes:
        instance = cls()
        assert str(instance)


def test_exceptions_accept_custom_message() -> None:
    """A custom message overrides the default for each exception type."""
    err = exc.VPNConnectionError("custom failure")
    assert "custom failure" in str(err)


def test_storage_models_vpn_error_default() -> None:
    """storage.models.VPNError has its own independent default message."""
    err = models.VPNError()
    assert "unknown vpn error" in str(err).lower()


def test_storage_models_vpn_error_custom_message() -> None:
    """Custom messages are preserved as-is."""
    err = models.VPNError("custom")
    assert str(err) == "custom"


def test_storage_models_server_error_default_message() -> None:
    """ServerError defaults to actionable guidance."""
    err = models.ServerError()
    assert "select a server" in str(err).lower()


def test_storage_models_authentication_error_default_message() -> None:
    """AuthenticationError points users at their credentials."""
    err = models.AuthenticationError()
    assert "credentials" in str(err).lower()


def test_storage_models_credentials_error_default_message() -> None:
    """CredentialsError includes the environment-variable setup instructions."""
    err = models.CredentialsError()
    text = str(err)
    assert "NORD_USER" in text
    assert "NORD_PASSWORD" in text


def test_storage_models_state_error_default_message() -> None:
    """StateError suggests disconnect/reconnect recovery."""
    err = models.StateError()
    assert "disconnecting and reconnecting" in str(err).lower()


def test_storage_models_cache_error_default_message() -> None:
    """CacheError suggests a cache refresh."""
    err = models.CacheError()
    assert "cache" in str(err).lower()


def test_storage_models_hierarchy() -> None:
    """All storage.models errors subclass the local VPNError."""
    assert issubclass(models.ServerError, models.VPNError)
    assert issubclass(models.AuthenticationError, models.VPNError)
    assert issubclass(models.CredentialsError, models.VPNError)
    assert issubclass(models.StateError, models.VPNError)
    assert issubclass(models.CacheError, models.VPNError)
