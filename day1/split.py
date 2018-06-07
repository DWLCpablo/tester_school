#program dzielący łańcuch znaków w miejscach gdzie pojawia się dany separator i towrzący listę powstałych
#boss
numbers = '123,21,27,3'
def split(text, sep):

    parts = []
    current_part = ''
    for char in text:
        if char != sep:
            current_part += char
        else:
            parts.append(current_part)
            current_part = ''
    parts.append(current_part)
    return parts

print(split(numbers, ','))


def split1(text, sep):
    return text.split(',')

print(split1(numbers, ','))

# z .join()
def split(text, sep):
    parts = []
    current_part = []
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []
    parts.append(''.join(current_part))
    return parts

print(split(numbers, ','))

#ze slicem Gosia
def split3(text, sep):
    parts = []
    start = 0
    curr = 0
    for char in text:
        if char != sep:
            curr += 1
        else:
            parts.append(text[start:curr])
            start = curr + 1
            curr += 1
    parts.append(text[start:curr])
    return parts

print(split3(numbers, ','))

#ze slicem boss
def split4(text, sep):
    parts = []
    start = 0
    for current, char in enumerate(text):
        if char == sep:
            parts.append(text[start:current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split4(numbers, ','))


def split(text, sep):
    try:
        return sep.join(text.split(sep))
    except AttributeError as err:
        print('Separator nie może być liczbą.')
        print('Błąd: ', err)
print(split(numbers, 9))


def split2(text, sep):
    try:
        bufor = ''
        good = []
        for i in text:
            if i != sep:
                bufor += i
            else:
                good.append(bufor)
                bufor = ''
        good.append(bufor)
        return 'The items are: ' + sep.join(good)
    except AttributeError as err:
        print('Separator nie może być liczbą.')
        print('Błąd: ', err)
print(split2(numbers, 1))