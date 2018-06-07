N = 5
x = '*'
for i in range(N):
    print(x*i)

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    print()



