# napisz program, który tworzy odwrócony słownik podanego słownika (zamienia wartości i klucze kolejnością)

slownik = {'pablo': 'tak se', 'łukasz': 'ok', 'kornel': 'tak se'}
rev_slownik = {}

for name, mark in slownik.items():
    if mark not in rev_slownik:
        rev_slownik[mark] = [name]
    else:
        rev_slownik[mark].append(name)

print(rev_slownik)

