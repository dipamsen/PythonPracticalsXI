# Generate the following patterns using nested loop.

# Pattern 1:      Pattern 2:        Pattern 3:
# *               1 2 3 4 5         A
# * *             1 2 3 4           AB
# * * *           1 2 3             ABC
# * * * *         1 2               ABCD
# * * * * *       1                 ABCDE

# Pattern 1:
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print(end="\n")

print()

# Pattern 2:
for i in range(5, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print(end="\n")

print()

# Pattern 3:
letters = "ABCDE"
for i in range(5):
    for j in range(i+1):
        print(letters[j], end="")
    print(end="\n")

'''
Output:

* 
* * 
* * *
* * * *
* * * * *

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

A
AB
ABC
ABCD
ABCDE
'''
