import pandas as pd
from pandas import DataFrame


def lambda_handler(event, context):
    # TODO implement
    df1 = DataFrame([{'a': 1, 'b': 1, 'c': 1}, {'a': 2, 'b': 1, 'c': 3}])
    df2 = DataFrame([{'a': 1, 'b': 1, 'c': 1, 'd': 1}, {'a': 2, 'b': 1, 'c': 3, 'd': 4}])
    test = pd.concat([df1, df2])

    return test
