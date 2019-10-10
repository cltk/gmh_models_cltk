"""

"""

import pickle

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_pickle(filename: str):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data


def test_lemma_to_tokens():
    lemma_to_tokens = read_pickle("lemma_to_tokens.pickle")
    print(lemma_to_tokens["wësen"])


def test_lemmatizer():
    token_to_lemma = read_pickle("token_to_lemma.pickle")
    print(token_to_lemma["wâr"])


if __name__ == "__main__":
    test_lemma_to_tokens()
    test_lemmatizer()
