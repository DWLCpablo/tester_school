import peseltools


pesel = input('Podaj 11-cyfrowy numer PESEL: ')
print(peseltools.validate(pesel))
print(peseltools.extract_personal_data(pesel))
