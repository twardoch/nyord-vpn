"""Test suite for nyord_vpn."""


def test_version() -> None:
    """Verify package exposes version."""
    import nyord_vpn

    assert nyord_vpn.__version__
