
a = [[0]*5 for i in range(5)]
# '''
# for i in range(5):
#      for j in range(5):
#          a[i][j] = int(input())
# '''
for i in range(5):
  a[i] = list(map(int, input().split()))

for i in range(5):
    for j in  range(5):
        if a[i][j] == 1:
            x = i+1
            y = j+1
n = abs(x-3) + abs(y-3)
print(n)