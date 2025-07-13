longestName = ""
for i in range(10):
    name = input("Enter name: ")
    if len(name) > len(longestName):
        longestName = name
print(longestName + " is the longest name")