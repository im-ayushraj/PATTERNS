#     *
#    ***
#   *****
#  *******
# *********

# formula
# 2 * row + 1
# n - row - 1
# for n = 5
#  5 - row - 1
for row in range(5):
    for space in range( 5 - row - 1):
        print(" ", end="")
    for stars in range( 2 * row + 1):
            print("*",end = "")
        
    print()

