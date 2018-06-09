#napisać program który dla danego słowa skonstruuje słownik zawierający częstości występowania poszczególnych liter. JJeżeli w podanym słowie znajdą się znaki inne niż litery to pogram powinien je zliczyć i umieścić pod jedną pozycją 'others' Program powinien ignorować wielkość znaków.
# poprawiłeś bossa, chyba źle przepisałeś, teraz działa
def histogram(text):
    dic = {}
    for char in text.lower():
        if char.isalpha() and char not in dic:
            dic[char] = dic.get(char, 0) + 1
        elif char.isalpha() and char in dic:
            dic[char] = dic[char] + 1
        elif char == ' ' and char not in dic:
            dic['others'] = dic.get('others', 0) + 1
        else:
            dic['others'] = dic['others'] + 1
    return dic
print(histogram('Pablo Najlepzymsadsa..,..,....????? Naszym przyjAcielem jEst'))