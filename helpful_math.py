num = input()
first = 0
second = 0
third = 0
for i in range(0, len(num)):
    if num[i] == '1':
        first += 1
    elif num[i] == '2':
        second += 1
    elif num[i] == '3':
        third += 1

x = "1+"*first + "2+"*second + "3+"*third
print(x[:-1])