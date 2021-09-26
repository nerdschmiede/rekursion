import math
import random
import string
import unittest

from rekursion import *


class TestRekursionenMitZahlen(unittest.TestCase):

    def test_fakultaet(self):
        for i in range(10):
            self.assertEqual(fakultaet(i), math.factorial(i))

    def test_fibonacci(self):
        fibonacci_zahlen = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for nummer, fibonacci_zahl in enumerate(fibonacci_zahlen):
            self.assertEqual(fibonacci(nummer + 1), fibonacci_zahl)

    def test_summe_bis(self):
        summen_zahlen = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        for nummer, summen_zahl in enumerate(summen_zahlen):
            self.assertEqual(summe_bis(nummer), summen_zahl)

    def test_produkt(self):
        for i in range(10):
            for j in range(10):
                self.assertEqual(produkt(i, j), i * j)

    def test_potenz(self):
        for i in range(10):
            for j in range(10):
                self.assertEqual(potenz(i, j), i ** j)

    def test_rest(self):
        for dividend in range(2, 10):
            for divisor in range(1, dividend):
                self.assertEqual(rest(dividend, divisor), dividend % divisor)


class TestRekursionenMitText(unittest.TestCase):
    def test_laenge(self):
        text = string.ascii_lowercase
        for stelle, _ in enumerate(text):
            self.assertEqual(laenge(text[0:stelle]), stelle)

    def test_rueckwaerts(self):
        alphabet = string.ascii_lowercase
        for stelle, _ in enumerate(alphabet):
            test_wort = alphabet[:stelle]
            test_wort_rueckwaerts = test_wort[::-1]
            self.assertEqual(rueckwaerts(test_wort), test_wort_rueckwaerts)

    def test_anzahl(self):
        wort = "mississippi"
        self.assertEqual(anzahl("m", wort), 1)
        self.assertEqual(anzahl("i", wort), 4)
        self.assertEqual(anzahl("s", wort), 4)
        self.assertEqual(anzahl("p", wort), 2)
        self.assertEqual(anzahl("a", wort), 0)

    def test_palindrom(self):
        self.assertEqual(ist_palindrom("reliefpfeiler"), True)
        self.assertEqual(ist_palindrom("python"), False)

    def test_finde(self):
        alphabet = string.ascii_lowercase
        for stelle, buchstabe in enumerate(alphabet):
            self.assertEqual(finde(buchstabe, alphabet), stelle)

    def test_ersetzen(self):
        self.assertEqual(ersetze(' ', '', "Python Ist Toll"), "PythonIstToll")


class TestRekursionenMitListen(unittest.TestCase):

    def test_maximum(self):
        for _ in range(10):
            liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            random.shuffle(liste)
            self.assertEqual(maximum(liste), 10)

    def test_summe(self):
        liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(summe(liste), 55)

    def test_laenge_von(self):
        liste = ['p', 'y', 't', 'h', 'o', 'n']
        self.assertEqual(laenge_von(liste), 6)
        liste = [4, 2, ' ', 'i', 's', 't ', ' ', 'd', 'i', 'e ', ' ', 'a', 'n', 't', 'w', 'o', 'r', 't']
        self.assertEqual(laenge_von(liste), 18)

    def test_enthaelt(self):
        liste = ['spam', 'eggs']
        self.assertEqual(enthaelt('spam', liste), True)
        self.assertEqual(enthaelt('foo', liste), False)


if __name__ == '__main__':
    unittest.main(exit=False)
