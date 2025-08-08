import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_basic():
    # nosec B101
    assert 2 + 2 == 4

def test_app_import():
    from app import app
    # nosec B101
    assert app is not None
    # nosec B101
    assert app.server is not None
