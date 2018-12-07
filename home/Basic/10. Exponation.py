'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615'''
import math
num = float(input('Give a number: '))
print('Your number raised to quadrant is ', num**2)
print('Your number raised to cube is ', num**3)
print('The sum of your number, its quadrant and cube is ', num + num**2 + num**3)

num = float(input('Give a number: '))
quad = num **2
cube = num **3
numbers = [num, quad, cube]
print('The sum is', sum(numbers))
