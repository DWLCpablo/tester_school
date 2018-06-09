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
#moje
import random
def wyzej_nizej():
    try:
        dolna = int(input('Podaj dół zakresu: '))
        gorna = int(input('Podaj górę zakresu: '))
        while dolna > gorna:
            print('Dół zakresu nie może być wyższy niż góra. Eejit.')
            dolna = int(input('Podaj dół zakresu: '))
            gorna = int(input('Podaj górę zakresu: '))
        target = random.randint(dolna, gorna)
        guess = int(input('Zgadnij liczbę: '))
        count = 1
        while guess != target:
            count += 1
            if guess > target:
                guess = int(input('To niższa liczba: '))
            elif guess < target:
                guess = int(input('To wyższa liczba: '))
        print('Gratki, zgadłeś. Ta liczba to', str(target) + '. Udało Ci się w', count, 'próbach.')
    except ValueError as err:
        print('Oczekiwano liczby. Nie można kontynuować')
        print('Zwrócony błąd: ', err)
wyzej_nizej()