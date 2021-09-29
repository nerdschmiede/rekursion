"""
Dieses Module enthält rekursive Lösungen zu einer Reihe von Fragestellungen sortiert nach den Eingaben.

Eingaben sind:
- Zahlen
- Texte
- Listen
"""

"""Zahlen"""


def fakultaet(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return fakultaet(n - 1) * n


def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def summe_bis(n: int) -> int:
    if n == 0:
        return 0
    else:
        return summe_bis(n - 1) + n


def produkt(a: int, b: int) -> int:
    if a == 0:
        return 0
    else:
        return produkt(a - 1, b) + b


def potenz(basis: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    else:
        return potenz(basis, exponent - 1) * basis


def rest(dividend: int, divisor: int) -> int:
    if dividend < divisor:
        return dividend
    else:
        return rest(dividend - divisor, divisor)


"""Texte"""


def laenge(text: str) -> int:
    if text == "":
        return 0
    else:
        text_ein_element_kuerzer = text[1:]
        return laenge(text_ein_element_kuerzer) + 1


def rueckwaerts(wort: str) -> str:
    if len(wort) <= 1:
        return wort
    else:
        erster_buchstabe = wort[0]
        restliches_wort = wort[1:]
        return rueckwaerts(restliches_wort) + erster_buchstabe


def anzahl(buchstabe: str, wort: str) -> int:
    if wort == "":
        return 0
    else:
        erster_buchstabe = wort[0]
        restliches_wort = wort[1:]
        if erster_buchstabe == buchstabe:
            return anzahl(buchstabe, restliches_wort) + 1
        else:
            return anzahl(buchstabe, restliches_wort) + 0


def ist_palindrom(wort: str) -> bool:
    if len(wort) <= 1:
        return True
    else:
        erster_buchstabe = wort[0]
        letzter_buchstabe = wort[-1]
        if erster_buchstabe != letzter_buchstabe:
            return False
        else:
            enden_abgeschnittenes_wort = wort[1:-1]
            return ist_palindrom(enden_abgeschnittenes_wort)


def finde(buchstabe: str, text: str) -> int:
    if len(text) == 0:
        return -1
    else:
        naechster_buchstabe = text[0]
        restlicher_text = text[1:]
        if naechster_buchstabe == buchstabe:
            return 0
        else:
            return finde(buchstabe, restlicher_text) + 1


def ersetze(alter_buchstabe: str, neuer_buchstabe: str, text: str) -> str:
    if text == "":
        return ""
    else:
        erster_buchstabe = text[0]
        restlicher_text = text[1:]
        if erster_buchstabe == alter_buchstabe:
            return neuer_buchstabe + ersetze(alter_buchstabe, neuer_buchstabe, restlicher_text)
        else:
            return erster_buchstabe + ersetze(alter_buchstabe, neuer_buchstabe, restlicher_text)


"""Listen"""


def laenge_von(liste: list) -> int:
    if not liste:
        return 0
    else:
        liste.pop()
        return laenge_von(liste) + 1


def maximum(liste: list) -> int:
    if len(liste) == 1:
        return liste[0]
    else:
        naechster_kandidat = liste.pop()
        bisheriges_maximum = maximum(liste)
        if naechster_kandidat > bisheriges_maximum:
            return naechster_kandidat
        else:
            return bisheriges_maximum


def summe(liste: list) -> int:
    if not liste:
        return 0
    else:
        summand = liste.pop()
        return summe(liste) + summand


def enthaelt(element, liste: list) -> bool:
    if not liste:
        return False
    else:
        naechstes_element = liste.pop()
        if element == naechstes_element:
            return True
        else:
            return enthaelt(element, liste)
