"""
utility functions for working with DataFrames using sklearn API
"""

from sklearn.model_selection import train_test_split


def tvts(data):
    """
    split DataFrame into train (60%), validation (20%), test (20%)
    """
    data = data.copy()
    trainval, test = train_test_split(
        data,
        test_size=.2,
        random_state=None
    )

    val_size = test.index_size()

    train, val = train_test_split(
        trainval,
        test_size=val_size,
        random_state=None
    )

    return train, val, test
