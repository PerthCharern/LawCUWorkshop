longestName = ""
for i in range(10):
    name = input("Enter name: ")
    if (name > longestName):
        longestName = name
print(longestName + " is the longest name")