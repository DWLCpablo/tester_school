x = 25


for item in range(x+1):
    if item ** 2 == x:
        print(x, 'to kwadrat liczby ', item)
    else:
        print(x, 'nie jest kwadratem.')


# poprawione solo
x = 25
bool = False

for item in range(x+1):
    if item ** 2 == x:
        bool = True
        print(x, 'jest kwadratem liczby', item)

if bool == False:
    print(x, 'nie jest kwadratem żadnej liczby.')

