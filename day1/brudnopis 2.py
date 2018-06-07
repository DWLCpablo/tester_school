year = '09'
year = int(year) + 1900
leap_year = None
if (year % 4 == 0 and year %100 != 0) or year % 400 == 0:
    leap_year = True
else:
    leap_year = False
print(leap_year)