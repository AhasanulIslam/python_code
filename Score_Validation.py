# count1 = 0
# count2 = 0
# count3 = 0
# while(True):
#     input1 = float(input())
#     if count3 == 1:
#         if input1 == 2:
#             break
#         elif input1 == 1:
#             count3 = 0
#             continue
#         else:
#             print("novo calculo (1-sim 2-nao)")
#             continue
#     else:
#         if input1 < 0 or input1 > 10:
#             print("nota invalida")
#         elif count2 == 0:
#             count1 = input1
#             count2 = 1
#         else:
#             print(f"media {(input1+count1)/2.00}")
#             count2 = 0
#             count3 = 1
#
#     if count3 == 1:
#         print("novo calculo (1-sim 2-nao)")
# n= int(input("enter the no.: "))
# for i in range(1,n):
#  for j in range(1,n-i):
#   print(j,end="")
#  print()
a, b, c = map(int, input().split())
print(f"{a} {b} {c}")