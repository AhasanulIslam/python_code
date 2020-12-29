import re
name = input()
if re.match(f'.*h.*e.*l.*l.*o.*', name):
    print('YES')
else:
    print('NO')