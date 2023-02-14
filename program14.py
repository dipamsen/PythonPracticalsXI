# Input a list/tuple of elements, search for a given element in the list/tuple.

elts = eval(input("Enter collection of elements: "))

e = eval(input("Enter element to search for: "))

for i in range(len(elts)):
    if e == elts[i]:
        print("Found element", e, "at index", i)
        break
else:
    print("Not found element", e, "in collection.")


"""
Output:

Enter collection of elements: 23, 248, 129, 40, 2, 4, 22
Enter element to search for: 4
Found element 4 at index 5

Enter collection of elements: 23, 248, 129, 40, 2, 4, 22
Enter element to search for: 90
Not found element 90 in collection.
"""
