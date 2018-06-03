# bubbleize(text - funkcja zwraca łańcuch znaków powstały z text poprzez zmianę co drugiej litery na dużą, co drugiej na małą
#randomize(text) - zwraca łańcuch znaków powstały z text przez losowowe poustawianie wielkości liter w text
#numberize(text) - zwraca łańcuch powstały z text poprzez zmianę wszystkich wystąpień litery e na 3, litery 'o' na 0,  litery 'i' na '!'  oraz litery 'a' na @
"""Module for funny string manipulations"""
from random import randint

def bubbleize(text):
    """Returns bubbleized strings
       Args:
           text: text to bubbleize
       Returns:
           bubbleized text
       """
    nowy = ''
    text = text.lower()
    for idx, char in enumerate(text):
        if idx % 2 == 1:
            nowy += char.upper()
        else:
            nowy += char
    return nowy

def bubbleize_2(text):
    chars = []
    for idx, char in enumerate(text):
        if idx % 2:
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)


def randomize(text):
    chars = []
    for idx, char in enumerate(text):
        if random.randint(0, 1):
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)