num = int(input())
a = [[0]*num for i in range(num)]
conut1 = 0
count2 = 0
count3 = 0
for i in range(num):
  a[i] = list(map(int, input().split()))
  conut1 += a[i][0]
  count2 += a[i][1]
  count3 += a[i][2]

if conut1 == 0 and count2 == 0 and count3 == 0:
  print("YES")
else:
  print("NO")
x = 1 + 2 * 3 - 8 / 4
print(x)
import h as h
#import r as r

#
# def computepay(h,r):
#   if h <= 40:
#     Pay = h * r
#   elif h > 40:
#     Pay = 40 * r + (h-40) * r * 1.5
#   return Pay
#
# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter rate:")
# r = float(rate)
# p = computepay(h,r)
# print("Pay",p)

num = 0
largest = -1
smallest = None

while True:
    inp = int(input("Enter a number: "))
    if inp == "done" :
        break
    try:
        num = int(inp)
    except:
        print("Invalid input")

    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print ("Maximum is", largest)
print ("Minimum is", smallest)
