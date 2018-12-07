def reversed(string):
    return string[::-1]

def multiple(string, x):
    return (string + '\n') * x

string = 'Pablo najlepszym naszym przyjacielem jest \n a twój stary jest ciasny \n a twoja siora mmmmmm'
string_2 = 'dupa dupa dupa'
with open('reversed.txt', 'wt') as new_file:  #działa
    new_file.write(reversed(string))

with open('multiple.txt', 'wt') as new_file:  #działa
    new_file.write(multiple(string, 5))

with open('multiple.txt', 'at') as new_file:  # działa; 'at' = append (zamiast + z notatek)
    new_file.write(multiple(string_2, 5))

with open('multiple.txt', 'rt') as new_file: #działa
    print(new_file.read())

with open('multiple.txt', 'rt') as new_file: #działa
    print(new_file.readline()) # readline() = odczytywanie pojedynczej linii

with open('multiple.txt', 'rt') as new_file:
    lines = new_file.readlines() # zwraca listę z linijkami, oddzielonymi \n
    for line in lines:
        print(line)


try:  #najlepsza konstrukcja otwierania plików z try/except
    with open('multiple1.txt', 'rt') as new_file:
        new_file.read()
except OSError as err:
    print('Chuja', err)