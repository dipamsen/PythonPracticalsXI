# Count and display the number of vowels, consonants, uppercase, lowercase characters in string.

string = input("Enter a string: ")

lower = 0
upper = 0
vowel = 0
consonant = 0

vowels = "aeiou"

for char in string:
    if not char.isalpha():
        continue

    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1

    if char.lower() in vowels:
        vowel += 1
    else:
        consonant += 1

print()
print("===========================")
print("Number of vowels     = ", vowel)
print("Number of consonants = ", consonant)

print("Number of uppercase  = ", upper)
print("Number of lowercase  = ", lower)
print("===========================")

'''
Output:

Enter a string: Hello, World!

===========================
Number of vowels     =  3
Number of consonants =  7
Number of uppercase  =  2
Number of lowercase  =  8
===========================
'''
