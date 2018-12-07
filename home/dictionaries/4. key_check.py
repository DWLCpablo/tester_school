d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_check(x, dict):
    if x in dict:
        return True
    return False

print(key_check(2, d))
print(key_check(8, d))

def value_check(x, dict):
    for i in dict:
        if dict[i] == x:
            return True
    return False

print(value_check(10, d))
print(value_check(1, d))