# Write a program to input the value of x and n and print the sum of the following series:

# 1) 1 + x + x^2 + x^3 + x^4 + ... x^n
# 2) 1 - x + x^2 - x^3 + x^4 - ... x^n
# 3) x - x^2/2 + x^3/3 - x^4/4 + ... x^n/n
# 4) x + x^2/2! - x^3/3! + x^4/4! - ... x^n/n!

import math

x = float(input("Enter value of x: "))
n = int(input("Enter value of n: "))
print()

# Series 1
s1 = 1
for i in range(1, n + 1):
    s1 += x**i
print("Series 1: ", s1)

# Series 2
s2 = 1
sgn = -1
for i in range(1, n + 1):
    s2 += (x**i) * sgn
    sgn *= -1
print("Series 2: ", s2)

# Series 3
s3 = 0
sgn = -1
for i in range(1, n + 1):
    s3 += ((x**i) / i) * sgn
    sgn *= -1
print("Series 3: ", s3)

# Series 4
s4 = x
sgn = 1
for i in range(2, n + 1):
    s4 += ((x**i) / math.factorial(i)) * sgn
    sgn *= -1
print("Series 4: ", s4)

"""
Output:

Enter value of x: 2
Enter value of n: 5

Series 1:  63.0
Series 2:  -21.0
Series 3:  -5.066666666666666
Series 4:  3.066666666666667

Enter value of x: 3
Enter value of n: 3

Series 1:  40.0
Series 2:  -20.0
Series 3:  -7.5
Series 4:  3.0
"""
