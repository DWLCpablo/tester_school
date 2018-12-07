def line_hist(text_file): #HAHAHAHAHAHA, sam napprawiłeś
    result = {}
    with open(text_file, 'rt') as my_file:
        for line in my_file.readlines():
            result[len(line)] = result.get(len(line), 0) + 1
            if result[len(line)] > 0:
                result[len(line)] += 1
        return result

print(line_hist('multiple.txt'))


def line_hist1(input): # nie dałeś rady
    result = {}
    with open(input, 'rt') as my_file:
        for line in my_file:
            stripped = line.rstrip('\r\n')
            result[len(stripped)] = result.get(stripped, 0) + 1
            if result[len(stripped)] > 0:
                result[len(stripped)] += 1
    return result

