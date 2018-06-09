def choinka(N):
    try:
        x = '*'
        for i in range(1, N+1):
            print(((N-i) * ' ' + (2 * i -1) * x))
    except TypeError as err:
        print('Naughty boy. Wpisz liczbę całkowitą, nie floata, literę, albo inne ciulstwo.')
        print('Zwrócony błąd:', err)
choinka(5)
choinka(4.0)
N = 5
x = '*'

for i in range(1, N): #trójkąt prostokątny
    print(x*i)
