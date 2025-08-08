import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_basic():
    assert 2 + 2 == 4


def test_dash_server():
    from app import app
    assert app is not None
    assert app.server is not None
