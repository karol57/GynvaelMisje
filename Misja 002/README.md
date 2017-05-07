Misja 002
=========
([powrót][1])

Stream: [Gynvael's Livestream #38: Pluginy, DLLki - z czym to się je][2]

Kolejna misja polegała na zdekodowoaniu następującej wiadomości:
```
QW== QT== QT== QQ== QU== Qd== QU== Qd==
QX== QV== QW== Qe== QT== QR== QU== QT==
QT== QU== QX== QU== QT== QR== QT== QQ==
QW== Qe==
```
Niestety trochę sobie zaspojlerowałem i wiem, że rozwiązaniem będzie słowo *communication*...

W każdym razie od razu widać, że użyto kodowania base64, jednak dekodowanie wiadomości daje za każym razem wynik
"AAAAAAAAAAAAAAAAAAAAAAAAAA", co jest złym wynikiem.

Oczywiście pierwszym odruchem było sprawdzenie jak działa base64 na [wiki][3] oraz szybka migracja na
[angielską wersję artykułu][4], ponieważ nic nie przemawia lepiej niż przykłady.

Kolejnym krokiem jest szybka próba ręcznego dekodowania wiadomości:
```
   Q      W      =      =
  16     22      -      -
010000 010110 ------ ------
   Q      T      =      =
  16     19      -      -
010000 010011 ------ ------
   Q      T      =      =
  16     22      -      -
010000 010011 ------ ------
   Q      Q      =      =
  16     16      -      -
010000 010000 ------ ------
   Q      U      =      =
  16     20      -      -
010000 010100 ------ ------
  Q      d      =      =
 16     29      -      -
010000 011101 ------ ------
```

Można zauważyć, że każde 4 znaki kodują 1,5 bajta (gdyby kodowały 3 bajty to sekwencje kończyły by się znakami AA):
```
01000001 0110---- --------
01000001 0011---- --------
01000001 0011---- --------
01000001 0000---- --------
01000001 0100---- --------
01000001 1101---- --------
```
Oczywiście ```0b01000001 0x41 65``` jest kodem literki A w [ASCII][5], dlatego dekodery zwracają ją jako wynik.
```
01100011
00110000
01001101
```
Co po zdekodowaniu daje ciąg ```c0M```. Zgadza się ze spojlerem, strzał okazał się trafiony i w sumie jedyne co się
nauczyłem to jak działa base64. Dzisiaj było prosto, więc dla urozmaicenia napisałem jeszcze
[prosty skrypt w Pythonie][6], który dekoduje całą wiadomość, która brzmi: ```c0MMun1C4t10n```
Oczywiście jakbym znał lepiej Pythona to kod był by krótszy... znacznie krótszy, jak np. [ten][7].

([powrót][1])

[1]: ..\README.md
[2]: https://www.youtube.com/watch?v=FN-5CowRdXM
[3]: https://pl.wikipedia.org/wiki/Base64
[4]: https://en.wikipedia.org/wiki/Base64
[5]: https://pl.wikipedia.org/wiki/ASCII
[6]: decode.py
[7]: https://gist.github.com/nowakartur/b36bda8be95118a1908b009e91f6a9be