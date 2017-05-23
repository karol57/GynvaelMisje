Misja 003
=========
([powrót][1])

Stream: [Gynvael's Livestream #39: RPC, czyli zdalne API][2]

Tym razem misja była prosta i opierała się na odpaleniu kodu w Pythonie, który można znaleźć [tutaj][3]. Po pewnym
czasie otrzymujemy  wiadomość ```Haslo: "WolneOprogramowanie!"``` i tyle...

...no i byłby koniec, gdyby ten "pewien czas" nie trwał na tyle długo, że nikomu normalnemu raczej nie będzie się
chciało czekać (nie wiem czy by mu sto lat wystarczyło). 

A więc mamy kod, który bierze sobie dość duże inty, robi z nimi coś i dekoduje hasło. Naszym zadaniem jest optymalizacja
tego kodu. Ponieważ pierwszą linijką robiącą to coś jest ```n = magic2(magic1(n1, n2), 1337)``` więc wypadało by się
dowiedzieć co robią funkcje ```magic1``` oraz ```magic2```.
```python
def magic1(a, b):
  o = 0
  i = 0
  while i < a:
    o += 1
    i += 1
  i = 0
  while i < b:
    o += 1
    i += 1
  return o
```
Po krótkiej analizie widać, że obie pętle dodają odpowiednio ```a``` i ```b``` odpowiednio do zmiennych ```o``` oraz
```i```, więc można je zastąpić dużo prostszymi sekwencjami:
```python
def magic1(a, b):
  o = 0
  i = 0
  o += a
  i += a
  i = 0
  o += b
  i += b
  return o
```
Co upraszcza się do:
```python
def magic1(a, b):
  return a + b
```
teraz można 'zoptymalizować' drugą funkcję, co powinno być już zadaniem trywialnym:
```python
def magic2(a, b):
  o = 0
  i = 0
  while i < b:
    #o = magic1(o, a)
    o += a
    i += 1
  return o
```
```python
def magic2(a, b):
  return a * b
```

Ostatecznie nasza linijka przybiera postać ```n = (n1 + n2) * 1337``` i kod wykonuje się w normalnym czasie.

Oczywiście pozostała jeszcze linijka: ```hex(n)[2:-1].decode("hex").splitlines()[0]```, którą wystarczy rozbić na
```python
print n
print hex(n)
print hex(n)[2:-1]
print hex(n)[2:-1].decode("hex").splitlines()
print hex(n)[2:-1].decode("hex").splitlines()[0]
```
Z czego otrzymamy:
```
549264340234998467129494984689502898642039973222263002891494221114915022603203250023
0x4861736c6f3a2022576f6c6e654f70726f6772616d6f77616e696521220a0a0a0a0767L
4861736c6f3a2022576f6c6e654f70726f6772616d6f77616e696521220a0a0a0a0767
['Haslo: "WolneOprogramowanie!"', '', '', '', '\x07g']
Haslo: "WolneOprogramowanie!"
```
Szczerze mówiąc, jak zobaczyłem ```splitlines()[0]```, byłem pewien, że Gynvael ukrył jeszcze coś w pozostałych
linijkach. Kod ze wszystkimi powyższymi modyfikacjami możemy zobaczyć [tutaj][4].

([powrót][1])

[1]: ../README.md
[2]: https://www.youtube.com/watch?v=xR0hAJPp1vs
[3]: code.py
[4]: code_fixed.py