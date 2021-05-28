from backend.Constants import BaseConstants


def test_simple() -> None:
    """Simple test. Checking pytest."""
    print('Simple test to check pytest.')
    try:
        import backend
    except ImportError:
        raise AssertionError
    else:
        assert backend


def test_constants() -> None:
    """Testing constants."""
    assert BaseConstants.test_constant is not None
