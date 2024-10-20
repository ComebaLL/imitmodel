mask = 0b00000000

for i in range(7, -1, -1):
    if 114 & mask == 64:
        print(mask)
    print(mask)
    
    mask |= 1 << i