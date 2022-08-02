list = []
for i in range(1, 31):
    list.append(i)

for i in range(28):
    num = int(input())
    list.remove(num)

for i in list:    
    print(i)