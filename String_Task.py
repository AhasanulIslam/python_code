name = str(input()).lower()
count = ""
word = ['a', 'o', 'i', 'e', 'u', 'y']
for i in range(0, len(name)):
    if name[i] not in word:
        count+= '.'
        count += name[i]
print(count)


