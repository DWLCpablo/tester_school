pesel = '85021312554'
scales1 = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
scales2 = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
verify1 = 0
verify2 = 0
for scale in scales1:
    for digits[scale] in pesel:
        verify1 += int(scale) * int(digits)

for scale in scales2:
    for digits in pesel:
        verify2 += int(scale) * int(digits)
print(verify1)