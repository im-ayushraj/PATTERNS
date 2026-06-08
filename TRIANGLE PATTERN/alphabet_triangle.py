# A
# AB
# ABC
# ABCD
# ABCDE

for row in range(5):
    for col in range(row + 1):
        print(chr(65 + col),end = "")
    print()