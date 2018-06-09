marks = {'John': 5.0, 'Sue': 3.0}
marks['Sue'] = 4.0 # zmiana wartości
marks['Anne'] = 3.0 #dodawanie nieistniejących wpisów
print(marks)
print()
for key in marks: #iterowanie po kluczach z wypisaniem kluczy i wartości
    print(key, marks[key])
print()
for name, mark in marks.items(): #iterowanie po kluczach i wartościach
    print(name, mark)
print()
for mark in marks.items(): #iterowanie po wartościach
    print(mark)
print()
for value in marks.items(): #iterowanie po wartościach
    print(value)