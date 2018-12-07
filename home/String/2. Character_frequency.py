'''. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''

def char_freq(string):
    dic = {}
    for char in string:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

print(char_freq('pablonajlepszy'))
sum = 0
for i in char_freq('pablonajlepszy'):
    sum += char_freq('pablonajlepszy')[i]
print(sum)
print(len('pablonajlepszy'))
