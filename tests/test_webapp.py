# built-in
from random import randint

# pytest
import pytest

# the app
from app.webapp import app

# help
from answers.database import rows_to_list_of_dicts as correct_rows

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_by_id(client):
    selected = randint(1, 100)
    rows = correct_rows()
    expected = rows[selected - 1]
    response = client.get(f"/api/people/{selected}")
    actual = response.get_json()
    assert actual == expected
