
from math import pi
r = float(input('Please give number: '))
if r <= 0:
    raise ValueError('Positive eejit!')
area = pi * r ** 2
print('Area of cricle of radius ' + str(r) + ' is ' + str(area))