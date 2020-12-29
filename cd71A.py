int_input = int(input())

for new in range(0, int_input):
      sting_input = str(input())
      length = len(sting_input)
      if (length > 10):
            print(f'{sting_input[0]}{length-2}{sting_input[length-1]}')
      else:
            print(sting_input)

