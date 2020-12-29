

num = int(input())
str = input()
count = 0
for i in range(num-1):

     if str[i] == str[i+1]:
         count += 1
print(count)

