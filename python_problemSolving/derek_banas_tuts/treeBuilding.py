

# program to print a tree using #
    #
   ###
  #####
 #######
#########
    #

'''

Given => length of 5
4 spaces : 1 hash
3 spaces : 3 hash
2 spaces : 5 hash
1 space : 7 hash
0 space : 9 hash

trunk => same as first => 4 spaces : 1 hash

Need to do:

1. Decrement the spaces by 1
2. Increment the spaces by 2
3. space = height - 1
4. Decrement tree height until it equals 0
5. Print spaces and then hashes for each row
6. Print spaces and then 1 hash


'''


# Get the height from the user
tree_height = input("How tall is the tree")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1
stump_spaces = tree_height - 1 # saving this for the trunk of the tree

# start the hash
hashes = 1

while tree_height != 0 :
    for i in range(spaces):
        print(' ', end="")

    for i in range(hashes):
        print("#", end="")

    # Print new line
    print()

    # Decrement spaces
    spaces -= 1

    # Increment hashes by 2
    hashes += 2

    # update the tree height
    tree_height -= 1


# printing the trunk of the tree
for i in range(stump_spaces):
    print(' ', end="")

print("#")