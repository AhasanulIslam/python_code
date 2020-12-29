# print("Ahasanul Islam")
# print('O----')
# print(' ||||')
# print('*' * 10)
#
# price = 10
# price = 20
# price = 2.3
# is_true = True
#print(price)
#print(is_true)

# input
# input = input("What is your name? ")
# print("Hi " + input )

# name = input("What's your name? ")
# color = input("What's your favourit color? ")
#print("My name is  Mosh " + name + ' ' +  color)

# typecast
# birth_year = input("Give your birth_date = ")
#print(type(birth_year))  #any type of input python underestand as string
# age = 2019 - int(birth_year)
#print(type(age))
#print(age)

# weight_lbs = input("input your weight = ")
# weight_lbs = int(weight_lbs) * .45
# print(weight_lbs)

#string
#
# msg = 'Institute of Information Tecnology'
#
# print(msg[:])

#first = "Jhon"
#last = "Smit"
#msg = f'{first} [{last}] a coder'
#print(msg)
#len(), uppor(), lower(), find(), in, **=power
# price = 1000000
# is_ture = True
# if is_ture:
#     down_prement = .1 * price
#
# else:
#     down_prement = .2 * price
# print(f"down prement is: {down_prement}")
# from enum import Enum
#
#
# class Color(Enum):
#     red = 1
#     green = 2
#     yello = 3
#
# print(Color.red)
# print(Color(1))
# print(Color['red'])
#
# for c in Color:
#     print(c)
import datetime

# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)
# print(today)
# print(yesterday)
# print(tomorrow)
from _ast import For
#
# for i in range(5):
#    for j in range(5):
#        print(list[i][j], end="\t")
#     print()
# arr2d = [[j for j in input().strip()] for i in range(n)]
# no_of_rows = 5
# matrix = [input().split() for i in range(no_of_rows)]
# print(matrix)
#a=[[0]*5 for i in range(5)]
# a = [[0]*3 for i in range(3)]
#
# #input
# for i in range(3):
#   for j in range(3):
#     a[i][j] = int(input())
#
# #output
# for i in range(3):
#   for j in range(3):
#     print(a[i][j], end=" ")
#   print('\n')
# arr = [[] for i in range(5)]
#
# for i in range(5):
#   arr[i] = list(map(int, input().split())) #input a row in a line like: 1 2 3
#   if arr[i] == 1:
#      int = x
#      x = abs(i-3)
#
# print(x)


# for i in range(3):
# #   for j in range(3):
# #     if arr[i] == 1:
# #       x = abs(i-3) + abs(j-3)
# # print(x)
#output
# for i in range(3):
#   for j in range(3):
#     print(arr[i][j], end=" ")
#   print()
# import a
# a=a[[0]*5 for i in range(5)]
#
# for i in range(5):
#      for j in range(5):
#          a[i][j] = int(input())
# for i in range(5):
#     for j in  range(5):
#         if a[i][j] == 1:
#             x = i+1
#             y = j+1
# n = abs(x-3) + abs(y-3)
# print(n)
#

# a = [[0]*5 for i in range(5)]
# '''
# for i in range(5):
#      for j in range(5):
#          a[i][j] = int(input())
# '''
# # for i in range(5):
#   a[i] = list(map(int, input().split()))
#
# for i in range(5):
#     for j in  range(5):
#         if a[i][j] == 1:
#             x = i+1
#             y = j+1
# n = abs(x-3) + abs(y-3)
# print(n a[i] = list(map(int, input().split())))
# for i in range(5):
#     a[i] = list(map(int, input().split()))
#
#     if 1 in a[i]:
#         x = a[i].index(1)
#         print(x)
# for lett in 'banana':
#     print(lett)
# from array import array
#
# vals = array('i', [3, 2, 5, 7, 2])
#
# newarr = array(vals.typecode, (a*a for a in vals))
#
# for i in newarr:
#     print(i)
# from array import array
#
# valu = array('i', [])
# n = int(input())
#
# for i in range(n):
#     x = int(input())
#     valu.append(x)
# print(valu)
a = 'dghdhdrst'
print(a[0:-])