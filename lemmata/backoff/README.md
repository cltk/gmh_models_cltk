# Lemmata

All tokens are normalized according to [Referenzkorpus Mittelhochdeutsch] rules.
 
lemma_to_tokens.pickle: {lemma1: {token1_1, token1_2, ...], lemma2: {token2_1, token_2_2, ...}, ...}
token_to_lemma.pickle: {token1: {lemma1_1, lemma1_2, ...], token2: {lemma2_1, lemma_2_2, ...}, ...}
sentences: [token]


DictLemmatizer: {token1: lemma1, token2: lemma2, ...} 
UnigramLemmatizer: list of sentences, where a sentence is [(token1, lemma1), (token2, lemma2, ...)]
