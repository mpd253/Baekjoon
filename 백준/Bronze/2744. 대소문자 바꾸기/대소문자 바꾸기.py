li = list(input())

for i in range(len(li)):
    if li[i].isupper():
        li[i] = li[i].lower()
    else:
        li[i] = li[i].upper()

str = "".join(li)
print(str)