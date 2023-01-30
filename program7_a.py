# Compute the greatest common divisor and least common multiple of two integers.

# Program A: (using math module)

import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = math.gcd(num1, num2)
lcm = math.lcm(num1, num2)

print("HCF of the two numbers is " + str(hcf))
print("LCM of the two numbers is " + str(lcm))

'''
Output:

Enter first number: 35
Enter second number: 25
HCF of the two numbers is 5
LCM of the two numbers is 175

Enter first number: 1232
Enter second number: 2912
HCF of the two numbers is 112
LCM of the two numbers is 32032
'''
