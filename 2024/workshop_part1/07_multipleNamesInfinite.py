longestName = ""
while True:
    name = input("Enter name: ")
    if name == "exit":
        break # exit the loop
    elif len(name) > len(longestName):
        longestName = name
    print(longestName)

print(longestName + " is the longest name")