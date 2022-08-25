num = int(input())

numlist = list(map(int, input().split()))

max = numlist[0]
min = numlist[0]

for i in numlist[1:]:
    if max < i:
        max = i
    elif min > i:
        min = i
        
print(min, max)