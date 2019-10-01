"""
utility functions for working with sklearn API
"""

from sklearn.model_selection import train_test_split


def tvts(data):
    data = data.copy()
    trainval, test = train_test_split(
        data,
        test_size=.2,
        random_state=None
    )

    val_size = trainval.index_size()

    train, val = train_test_split(
        trainval,
        test_size=val_size,
        random_state=None
    )

    return train, val, test
