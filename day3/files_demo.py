my_file = None
try:
    my_file = open('plik.txt', 'rt')
    data = my_file.read()
    print(data)
    my_file.close()
except OSError as err:
    print('Error: ', str(err))
finally:
    if my_file is not None:
        print('Zamykam')
        my_file.close()

try: #rekomendowana składnia odczytywania pliku
    with open('plik2.txt') as my_file:  # menadżer kontekstu, konstrukcja automatycznie zamykająca plik
        print(my_file.read())
except OSError as err:
    print(err)

with open('plik3.txt', 'wt') as out_file:
    out_file.write('cokolwiek')
