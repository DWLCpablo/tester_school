

x = 10
y = 12
z = 10

if (x <= y) and (y <= z) or z <= y <= x:
    print ('Mediana to y')
elif y<= x <= z or z <= x <= y:
    print ('Mediana to x')
else:
    print ('Mediana to z')