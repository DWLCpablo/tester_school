"""7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'"""

def replace(string):
    string_not = string.find('not')
    string_poor = string.find('poor')
    if string_poor > string_not:
        string = string.replace(string[string_not:(string_poor+4)], 'good')
    return string

print(replace('The lyrics is not that poor!'))

# string.find('word') zwraca index_number pod którym występuje dane słowo w stringu
