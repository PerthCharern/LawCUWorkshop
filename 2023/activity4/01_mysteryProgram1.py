# What does this program do?

studentInfo = {}

while True:
    name = input("Enter name: ")
    school = input("Enter school: ")
    if name == "exit" or school == "exit":
        break;
    
    if (school not in studentInfo):
        studentInfo[school] = []
    
    studentInfo[school].append(name)

print(studentInfo)
    