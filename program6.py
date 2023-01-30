# Write a program to input a number and check if the number is a prime number or not.

import math

num = int(input("Enter any number: "))

# First check divisibility by 2.
if (num % 2 == 0):
    print("The number is not prime. (Divisible by 2)")
else:
    is_prime = True
    # start from 3, go upto num, and check divisibility
    # (skip even numbers because num is already not divisible by 2.)
    for i in range(3, num, 2):
        if num % i == 0:
            is_prime = False
            least_div = i
            break

    if (is_prime):
        print("The number is prime.")
    else:
        print("The number is not prime. (Divisible by " + str(least_div) + ")")


'''
Output:

Enter any number: 1022347
The number is not prime. (Divisible by 37)

Enter any number: 234567
The number is not prime. (Divisible by 3)

Enter any number: 7919  
The number is prime.

'''
