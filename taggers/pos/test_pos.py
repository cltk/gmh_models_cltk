import unittest

from taggers.pos.reader import read_pickle

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class TestPOSTagger(unittest.TestCase):
    def test_token_to_pos(self):
        token_to_pos = read_pickle("tokens_pos.pickle")
        print(token_to_pos["wâr"])
        self.assertEqual(token_to_pos["wâr"], {'PAVW', 'AVW', 'ADJN', 'ADJA', 'AVD', 'ADJD', 'NA', 'VAFIN'})

    def test_tnt_tagger(self):
        tnt_tagger = read_pickle("tnt.pickle")
        self.assertEqual(tnt_tagger.tag("uns ist in alten mæren wunders vil geseit".split(" ")),
                         [('uns', 'PPER'), ('ist', 'VAFIN'), ('in', 'APPR'), ('alten', 'ADJA'), ('mæren', 'ADJA'),
                          ('wunders', 'NA'), ('vil', 'AVD'), ('geseit', 'VVPP')])

    def test_unigram_tagger(self):
        unigram_tagger = read_pickle("unigram.pickle")
        target = [('uns', 'PPER'),
                  ('ist', 'VAFIN'),
                  ('in', 'APPR'),
                  ('alten', 'ADJA'),
                  ('mæren', 'ADJA'),
                  ('wunders', 'NA'),
                  ('vil', 'ADJA'),
                  ('geseit', 'VVPP')]
        self.assertEqual(target, unigram_tagger.tag("uns ist in alten mæren wunders vil geseit".split(" ")))

    def test_bigram_tagger(self):
        bigram_tagger = read_pickle("bigram.pickle")
        target = [('uns', 'PPER'),
                  ('ist', 'VAFIN'),
                  ('in', 'APPR'),
                  ('alten', 'ADJA'),
                  ('mæren', 'NA'),
                  ('wunders', 'NA'),
                  ('vil', None),
                  ('geseit', None)]
        self.assertEqual(target, bigram_tagger.tag("uns ist in alten mæren wunders vil geseit".split(" ")))

    def test_trigram_tagger(self):
        tri_tagger = read_pickle("trigram.pickle")
        target = [('uns', 'PPER'),
                  ('ist', 'VAFIN'),
                  ('in', 'APPR'),
                  ('alten', 'ADJA'),
                  ('mæren', 'NA'),
                  ('wunders', 'NA'),
                  ('vil', None),
                  ('geseit', None)]
        self.assertEqual(target, tri_tagger.tag("uns ist in alten mæren wunders vil geseit".split(" ")))


if __name__ == '__main__':
    unittest.main()
