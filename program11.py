# Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have scored marks above 75.

students = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    print()
    r_no = int(input("Enter roll no: "))
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[r_no] = (name, marks)
print()

print("Students with marks above 75:")
for r in students:
    name, mks = students[r]

    if mks > 75:
        print(name, "(" + str(mks) + ")")

'''
Output:

Enter the number of students: 4

Enter roll no: 1
Enter student name: Pradip
Enter marks: 76

Enter roll no: 2
Enter student name: Rahul
Enter marks: 98

Enter roll no: 3
Enter student name: Soham
Enter marks: 58

Enter roll no: 4
Enter student name: Harsh
Enter marks: 81

Students with marks above 75:
Pradip (76.0)
Rahul (98.0)
Harsh (81.0)
'''
