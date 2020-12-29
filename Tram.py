# sum = 0
# count = 0
#
# num = int(input())
# for i in range(num):
#     enter, exit = map(int, input().split())
#     sum = (enter + count) - exit
#     if sum < 0:
#         count = 0
#     else:
#         count = sum
# print(count)
# n = int(input())
# for i in range(2, n):
#
#     if n % i == 0:
#         o = 1
#         for j in range(2, i//2+1):
#             if i % j == 0:
#                 o = 0
#                 break
#         if o == 1:
#             print(i)

####
#include <stdio.h>
#
# int main()
# {
#     int i, j, num, isPrime;
#
#     /* Input a number from user */
#     printf("Enter any number to print Prime factors: ");
#     scanf("%d", &num);
#
#     printf("All Prime Factors of %d are: \n", num);
#
#     /* Find all Prime factors */
#     for(i=2; i<=num; i++)
#     {
#         /* Check 'i' for factor of num */
#         if(num%i==0)
#         {
#             /* Check 'i' for Prime */
#             isPrime = 1;
#             for(j=2; j<=i/2; j++)
#             {
#                 if(i%j==0)
#                 {
#                     isPrime = 0;
#                     break;
#                 }
#             }
#
#             /* If 'i' is Prime number and factor of num */
#             if(isPrime==1)
#             {
#                 printf("%d, ", i);
#             }
#         }
#     }
#
#     return 0;
# }
#
# num = int(input("ENTER A NUMBER : "))
# for i in range(2,num + 1):
#     if(num % i == 0):
#         prime = True
#         for j in range(2,(i//2 + 1)):
#             if(i % j == 0):
#                 prime = False
#                 break
#         if(prime):
#             print("%d"%i,end=' ')
# print("ARE THE PRIME FACTORS OF NUMBER",num)
X = 0
c = 0
while X != 2:
    m = 0
    if c != 1:
        a = input()
        a = float(a)
    z = a
    c = 0
    if z >= 0.0 and z <= 10.0:
        b = input()
        b = float(b)
        if b >= 0.0 and b <= 10.0:
            m = (z + b) / 2.0
            print("media = %.2f" % m)
            print("novo calculo (1-sim 2-nao)")
            X = int(input())
        elif b < 0.0 and b > 10.0:
            print("nota invalida")
            c = 1
    elif z < 0.0 or z > 10.0:
        print("nota invalida")
    while X < 1 and X > 2:
        print("novo calculo (1-sim 2-nao)")
        X = int(input())