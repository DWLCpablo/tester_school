import json
#policz średnią wzrostów i średnią wzrostów ludzi o tym samym imieniu
#boss
data = [{'first_name': 'John', 'last_name': 'Doe', 'height': 173},
        {'first_name': 'James', 'last_name': 'Kovalsky', 'height': 183},
        {'first_name': 'John', 'last_name': 'Smith', 'height': 165},
        {'first_name': 'Anne', 'last_name': 'Novak', 'height': 170}]
total = 0
avg = 0

for item in data:
    total += item['height']
print('Średnia wzrostu: ', total // len(data))

new = {}
for item in data:
    if item['first_name'] in new:
        new[item['first_name']].append(item['height'])
    else:
        new[item['first_name']] = [item['height']]
print(new)

for key, value in new.items():
    print(key, sum(new[key]) / len(new[key]))


total_by_name = {}
count_by_name = {}
result = []
for item in data:
    first_name = item['first_name']
    total_by_name[first_name] = total_by_name.get(first_name, 0) + item['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1
print(total_by_name)
print(count_by_name)
for key, value in total_by_name.items():
    result += key + ':', value / count_by_name[key]
print(result)
result_dic = {}
for key, value in total_by_name.items():
    result_dic[key] = total_by_name[key] / count_by_name[key]
print(result_dic)


with open('heights.txt', 'wt') as my_file:
    my_file.write('Average heights are: ' + str(result_dic))

with open('heights.json', 'wt') as my_file:
    my_file.write(json.dumps(result_dic))

with open('heights.json', 'r') as my_file:
    my_file.read(json.loads(my_file))