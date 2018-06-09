F = 70
C = float((F - 32) * 5 / 9)
print (C)
print (type(C))
print('cokolwiek')




def lbs_to_kg(x):
    try:
        return x // 2.2046
    except TypeError as err:
        print('Waga musi być wyrażona numerycznie silly goose.')
        print('Zwrócony błąd:', err)
print(lbs_to_kg('11'))