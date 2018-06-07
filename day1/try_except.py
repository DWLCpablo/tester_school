number = None
while number is None:
    try:
        number = int(input('Podaj liczbę: '))
    except ValueError as err:
        print('To nie liczba...')
        print(err)
print('Podałeś: ', number)