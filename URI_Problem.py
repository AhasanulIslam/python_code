
while True:
  salary = float(input())
  if (salary <= 400.00):
    count = salary * .15
    total = salary + count
    per = 15
  elif (salary >= 400.00 and salary <= 800):
    count = salary * .12
    total = salary + count
    per = 12
  elif (salary >= 800.01 and salary <= 1200 ):
    count = salary * .10
    total = salary + count
    per = 10
  elif(salary >= 1200.01 and salary <= 2000):
    count = salary * .07
    total = salary + count
    per = 7
  elif(salary >= 2000.01):
    count = salary * .04
    total = salary + count
    per = 4


  print(f"Novo salario: {round(total, 2)}")
  print(f"Reajuste ganho: {round(count, 2)}")
  print(f"Em percentual: {per}%")