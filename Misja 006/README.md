Misja 006
=========
([powrót][1])

Stream: [Gynvael's Livestream #43: Raytracer #2 - implementacja ][2]

Tym razem zadaniem było zdekodowanie następującego ciągu znaków:
```
  c5 c2 c3 c4 c9 c3 40 82 a8 93 82 a8 40 86 81 91 95 a8 40 87 84
  a8 82 a8 40 82 a8 93 40 93 96 87 89 83 a9 95 a8 4b 40 c1 93 85
  40 95 89 85 40 91 85 a2 a3 4b
```

Dodatkowo podana zostałą informacja, że jest to jakieś zdanie w języku Polskim.

Oczywiście, bez namysłu moją pierwszą próbą było trywialne:
```python
"c5c2c3c4c9c34082a89382a84086819195a8408784a882a84082a893409396878983a995a84b40c1938540958985409185a2a34b".decode("hex");
```
Co dało rezultat:
```python
'\xc5\xc2\xc3\xc4\xc9\xc3@\x82\xa8\x93\x82\xa8@\x86\x81\x91\x95\xa8@\x87\x84\xa8\x82\xa8@\x82\xa8\x93@\x93\x96\x87\x89\x83\xa9\x95\xa8K@\xc1\x93\x85@\x95\x89\x85@\x91\x85\xa2\xa3K'
```
No był to bardzo inteligentny pomysł, szególnie gdy widać, że większość bajtów jest >= 0x80, więc wykracza poza standardowe ASCII...
W tym wypadku miałem dwie możliwości:
1. Tekst jest zaszyfrowany, więc można spróbować go zbrutować.
2. Użyte jest jakieś popularne, ale dziwne kodowanie, więc chwile by wystarczyło pogooglować.
Ponieważ nie chciało mi się ani jednego ani drugiego użyłem trzeciej możliwości: Skoro ~~~wszystkie~~~większość bajtów ma zapalony ostatni bit
to może warto spróbować go zgasić. Wiem... też bardzo inteligentne, a nawet jak inteligentne to naiwne, no ale miałem konsolę z Pythonem otwartą
i spróbowałem:
```
str = "c5c2c3c4c9c34082a89382a84086819195a8408784a882a84082a893409396878983a995a84b40c1938540958985409185a2a34b".decode("hex");
for ch in str:
  print ch ^ 0x80
```
Co dało rezultat
```
'E'
'B'
'C'
'D'
'I'
'C'
'\xc0'
'\x02'
'('
'\x13'
'\x02'
...
```
No i jednak takie głupie to nie było. Kolejny krok google:[EBCID][3]. Następnie google:EBCID python i dodanie linijki:
```python
str.decode('cp500');
```
Dzięki czemu odszyfrowałem wiadomość która brzmi: ```EBCDIC bylby fajny gdyby byl logiczny. Ale nie jest.```

([powrót][1])

[1]: ../README.md
[2]: https://www.youtube.com/watch?v=w-7vLvTKJbI
[3]: https://pl.wikipedia.org/wiki/EBCDIC