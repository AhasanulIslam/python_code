

n = int(input())
a = []
sum = 0
ans = 0
count = 1

for i in range(n):
    a[i] = map(int, input().split())
b = [a, a+n]
b.sort()
for i in range(0, i):
    sum += a[i]
sum = sum/2
while(ans<=sum):
    count += 1
    ans += a[n - count]
print(count)