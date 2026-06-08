# A
# B C
# D E F
# G H I J
# K L M N O

ch = 65
for row in range(5):
    for col in range( row + 1):
        print(chr(ch),end="")
        ch+=1
    print()
