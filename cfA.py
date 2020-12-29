height, weigth, block = map(int, input().split())
if height%block==0:
        height_block = height//block
else:
        height_block = height//block+1

if weigth % block == 0:
        weigth_block = weigth // block
else:
        weigth_block = weigth // block+1
print(height_block * weigth_block)