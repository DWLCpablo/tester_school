import string


def is_pangram(text):
    text = text.lower()
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
    return True

print(is_pangram('jghjhklghbouy23232ghjkSSSSghj'))
pang = 'The quick brown fox jumps over the lazy dog'
not_pang = 'Oko'
print(is_pangram(pang))
print(is_pangram(not_pang))

#ze słownikiem (trudne)
def is_pangram2(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha():
            found_letters[char] = 0
    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False
print(is_pangram2(pang))
print(is_pangram2(not_pang))
