# Input a list of numbers and swap elements at the even location with the elements at the odd location.

val = eval(input("Enter list of numbers: "))

even = val[::2]
odd = val[1::2]

val[::2] = odd
val[1::2] = even

print("Swapped list: ", val)

"""
Output: 

Enter list of numbers: [23, 12, 90, 2, 75, 46]
Swapped list:  [12, 23, 2, 90, 46, 75]
"""
