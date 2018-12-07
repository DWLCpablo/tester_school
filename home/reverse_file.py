def reverse(input_file, output_file):
    with open(input_file, 'rt') as plik:
        data = plik.read()
    with open(output_file, 'wt') as plik:
        for line in plik.readlines():
            plik.write(data[0:5])

print(reverse('multiple.txt', 'multiple_reversed.txt'))