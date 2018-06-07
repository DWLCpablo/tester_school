import random
# boss
def int_input():
    number = None
    while number is None:
        try:
            number = int(input('Dawaj liczbę: '))
        except ValueError:
            print('To nie jest liczba.')
    return number
    while lower_bound > upper_bound:
        lower_bound = int_input('Podaj dół zakresu: ')
        upper_bound = int_input('Podaj górę zakres: ')
        if lower_bound > upper_bound:
            print('Początek zakresu nie może być wiekszy niż koniec...')
    target = random.randint(lower_bound, upper_bound)
    guess = None
    count = 0

    while target != guess:
        count += 1
        guess = int_input('Podaj liczbę: ')
        if guess < target:
            print('za mało')
        elif guess > target:
            print('za dużo')

    return('Gratki, Ta liczba to ' + str(target) + '. Ilość ruchów: ', count)
int_input()