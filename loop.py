# command = ""
# started = False
# while command != "quit":
#         command = input("> ").lower()
#         if command == "start":
#             if started == True:
#                  print("car already started...")
#             else:
#                 started = True
#                 print("car start...")
#         elif command == "stop":
#             if not started:
#                 print("car already stopped..")
#             else:
#                 started  = False
#             print("car stopped")
#         elif command == "help":
#             print("""
#             start- start the car
#             stop- stop the car
#             quit- to quit
#             """
#             )
#         elif command == "quit":
#             print("stopped")
#             break
#
# for item in range(0,5):
#           print(item)
# news = [13, 43, 23]
# total = 0
# for new in news:
#   total += new
# print(f"total price: {total}")
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")
# numbers = [5, 4, 3 , 2, 1]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += "x"
#     print(output)
# numbers = [3, 4, 5, 2, 6]
# numbers.append(20)
# print(numbers)
# numbers.insert(3, 10)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# # numbers.clear()
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# def getting(name):
#     print(f"good morning {name}")
#     print("hi buddy")
#
#
# getting("Ahsan")
from pip._vendor.distlib.compat import raw_input

n = raw_input()
print(n)