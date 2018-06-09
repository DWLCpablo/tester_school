import pesel_utility

""""
Given:
    the application retrieves the user's pesel number.
When:
    the application checks if pesel is correct.
Then:
    the application returns dictionary with users gender and date of birth.
"""

check = pesel_utility
pesel = input('Proszę podać numer pesel: ')

print(check.is_correct(pesel))
print(check.extract_personal_data(pesel))