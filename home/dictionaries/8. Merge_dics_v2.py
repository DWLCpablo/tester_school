'''8. Write a Python script to merge two Python dictionaries. Go to the editor
Click me to see the sample solution'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}

def merge_dics(a, b):
    target = {}
    for i in (a, b):
        target.update(i)
    return target

print(merge_dics(dic1, dic2))