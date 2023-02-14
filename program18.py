# Determine whether a number is a perfect number, an Armstrong number or a palindrome.

n = int(input("Enter number: "))

# Perfect Number
factors = []
for i in range(1, n):
    if n % i == 0:
        factors.append(i)
if sum(factors) == n:
    print(n, "is a perfect number.")
else:
    print(n, "is NOT a perfect number.")

# Armstrong Number
digits = list(str(n))
num_digits = len(digits)
val = 0
for d in digits:
    val += int(d) ** num_digits
if val == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is NOT an Armstrong number.")

# Palindrome number
s = str(n)
if s == s[::-1]:
    print(n, "is an Palindrome number.")
else:
    print(n, "is NOT an Palindrome number.")


"""
Output:

Enter number: 12321
12321 is NOT a perfect number.
12321 is NOT an Armstrong number.
12321 is an Palindrome number.

Enter number: 1634
1634 is NOT a perfect number.
1634 is an Armstrong number.
1634 is NOT an Palindrome number.

Enter number: 28
28 is a perfect number.
28 is NOT an Armstrong number.
28 is NOT an Palindrome number.
"""
