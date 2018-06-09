
def line_hist(input): # nie dałeś rady
    result = {}
    with open(input, 'rt') as my_file:
        for line in my_file:
            stripped = line.rstrip('\r\n')
            result[len(stripped)] = result.get(stripped, 0) + 1
    return result


def line_histogram2(input_file):
    result = {}
    for line in input_file:
        key = len(line.rstrip('\r\n'))
        result[key] = result.get(key, 0) + 1
    print(result)

if __name__ == '__main__':
    try:
        print(line_hist('plik.txt'))
    except OSError as err:
        print(err)


try:
    with open(path, 'rt') as in_file:
        print(lines_histogram2(in_file))
except OSError as err:
    print(err)