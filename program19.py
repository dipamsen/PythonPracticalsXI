# Python program to print terms of Fibonacci Series Using for Loop.

n = int(input("Enter number of terms: "))

a, b = 0, 1
fib = [a, b]
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)

"""
Output:

Enter list of numbers: [1, 2, 35, 23, 20, 99]
Largest even:  20
"""
