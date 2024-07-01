students = []
for i in range(5):
    student = input("Enter student name: ")
    students.append(student)

# Print the entire list in the default format with [ ] and ,
print("Student names in default format")
print(students)

# Print only the student names in separate lines
print("Student names in normal order")
for student in students:
    print(student)

# Reverse the students list in place
students.reverse()

# Print the student names in reverse order
print("Student names in reverse order")
for student in students:
    print(student)

# Access a specific student (Note that computers start counting at 0)
print("Student number 2 is: " + students[1])