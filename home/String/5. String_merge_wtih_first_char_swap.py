"""5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

def swap(string1, string2):
    result = ''
    new1 = string1[0:2] + string2[2:]
    new2 = string2[0:2] + string1[2:]
    for char in new2:
        result += char
    result += ' '
    for char in new1:
        result += char
    return result

print(swap('pablo', 'ciula'))

def char_mix(string1, string2):
    new1 = string1[0:2] + string2[2:]
    new2 = string2[0:2] + string1[2:]
    return new2 + ' ' + new1

print(char_mix('pablo', 'ciula'))