# built in
import statistics

# to test
from app.database import Database
import app.database as database


def test_rows_to_list_of_dicts():
    rows = database.rows_to_list_of_dicts()
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
        for column in expected:
            expected_type = expected[column]
            t = type(row.get(column))
            assert t == expected_type, f'Column {column} should be type {expected_type} but was type {t}'

def test_get_incomes():
    rows = database.rows_to_list_of_dicts()
    incomes = [row["income"] for row in rows]
    expected_average = statistics.mean(incomes)
    average_income = database.get_average_income()
    assert average_income == expected_average, f'Expected average of {expected_average} but got {average_income}'


def test_get_clean_column_names():
    expected_columns = [
        "Id",
        "First Name",
        "Last Name",
        "Age",
        "Gender",
        "Income",
        "Job Title"
    ]
    column_names = database.get_clean_column_names()
    assert column_names == expected_columns


def test_get_gender_count():
    with Database("db.sqlite3") as db:
        response = db.query("SELECT gender FROM people WHERE gender = 'female'")
        female_count = len(response)
    count = database.get_gender_count("female")
    assert count == female_count