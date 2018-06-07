# program który porównuje czy dwa słowa są anagramami - czy zawierają takie same znaki

# boss
def anagrams(first, second):
    dic1 = {}
    dic2 = {}
    for char in first.lower():
        dic1[char] = dic1.get(char, 0) + 1
    for char in second.lower():
        dic2[char] = dic2.get(char, 0) + 1
    if dic1 == dic2:
        return first, 'and', second, 'are anagrams.'
    else:
        return first, 'and', second, 'are not anagrams.'



print(anagrams('older and wiser', 'I learned words'))
