b = float(input())
a = float(input())
c = float(input())
delta = b ** 2 - 4 * a * c
print (delta)

if delta < 0:
    print ('non possumus')
if delta == 0:
    print (-b / (2 * a))
else:
    print ((-b + (delta ** 0.5) / 2 * a), (-b + (delta ** 0.5) / 2 * a))