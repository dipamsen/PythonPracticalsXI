# Input a string and determine whether it is a palindrome or not; convert the case of characters in a string

s = input("Enter a string: ")

if s.upper() == s.upper()[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

'''
Output:

Enter a string: Hello
The entered string is not a palindrome.

Enter a string: Racecar
The entered string is a palindrome.
'''
