import string


def pangram(text):
    dic = {}
    for char in text.lower():
        if char.isalpha():
            dic[char] = 0
    print(dic)
    if len(dic) == len(string.ascii_lowercase):
        return (text + ' is a pangram.')
    else:
        return (text + ' is not a pangram.')

print(string.ascii_lowercase)
def is_pangram2(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha():
            found_letters[char] = 0
    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False

print(pangram('The quick brown fox jumps over the lazy dog'))
print(pangram('fghjkjhfbvbnmnjnvg'))