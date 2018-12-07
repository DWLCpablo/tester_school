"""7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java"""

file = str(input('Give full file name: '))
elements = file.split('.')
print(elements[len(elements) - 1])
print(elements[-1]) 