num = int(input())
count = 0
for i in range(0, num):
    participant = input()
    if participant.count('1') >= 2:
        count = count+1
print(count)