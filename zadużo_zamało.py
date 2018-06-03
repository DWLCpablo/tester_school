#pra za dużo za mało, zgadłeś!
#komputer daje podpowiedzi, zlicza też próby i wypluwa na końcu ile prób

import random

#boss - działa
def int_input(prompt):
    try:
        lower_bound = int(input('Podaj dół zakresu: '))
        upper_bound = int(input('Podaj górę zakres: '))
        target = random.randint(lower_bound, upper_bound)
        guess = None
        count = 0

        while target != guess:
            count += 1
            guess = int(input('Podaj liczbę: '))
            if guess < target:
                print('za mało')
            elif guess > target:
                print('za dużo')

        print('Gratki, Ilość ruchów: ', count)
    except ValueError as err:  #jeżeli jakaś linijka w try da błąd to program przerywa działanie z try, i przechodzi do except
        print('Oczekiwano liczby. Nie można kontynuować')
        print('Zwrócony błąd: ', err)
int_input('Libcza')