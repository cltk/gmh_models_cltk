"""

"""

import pickle

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_pickle(filename: str):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data


def test_token_to_pos():
    token_to_pos = read_pickle("tokens_pos.pickle")
    print(token_to_pos["wâr"])
    tnt_tagger = read_pickle("tnt.pickle")
    print(tnt_tagger.tag("uns ist in alten mæren wunders vil geseit".split(" ")))


if __name__ == "__main__":
    test_token_to_pos()
