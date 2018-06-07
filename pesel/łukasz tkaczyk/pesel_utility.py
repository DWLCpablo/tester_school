def is_correct(pesel):
    """
    Check if pesel number is correct.
    Args:
        pesel: string to be checked.
    Returns:
        True if pesel number is correct, False otherwise.
    """

    scales = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    verify = 0
    if len(pesel) != 11:
        return False
    elif not is_only_digits(pesel):
        return False
    else:
        for scale in scales:
            for digits in pesel:
                verify += int(scale) * int(digits)
        return verify % 10 == 0


def is_only_digits(pesel):
    digits = []
    others = []
    for record in pesel:
        if record.isdigit():
            digits.append(0)
            others.append(0)
        else:
            others.append(1)
    return digits == others


def extract_personal_data(pesel):
    """
    Check the gender and the date of the owner birthday.
    Args:
        pesel: string to be checked.
    Returns:
        dictionary with keys: sex, birth_date.
    """

    personal_data = {}
    try:
        int(pesel)
        if int(pesel[9:10]) % 2 != 0:
            personal_data['sex'] = 'male'
            get_birth_date(personal_data, pesel)
        else:
            personal_data['sex'] = 'female'
            get_birth_date(personal_data, pesel)
    except ValueError as error:
        print('Podany pesel jest nieprawidłowy!')
        raise
    return personal_data


def get_birth_date(personal_data, pesel):
    """
    Get birth date from pesel number.
    Args:
        pesel: string to be checked.
    Returns:
        dictionary with key: birth_date.
    """

    if int(pesel[2]) < 2:
        personal_data['birth_date'] = pesel[4:6] + '.' + pesel[2:4] + '.19' + pesel[0:2]
    elif 1 < int(pesel[2]) < 4:
        personal_data['birth_date'] = pesel[4:6] + '.' + '0' + str(int(pesel[2:4]) - 20) + '.20' + pesel[0:2]
    elif 3 < int(pesel[2]) < 6:
        personal_data['birth_date'] = pesel[4:6] + '.' + '0' + str(int(pesel[2:4]) - 40) + '.21' + pesel[0:2]
    elif 7 < int(pesel[2]) < 10:
        personal_data['birth_date'] = pesel[4:6] + '.' + '0' + str(int(pesel[2:4]) - 80) + '.18' + pesel[0:2]
    else:
        personal_data['birth_date'] = pesel[4:6] + '.' + '0' + str(int(pesel[2:4]) - 60) + '.22' + pesel[0:2]