# napisać program obliczający silnię
# boss

def factorial(n):
    if n < 0:
        raise ValueError('Silnia nie może być podana dla liczby ujemnej')
    result = 1
    for i in range (1, n+1):
        result *= i
    return result


print(factorial(-1))