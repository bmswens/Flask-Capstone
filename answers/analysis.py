# custom
from . import database

# 3rd party
import pandas as pd
import numpy as np


def standard_deviation(column):
    """
    A function to return the standard devation of a given column.
    This function should use the pandas library.
    input:
        column - a string representing the column name
    output:
        output - the standard deviation as a number
    """
    rows = database.rows_to_list_of_dicts()
    df = pd.json_normalize(rows)
    output = df["income"].std()
    return output


def variance(column):
    """
    A functon to calculate the variance of a given column.
    This function should use the numpy library.
    input:
        column - a string representing the column name
    output:
        output - the variance as a number
    """
    rows = database.rows_to_list_of_dicts()
    ages = [row["age"] for row in rows]
    output = np.var(ages)
    return output
