# custom
from answers.database import rows_to_list_of_dicts as correct_rows

# 3rd party
import pandas as pd
import numpy as np

# to test
import app.analysis as analysis

def test_standard_deviation():
    rows = correct_rows()
    df = pd.json_normalize(rows)
    expected = df["income"].std()
    actual = analysis.standard_deviation("income")
    assert actual == expected, f'Standard devation of "income" should be {expected}, recieved {actual}'


def test_variance():
    rows = correct_rows()
    ages = [row["age"] for row in rows]
    expected = np.var(ages)
    actual = analysis.variance("age")
    assert actual == expected, f'Variance of "age" should be {expected}, recieved {actual}'