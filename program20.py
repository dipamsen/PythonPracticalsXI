# Write a program that returns the largest even number in the list of integers. If there is no even number in input, print "No even number".

val = eval(input("Enter list of numbers: "))

evens = []
for v in val:
    if v % 2 == 0:
        evens.append(v)

if len(evens) > 0:
    print("Largest even: ", max(evens))
else:
    print("No even number")
