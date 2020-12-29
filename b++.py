num = int(input())
count = 0
for i in range(0, num):
    str_name = input()
    if str_name[1] == "+":
        count += 1
    else:
        count -= 1
print(count)