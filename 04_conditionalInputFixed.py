person1 = input("Input name: ")
person2 = input("Input another name: ")
if (len(person1) > len(person2)):
    print(person1 + " is longer than " + person2)
elif (len(person1) == len(person2)):
    print(person1 + " is as long as " + person2)
else:
    print(person2 + " is longer than " + person1)