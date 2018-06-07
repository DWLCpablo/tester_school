# to ma błędy (zajęcia)
liczba = float(input('podaj liczbę = '))

suma = 0
ile_razy = 0


while liczba >= 0:
    liczba = float(input('podaj liczbę = '))
    if liczba >= 0:
        suma += liczba
        ile_razy += 1

if ile_razy == 0:
    print('nie podano ujemnej liczby')
else:
    print ('Podano tyle nieujemnych liczb: ', ile_razy)
    print('Ich średnia: ', suma / ile_razy)
# to działa jak należy, poprawiłeś solo
suma = 0
ile_razy = 0
liczba = int(input('Podaj liczbę nieujemną: '))
if liczba >= 0:
    ile_razy += 1
    suma += liczba
else:
    print('To liczba ujemna')
while liczba >= 0:
    liczba = int(input('Podaj liczbę nieujemną: '))
    if liczba >= 0:
        suma += liczba
        ile_razy += 1
print('podałeś ', str(ile_razy), 'liczb nieujemnych, które dały sumę', str(suma))