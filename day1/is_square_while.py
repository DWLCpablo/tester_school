
n = 68
i = 0
square = False
done = False
current = i ** 0

while i ** 2 <= n:
    if i ** 2 == n:
        square = True
        done = True
    elif i ** 2 > n:
        done = True
    i += 1
if square:
    print ('n jest kwadratem')
else:
    print('n nie jest kwadratem')