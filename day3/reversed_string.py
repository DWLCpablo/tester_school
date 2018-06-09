def reversed(input):
    with open('plik.txt', 'r+t') as my_file:
        my_file.write(input[::-1])

reversed('PABLO NAJLEPSZYM NASZYM PRZYJACIELEM JEST')

def reversed1(open_path, saved_path):
    try:
        with open(open_path, 'rt') as my_file:
            data = my_file.read()
        with open(saved_path, 'wt') as my_file:
            my_file.write(data[::-1])
    except OSError as err:
        print(err)

reversed1('plik.txt', 'plik_2.txt')

def reverse_file(input_path, output_path): # boss
    with open(input_path, 'rt') as input_file:
        data = input_file.read()

    with open(output_path, 'wt') as output_file:
        output_file.write(data[::-1])

if __name__ == '__main__':
    reverse_file('plik.txt', 'plik_reversed.txt')
    print('test!!')


with open('plik.txt') as my_file: #wszystkie linie ze znakami \n
    lines = my_file.readlines()
    print(lines)

with open('plik.txt') as my_file: # wszystkie linie z dodatkowym 'enterem' = nową linią
    for line in my_file:
        print(line)

text = 'some text'
print(text.rstrip('\r\n'))