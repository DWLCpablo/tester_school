#napisać program który dla danego słowa skonstruuje słownik zawierający częstości występowania poszczególnych liter. JJeżeli w podanym słowie znajdą się znaki inne niż litery to pogram powinien je zliczyć i umieścić pod jedną pozycją 'others' Program powinien ignorować wielkość znaków.


# boss
text = 'Ala ma kota'
hist = {'a': 4, 'm': 1, 'k': 1, 'l': 1, 'o': 1, 't': 1, 'others': 3}

def histogram(text):
    hist = {}
    for char in text.lower():
        if char.isalpha() and char not in hist:
            hist[char] = hist.get(char, 0) + 1
    else:
        hist['others'] = hist.get('others', 0) + 1
    return hist
print(histogram('Ala ma kota!'))

# tutaj others jest błędne !!