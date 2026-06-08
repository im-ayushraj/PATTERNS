#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


for row in range(5):
    for space in range( 5 - row - 1):
        print(" ", end="")
    for stars in range( 2 * row + 1):
            print("*",end = "")
        
    print()

for rows in range(1,5):
    for space in range(rows) :
        print(" ", end = "")
    for stars in range( 2 * (5 - rows) - 1):
        print("*",end="")
    
    print()