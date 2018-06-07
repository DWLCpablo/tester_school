import string

x = -10
if x < 0 and x % 2 == 0:
    print('x ujemny parzysty')
elif x < 0:
    print('x ujemny nieparzysty')
elif x == 0:
    print('x wynosi 0')
elif x == 10:
    print('x równy 10')
else:
    print('x nieujemny, różny od 10')

def check_number(x):
    try:
        if x == 0:
            return (str(x) + ' jest ło kurwa parzyste.')
        elif x >= 0 and x % 2 == 0:
            return (str(x) + ' jest liczbą dodatnią, parzystą.')
        elif x >= 0 and x % 2 != 0:
            return (str(x) + ' jest liczbą dodatnią, niepatrzystą.')
        elif x < 0 and x % 2 == 0:
            return (str(x) + ' jest liczbą ujemną, parzystą.')
        else:
            return (str(x) + ' jest liczbą ujemną, niepatzystą.')
    except TypeError:
        print('Jak mam sprawdzić jaką liczbą jest litera, albo znak?? Liczbę miałeś podać cioto!')

print(check_number(-4.1))
print(check_number(0))
print(check_number('saas;'''))

def check_number1(x):
    if str(x) not in '1234567890':
        raise TypeError('to nie liczba')
    if x == 0:
        return (str(x) + ' jest ło kurwa parzyste.')
    elif x >= 0 and x % 2 == 0:
        return (str(x) + ' jest liczbą dodatnią, parzystą.')
    elif x >= 0 and x % 2 != 0:
        return (str(x) + ' jest liczbą dodatnią, niepatrzystą.')
    elif x < 0 and x % 2 == 0:
        return (str(x) + ' jest liczbą ujemną, parzystą.')
    else:
        return (str(x) + ' jest liczbą ujemną, niepatzystą.')

print(check_number1(-4.1))
print(check_number1(0))
print(check_number1('saas;'''))