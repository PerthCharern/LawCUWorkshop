longestName = ""
while True:
    name = input("Enter name: ")
    if (name == "exit"):
        break;
    elif (len(name) > len(longestName)):
        longestName = name

print(longestName + " is the longest name")