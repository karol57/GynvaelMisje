Misja 007
=========
([powrót][1])

Stream: [Gynvael's Livestream #44: Raytracer #3 - optymalizacja][2]

A więc pojawiła się kolejna misja:
```
MISJA 007            [goo.gl/f6ogMR][3]                  DIFFICULTY: █░░░░░░░░░ [1/10]
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅
Otrzymaliśmy zaszyfrowaną wiadomość. Podobno użyty został potężny algorytm ROTn,
ale ze zmieniającym się kluczem. Klucz podobno zmienia się w prosty do
przewidzenia sposób, więć zostawiamy rozkodowanie wiadomości Tobie:

  KFGS WUSTRX DBZAYE KIGHFL RPNOMS

--

Odzyskaną wiadomość umieśc w komentarzu pod tym video :)
Linki do kodu/wpisów na blogu/etc z opisem rozwiązania są również mile
widziane!

P.S. Rozwiązanie zadania przedstawie na początku kolejnego livestreama.
```

Ponieważ jak można się domyślić ROTn określa rodzinę szyfrów ROT1, ROT2, ..., [ROT13][4], ..., ROT25, więc jest to tzw. [Szyfrem Cezara][5].

Ponieważ w tekście misji jest wspomniane, że szyfr zmienia się w prosty sposób, więc pierwszym strzałem jest,
że n zmienia się o jakąś stałą wartość z każdym znakiem tekstu.

Szybko postała funkcja, która dekoduje w taki tekst:
```python
def rotn(msg, n, inc):
	result = []
	for i, ch in enumerate(msg):
		if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
			result.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A')))
		else:
			result.append(ch);
		n += inc
	return ''.join(result)
```

Łatwo zauważyć, że n ∈ [0;25] oraz inc ∈ [0;25]. Ponieważ w alfabecie angielskim jest tylko 26 liter i wyższe wartości "zawijają się" i odpowiadają reszcie z dzielenie siebie przez 26.
Więc mamy tylko 676 możliwości, co można łatwo zbrutforce'ować. Dwie proste pętle, rzut okiem na wyniki i dla inc = 25 oraz n = 0 otrzymujemy ```KEEP ROLLIN ROLLIN ROLLIN ROLLIN```.

[Tutaj][6] cały kod.

([powrót][1])

[1]: ../README.md
[2]: https://www.youtube.com/watch?v=JXZicjwhpwQ
[3]: https://goo.gl/f6ogMR
[4]: https://pl.wikipedia.org/wiki/ROT13
[5]: https://pl.wikipedia.org/wiki/Szyfr_Cezara
[6]: decode.py