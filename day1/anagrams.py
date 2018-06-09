# program który porównuje czy dwa słowa są anagramami - czy zawierają takie same znaki

# boss

def are_anagrams(first, second):
    hist1 = {}
    hist2 = {}
    for char in first:
        hist1[char] = hist1.get(char ,0) + 1
    for char in second:
        hist2[char] = hist2.get(char, 0) + 1
    return hist1 == hist2

print(are_anagrams('first', 'second'))
