import unittest

from lemmata.backoff.reader import read_pickle


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class TestLemmatizer(unittest.TestCase):

    def test_lemma_to_tokens(self):
        lemma_to_tokens = read_pickle("lemma_to_tokens.pickle")
        self.assertEqual(lemma_to_tokens["wësen"], {'[wære]',
                                                    'gewesen',
                                                    'gewesene',
                                                    'gewesener',
                                                    'geweset',
                                                    'gewest',
                                                    'w[ær]e',
                                                    'warent',
                                                    'wart',
                                                    'was',
                                                    'waz',
                                                    'wer',
                                                    'wese',
                                                    'wesen',
                                                    'wesene',
                                                    'wesenes',
                                                    'wesenne',
                                                    'wesent',
                                                    'wesente',
                                                    'wesentem',
                                                    'wesenten',
                                                    'wesenter',
                                                    'wesentere',
                                                    'weset',
                                                    'wis',
                                                    'wise',
                                                    'wisen',
                                                    'wises',
                                                    'wiset',
                                                    'wâr',
                                                    'wâre',
                                                    'wâren',
                                                    'wârent',
                                                    'wâres',
                                                    'wâret',
                                                    'wârn',
                                                    'wârt',
                                                    'wær',
                                                    'wære',
                                                    'wæren',
                                                    'wærent',
                                                    'wæres',
                                                    'wærest',
                                                    'wæret',
                                                    'wærn',
                                                    'wærs',
                                                    'wærst',
                                                    'wært'})

    def test_lemmatizer(self):
        token_to_lemma = read_pickle("token_to_lemma.pickle")
        self.assertEqual(token_to_lemma["wâr"], {'war(e)',
                                                 'wâr',
                                                 'wâr/+abe',
                                                 'wâr/+ane',
                                                 'wâr/+inne',
                                                 'wâr/+mit(e)',
                                                 'wâr/+nâh',
                                                 'wâr/+umbe',
                                                 'wâr/+zuo',
                                                 'wâr/+ûf',
                                                 'wâr/+ûz',
                                                 'wâr/+über(e)',
                                                 'wâr/.+nû',
                                                 'wâr/.+umbe',
                                                 'wâre',
                                                 'wësen'})


if __name__ == '__main__':
    unittest.main()
