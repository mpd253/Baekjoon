num = int(input())

for i in range(num):
    for j in range(num):
        if j <= i:
            print('*', end='')
    print()