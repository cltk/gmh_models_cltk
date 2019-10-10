"""

"""

import pickle

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_pickle(filename: str):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data


def test_token_to_pos():
    token_to_lemma = read_pickle("tokens_pos.pickle")
    print(token_to_lemma["wâr"])


if __name__ == "__main__":
    test_token_to_pos()
