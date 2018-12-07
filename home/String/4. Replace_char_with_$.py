"""4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'"""

def replace_char(string):
    new = ''
    for char in string:
        if char == string[0]:
            char = '$'
        new += char
    return new

print(replace_char('twojastara'))


def replace_char(string):
    main = string[0]
    replaced = string.replace(main, '$')   # string.replace(character, 'x') - zastępujesz wybrany znak, innym
    return main + replaced[1:]


print(replace_char('twojastara'))