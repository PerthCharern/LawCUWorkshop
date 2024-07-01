#01 Student Count
print(len(students))

#02 Find someone with the same year of birth
for student in students:
    if student["yearOfBirth"] == me["yearOfBirth"]:
        print(student["name"], student["yearOfBirth"])
    
#03 Find someone with the same city of birth
for student in students:
    if student["cityOfBirth"] == me["cityOfBirth"]:
        print(student["name"], student["cityOfBirth"])

#04 Find a staff member with month of birth within +/- one range
for staffMember in staffMembers:
    if staffMember["monthOfBirth"] == me["monthOfBirth"] or staffMember["monthOfBirth"] == me["monthOfBirth"] + 1 or staffMember["monthOfBirth"] == me["monthOfBirth"] - 1:
        print(staffMember["name"], staffMember["monthOfBirth"])

#05 Find a student who went to a school with a longer name than yours
for student in students:
    if len(student["school"]) > len(me["school"]):
        print(student["name"], student["school"], len(student["school"])) 

#06 Find the number of students who is born at least 2 years before you
count = 0
for student in students:
    if student["yearOfBirth"] >= me["yearOfBirth"] + 2:
        count = count + 1
print(count)

#07 Find a student who has been to more than 10 countries
for student in students:
    if len(student["countriesVisited"]) > 10:
        print(student["name"], len(student["countriesVisited"])

#08 Find a student who has been to more thai provinces that you have
for student in students:
    if len(student["thaiProvincesVisited"]) > len(me["thaiProvincesVisited"]):
        print(student["name"], len(student["thaiProvincesVisited"]))

#09 Find a student whose previous school country is not Thailand
for student in students:
    if student["schoolCountry"] != "Thailand":
        print(student["name"], student["school"])

#10 Find a student who likes at least one singer as you also like
for student in students:
    for singer1 in student["favoriteSingers"]:
        for singer2 in me["favoriteSingers"]:
            if singer1 == signer2:
                print (student["name"], singer1)

#11 Find a student who likes at least one favorite hobby as you also like
for student in students:
    for hobby1 in student["favoriteHobbies"]:
        for hobby2 in me["favoriteHobbies"]:
            if hobby1 == hobby2:
                print (student["name"], hobby1)

#12 Find a student who likes at least one favorite legal series as you also like
for student in students:
    for legalSeries1 in student["favoriteLegalSeriesList"]:
        for legalSeries2 in me["favoriteLegalSeriesList"]:
            if legalSeries1 == legalSeries2:
                print (student["name"], legalSeries1)

#13 Find a student who went to a school with the same number of "a"s in its name as yours
for student in students:
    aCountStudent = 0
    for letter in student["school"]:
        if letter == "a" or letter == "A":
            aCountStudent = aCountStudent + 1
    aCountMe = 0
    for letter in me["school"]:
        if letter == "a" or letter == "A":
            aCountMe = aCountMe + 1

    if aCountStudent == aCountMe:
        print(student["name"], student["school"], aCountStudent)

#14 Find a student who speak more languages than you do
for student in students:
    if len(student["languagesSpoken"]) > len(me["languagesSpoken"]):
        print(student["name"], student["languagesSpoken"])

#15 Find a student who has the same number of "s"s in his or her name as yours
for student in students:
    sCountStudent = 0
    for letter in student["name"]:
        if letter == "s" or letter == "S":
            sCountStudent = sCountStudent + 1
    sCountMe = 0
    for letter in me["name"]:
        if letter == "s" or letter == "S":
            sCountMe = sCountMe + 1

    if sCountStudent == sCountMe:
        print(student["name"], sCountStudent)

#16 Find a student who likes at least one (food) dish as you also like
for student in students:
    for food1 in student["favoriteFoodList"]:
        for food2 in me["favoriteFoodList"]:
            if food1 == food2:
                print (student["name"], food1)