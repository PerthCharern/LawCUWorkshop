persons = []
for i in range(10):
    person = input("Enter name: ")
    persons.append(person)
print(persons)

persons.reverse()

for person in persons:
    print(person)