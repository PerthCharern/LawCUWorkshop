# Write a program that takes 10 names as input and returns the average length of the names as output.

totalLength = 0
for i in range(10):
    name = input("Enter name: ")
    totalLength = totalLength + len(name)
print(totalLength / 10)