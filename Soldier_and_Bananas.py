price, cost_of_first_banana, number_of_banana = map(int, input().split())

number_of_banana = number_of_banana * (number_of_banana+1)/2

borrow_money = price*number_of_banana - cost_of_first_banana
if borrow_money <= 0:
    print("0")
else:
    print(int(borrow_money))
# taking two inputs at a time
# x, y = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)