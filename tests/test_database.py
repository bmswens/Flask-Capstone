# built in
import statistics

# to test
from app.database import Database
import app.database as database


def test_rows_to_list_of_dicts():
    rows = database.rows_to_dict()
    expected ={ 
        "id": int,
        "first_name": str,
        "last_name": str,
        "age": int,
        "gender": str,
        "income": int,
        "job_title": str
    }
    for row in rows:
        for expected_type, column in expected:
            assert type(row.get(column)) == expected_type

def test_get_incomes():
    with Database("db.sqlite3") as db:
        incomes = db.query("SELECT income FROM people")
        expected_average = statistics.mean(incomes)
    average_income = database.get_average_income()
    assert average_income == expected_average


def test_get_clean_column_names():
    expected_columns = [
        "Id"
        "First Name",
        "Last Name",
        "Age",
        "Gender",
        "Income",
        "Job Title"
    ]
    column_names = database.get_clean_column_names()
    assert column_names == expected_columns


def test_get_gender_counts():
    with Database("db.sqlite3") as db:
        genders = db.query("SELECT gender FROM people")
        male_count = genders.count("male")
        female_count = genders.count("female")
    gender_counts = database.get_gender_counts()
    assert gender_counts["male"] == male_count
    assert gender_counts["female"] == female_count