# % represents the modulo operator, i.e. it gives you the "remainder" after a division.
# For example, 0 % 3 = 0, 1 % 3 = 1, 2 % 3 = 2, 3 % 3 = 0, 4 % 3 = 1, 5 % 3 = 2, 6 % 3 = 0

# Student information

studentFirstNames = ["Achiraya", "Akewisut", ..., "Yolanda"] # In alphabetical order

studentHighSchoolsOrUniversities = ["Harrow International School", "Regent's International School", ..., "Chulalongkorn University"] # In the same order as the students in studentFirstNames

studentBranchOfLawMostInterestedIn = [...] # "Criminal", "Commercial", "Administrative", "International", "Intellectual Property", "Maritime", "Tort", "Constitution", "Real Property", "Environmental", ...

studentFavoriteLegalSeries = [...] # "Suits", "The Good Wife", "Extraordinary Attorney Woo", "Law School", "The Devil Judge", "Ace Attorney", ...

length = len(studentFirstNames)

# Staff information

staffNicknames = ["Perth", "Vin", "Touch", "Lily", "Am", "Liy"]

staffFavoriteLegalSeries = [...]

# Supposed that index i represents you

# 1

print(i)
print(studentFirstNames[i])
print(studentHighSchoolsOrUniversities[i])
print(studentBranchOfLawMostInterestedIn[i])
print(studentFavoriteLegalSeries[i])

# 2

if i == length - 1:
    print(studentFirstNames[0])
    print(studentBranchOfLawMostInterestedIn[0])
else:
    print(studentFirstNames[i + 1])
    print(studentBranchOfLawMostInterestedIn[i + 1])

# 3

if i == 0:
    print(studentBranchOfLawMostInterestedIn[length - 1])
else:
    print(studentBranchOfLawMostInterestedIn[i - 1])

# 4

print(studentFavoriteLegalSeries[(i + 30) % length])

# 5

count = 0

for highSchool in studentHighSchoolsOrUniversities:
    if highSchool == studentHighSchoolsOrUniversities[i]:
        count = count + 1

print(count)

# 6

print(staffNicknames[i % len(staffNicknames)])

# 7

print(staffFavoriteLegalSeries[(i + 2) % len(staffNicknames)])

# 8

result = 0

for show in staffFavoriteLegalSeries:
    if (show == studentFavoriteLegalSeries[i]):
        result = result + 1

print(studentFavoriteLegalSeries[i])
print(result)
