# Input three numbers and display the largest / smallest number.

num1 = int(input("Enter a number (1): "))
num2 = int(input("Enter a number (2): "))
num3 = int(input("Enter a number (3): "))

if (num1 > num2):
    if (num1 > num3):
        greatest = num1
        if (num2 > num3):
            smallest = num3
        else:
            smallest = num2
    else:
        greatest = num3
        smallest = num2
else:
    if (num2 > num3):
        greatest = num2
        if (num1 > num3):
            smallest = num3
        else:
            smallest = num1
    else:
        greatest = num3
        smallest = num1

print()
print("The largest number is: ", greatest)
print("The smallest number is:", smallest)

'''
Output:

Enter a number (1): 15
Enter a number (2): 29
Enter a number (3): 82

The largest number is:  82
The smallest number is: 15

'''
