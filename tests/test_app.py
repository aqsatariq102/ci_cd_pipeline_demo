def test_basic():
    assert 2 + 2 == 4


def test_dash_server():
    from app import app
    assert app is not None
    assert app.server is not None
