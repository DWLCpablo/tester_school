
#suma liczb parzystych
suma = 0
for i in range(0, 101, 2):
    suma += i
print(suma)

#inny sposób (liczby nieparzyste), solo
suma = 0
for i in range(101):
    if i % 2 != 0:
        suma += i
print(suma)
suma = 0
