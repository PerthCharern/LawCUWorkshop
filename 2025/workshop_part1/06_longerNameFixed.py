person1 = input("Input name: ")
person2 = input("Input another name: ")
if len(person1) > len(person2):
    print("The name " + person1 + " is longer.")
elif len(person2) > len(person1):
    print("The name " + person2 + " is longer.")
else:
    print("The two names are equally long.")
