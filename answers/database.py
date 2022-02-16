# built in
import sqlite3
import os
import random
import statistics

# 3rd party
from faker import Faker
fake = Faker()


class Database:
    def __init__(self, path):
        # path to file
        self.path = path

        # whether we're connected or not
        self.connection = None
        self.cursor = None

        # create the database if none exists
        if not os.path.exists(self.path):
            self.create_database()

    def __enter__(self):
        """
        Enables the "with X as Y:" syntax
        """
        if not self.connection:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Defines what to do when "with X as Y:" closes
        """
        if not self.connection:
            return
        else:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None

    def query(self, query_string):
        self.cursor.execute(query_string)
        return self.cursor.fetchall()

    def create_database(self):
        self.__enter__()
        table_creation = """
        CREATE TABLE people
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT CHECK( gender IN ('male', 'female')) NOT NULL,
            income INTEGER NOT NULL,
            job_title TEXT NOT NULL
        );
        """
        self.cursor.execute(table_creation)
        for _ in range(150):
            name = fake.name().split(' ')
            first_name = name[0]
            last_name = name[1] or 'Smith'
            age = random.randint(18, 99)
            gender = random.choice(["male", "female"])
            income = random.randint(20000, 120000)
            job_title = random.choice(
                ["chef", "designer", "merchant", "programmer"]
                )
            row_creation = f"""
            INSERT INTO people
            (
                first_name,
                last_name,
                age,
                gender,
                income,
                job_title
            )
            VALUES
            (
                '{first_name}',
                '{last_name}',
                {age},
                '{gender}',
                {income},
                '{job_title}'
            );
            """
            self.cursor.execute(row_creation)
        self.__exit__(None, None, None)


def rows_to_list_of_dicts():
    output = []
    columns = [
        "id",
        "first_name",
        "last_name",
        "age",
        "gender",
        "income",
        "job_title"
    ]
    with Database("db.sqlite3") as db:
        rows = db.query('SELECT * FROM people')
    for row in rows:
        output_row = {}
        for index, column in enumerate(columns):
            output_row[column] = row[index]
        output.append(output_row)
    return output


def get_average_income():
    rows = rows_to_list_of_dicts()
    incomes = [row["income"] for row in rows]
    return statistics.mean(incomes)


def get_clean_column_names():
    output = []
    with Database("db.sqlite3") as db:
        columns = db.query("PRAGMA table_info(people);")
    for column in columns:
        column = column[1].replace('_', ' ').title()
        output.append(column)
    return output


def get_gender_count(gender):
    output = 0
    rows = rows_to_list_of_dicts()
    for row in rows:
        if row["gender"] == gender:
            output += 1
    return output
