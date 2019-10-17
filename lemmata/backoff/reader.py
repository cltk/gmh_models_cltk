"""

"""

import pickle

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_pickle(filename: str):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data
