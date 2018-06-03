a = float(input('Podaj liczbę dla boku a: '))
b = float(input('Podaj liczbę dla boku b: '))
c = float(input('Podaj liczbę dla boku c: '))


if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print ('trójkąt o bokach a, b, c jest prawdziwy')
    else:
        print ('Impossibru')
else:
    print ('Impossibru')
