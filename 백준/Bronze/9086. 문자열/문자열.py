num = int(input())

for i in range(num):
    user_input = input()
    print(user_input[0], end='')
    print(user_input[len(user_input)-1])