
#dupa

def validate(pesel):
    pesel = str(pesel)
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if len(str(pesel)) != 11:
        return False
    checksum = str(9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + int(pesel[3]) + 9 * int(pesel[4]) + 7 * int(
        pesel[5]) + 3 * int(pesel[6]) + int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(pesel[9]))
    if pesel[-1] != checksum[-1]:
        return False
    if pesel[2] == '0' or pesel[2] == '1':  # dla lat 1900-1999
        year = int(year) + 1900
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == '02' and (int(day) > 29 or int(day) <= 0):
                return False
            elif month != '02' and (month_lengths[(int(month) - 1)] < int(day) or int(day) <= 0):
                return False
        elif not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if month == '02' and (int(day) > 28 or int(day) <= 0):
                return False
            elif month != '02' and (month_lengths[(int(month) - 1)] < int(day) or int(day) <= 0):
                return False
    elif month[0] == '2' or month[0] == '3':  # dla lat 2000-2099
        year = int(year) + 2000
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == '22' and (int(day) > 29 or int(day) <= 0):
                return False
            elif month != '22' and (month_lengths[(int(month) - 21)] < int(day) or int(day) <= 0):
                return False
        elif not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if month == '22' and (int(day) > 28 or int(day) <= 0):
                return False
            elif month != '22' and (month_lengths[(int(month) - 21)] < int(day) or int(day) <= 0):
                return False
    return True

pes1 = '21302116275' #nie-przestępny 21.10.2021 TRUE
pes2 = '01222886498' # nie-przestępny 28.02.2001 TRUE
pes3 = '00022897147' #nie-przestępny 28.02.1900  TRUE
pes4 = '51101611772' # nie-przestępny 16.10.1951 TRUE
pes5= '67062916429' # nie-przestępny 29.06.1967 TRUE
pes60 = '96022912414' #przestępny 29.02.1996 FALSE
pes61 = '80050333611' #przestępny 03.05.1980 TRUE
pes6 = '36290929637' #przestępny 9.09.2036 TRUE
pes7 = '04022932491' #przestępny 29.02.1904 FAlSE
pes8 = '00222977748' #przestępny 29.02.2000 FALSE
pes9 = '16222918957' #przestępny 29.02.2016 FALSE
print(validate(pes60))
