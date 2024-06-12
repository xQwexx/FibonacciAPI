import json
from pathlib import Path

import pytest

from api import create_app, db

app = create_app()
TEST_DB = "test.db"


@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    app.config["DATABASE"] = BASE_DIR.joinpath(TEST_DB)

    with app.app_context():
        db.init_db()
        # db.get_db().create_all()  # setup
        yield app.test_client()  # tests run here
        #db.get_db().drop_all()  # teardown


def test_fibonacciIndex(client):
    """Fibonacci Index function"""
    fib = client.get(
        "/fibonacci/1",
        data='',
        follow_redirects=True,
    )
    assert b'{"index":"1","value":"1"}\n' in fib.data


def test_fibonacciList(client):
    """Fibonacci List Index function"""
    fib = client.get(
        "/fibonacci/list/1",
        data='',
        follow_redirects=True,
    )
    assert b'[{"index":"0","value":"0"},{"index":"1","value":"1"}]\n' in fib.data


def test_home(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 404


def test_database(client):
    """initial test. ensure that the database exists"""
    tester = Path("test.db").is_file()
    assert tester

