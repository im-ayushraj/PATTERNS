# 1
# 12
# 123
# 1234
# 12345

for row in range(5):
    for col in range(row + 1):
        print(col + 1,end="")
    print()
    