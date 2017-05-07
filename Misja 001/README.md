Misja 001
=========
([powrót][1])

Stream: [Gynvael's Livestream #37: Jak nie szyfrować - XOR][2]

Misja polegała na rozszyfrowaniu następującej listy angielskich słów, które były zaszyfrowane tym samym (160-bitowym)
kluczem.
```
1f9111
1799
0790001226d8
0a9e1e5c3ada
1f
099e195e
0a97075a21dac1
0a9710
199e075131d3
1199
12961350
```
Moim rozwiązaniem był "inteligentny" brute-force. Pierwszym krokiem było uzyskanie słownika czyli [listy wszystkich
angielskich słów][3]. Następnie słowa do rozszyfrowania zostały posortowane w kolejności od najkrótszego do
najdłuższego. Słownik został posortowany w ten sam sposób, lecz wcześniej zostały z niego usunięte wszystkie wyrazy
krótsze oraz dłuższe od zaszyfrowanych słów.

Z tak przygotowanymi danymi można było zacząć łamać klucz. Algorytm zaczyna od najkrótszego zaszyfrowanego słowa i
XORuje je ze wszystkimi słowami w słowniku o tej samej długości uzyskiwając podstawowe klucze. Następnie brane jest
kolejne słowo, które jest XORowane ze swoimi rówieśnikami i uzyskujemy kolejną listę kluczy. Z owej listy zachowywane są
tylko te klucze, których początek zgadza się z którymś z kluczy podstawowych. Tak uzyskane klucze są używane jako klucze
podstawowe w kolejnych iteracjach. Po zbrutowaniu wszystkich zaszyfrowanych słów uzyskujemy klucze, które dają sensowne
rozwiązania. W tym wypadku jest ono tylko jedno.

Klucz: 7eff753554bda9
```
and
if
you're
taking
a
walk
through
the
garden
of
life
```
Jest to pierwsze zdanie w utworze Blood Brothers zespołu Iron Maiden.

Oczywiście możliwe jest otrzymanie tylko 56-bitów klucza, ponieważ tyle miało najdłuższe słowo. Oczywiście zapraszam
do lektury kodu deszyfrującego w pliku [decode.py][4]

([powrót][1])

[1]: ..\README.md
[2]: https://www.youtube.com/channel/UCjS2aGCvsnhExcWRAI8T4Pw
[3]: https://github.com/dwyl/english-words/blob/master/words.txt
[4]: decode.py