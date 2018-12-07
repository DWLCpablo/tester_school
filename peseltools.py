def validate(pesel):
    """
    validate(pesel) - checks whether input PESEL is valid or not.
            Args:
                pesel
            Returns:
                True - if valid
                or
                False - if not valid
    """

    pesel = str(pesel)
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if len(pesel) != 11:
        return False
    check_list = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    check_sum = 0
    for idx, value in enumerate(check_list):
        check_sum += value * (int(pesel[idx]))
    if pesel[-1] != str(check_sum)[-1]:
        return False
    if pesel[2] == '0' or pesel[2] == '1':  # dla urodzonych w 1900-1999
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
    elif month[0] == '2' or month[0] == '3':  # dla urodzonych w 2000-2099
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
    elif month[0] == '8' or month[0] == '9':  # dla urodzonych w 1800-1899
        year = int(year) + 1800
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == '82' and (int(day) > 29 or int(day) <= 0):
                return False
            elif month != '82' and (month_lengths[(int(month) - 81)] < int(day) or int(day) <= 0):
                return False
        elif not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if month == '82' and (int(day) > 28 or int(day) <= 0):
                return False
            elif month != '82' and (month_lengths[(int(month) - 81)] < int(day) or int(day) <= 0):
                return False
    elif month[0] == '4' or month[0] == '5':  # dla urodzonych w 2100-2199
        year = int(year) + 2100
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == '42' and (int(day) > 29 or int(day) <= 0):
                return False
            elif month != '42' and (month_lengths[(int(month) - 41)] < int(day) or int(day) <= 0):
                return False
        elif not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if month == '42' and (int(day) > 28 or int(day) <= 0):
                return False
            elif month != '42' and (month_lengths[(int(month) - 41)] < int(day) or int(day) <= 0):
                return False
    elif month[0] == '6' or month[0] == '7':   # dla urodzonych w 2200-2299
        year = int(year) + 2200
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == '62' and (int(day) > 29 or int(day) <= 0):
                return False
            elif month != '62' and (month_lengths[(int(month) - 61)] < int(day) or int(day) <= 0):
                return False
        elif not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if month == '62' and (int(day) > 28 or int(day) <= 0):
                return False
            elif month != '62' and (month_lengths[(int(month) - 61)] < int(day) or int(day) <= 0):
                return False
    return True


def extract_personal_data(pesel):
    """
    extract_personal_data(pesel) - uses validate(pesel) to confirm validity of PESEL,
                and if so returns a dictionary containing date of birth and sex stored inside PESEL.
                If PESEL not valid, returns ValueError.
            Args:
                pesel
            Returns:
                dictionary with data
                or
                ValueError
    """

    if validate(pesel) is False:
        raise ValueError('Numer PESEL nie jest poprawny.')
    pesel = str(pesel)
    personal_data = {'birth_date': None, 'sex': None}
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    if month[0] == '0' or month[0] == '1':
        personal_data['birth_date'] = str(day + '/' + month + '/19' + year)
    elif month[0] == '2':
        personal_data['birth_date'] = str(day + '/' + '0' + str((int(month) - 20)) + '/20' + year)
    elif month[0] == '3':
        personal_data['birth_date'] = str(day + '/' + str((int(month) - 20)) + '/20' + year)
    elif month[0] == '4':
        personal_data['birth_date'] = str(day + '/' + '0' + str((int(month) - 40)) + '/21' + year)
    elif month[0] == '5':
        personal_data['birth_date'] = str(day + '/' + str((int(month) - 40)) + '/21' + year)
    elif month[0] == '6':
        personal_data['birth_date'] = str(day + '/' + '0' + str((int(month) - 60)) + '/22' + year)
    elif month[0] == '7':
        personal_data['birth_date'] = str(day + '/' + str((int(month) - 60)) + '/22' + year)
    elif month[0] == '8':
        personal_data['birth_date'] = str(day + '/' + '0' + str((int(month) - 80)) + '/18' + year)
    elif month[0] == '9':
        personal_data['birth_date'] = str(day + '/' + str((int(month) - 80)) + '/18' + year)
    if int(pesel[-2]) % 2 == 0:
        personal_data['sex'] = 'Female'
    else:
        personal_data['sex'] = 'Male'
    return personal_data
