marks = {'John': 5.0, 'Sue': 3.0}
print(marks['John']) #odwołanie do wartości
marks['Sue'] = 4.0 # zmiana wartości
marks['Anne'] = 3.0 #dodawanie nieistniejących wpisów
print(marks)

for key in marks:
    print(key, marks[key])

for name, mark in marks.items(): #iterowanie po kluczach i wartościach
    print(name, mark)

for mark in marks.items(): #iterowanie po wartościach
    print(mark)