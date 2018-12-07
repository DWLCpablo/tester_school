dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
big = {}
for key, value in dic1.items():
    big[key] = value
for key, value in dic2.items():
    big[key] = value
for key, value in dic3.items():
    big[key] = value
print(big)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)  # dic.update() to dobry sposób na stawianie nowych/nadpisywanie starych wartości i kluczy w słowniku
print(dic4)