# *********
#  *******
#   *****
#    ***
#     *

# formula = 2 * (n - row ) - 1
for rows in range(5):
    for space in range(rows) :
        print(" ", end = "")
    for stars in range( 2 * (5 - rows) - 1):
        print("*",end="")
    
    print()