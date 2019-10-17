# POS

## Tagset
Links to tagset 

* https://www.linguistics.rub.de/rem/documentation/pos.html (in German)
* https://www.linguistics.rub.de/~dipper/pub/zgl15.pdf (in German)
* https://linguistics.rub.de/forschung/arbeitsberichte/19.pdf (in German)

## File format

All tokens are normalized according to [Referenzkorpus Mittelhochdeutsch](https://linguistics.rub.de/forschung/arbeitsberichte/19.pdf)'s rules.

* tnt.pickle: TnT instance trained with list of annotated sentences of the form [(token1, pos_1), (token_2, pos_2), ...]
* norm_pos.pickle: [(token1, {pos1_1, pos1_2, ...}), (token2, {pos2_1, pos2_2, ...}), ...]

