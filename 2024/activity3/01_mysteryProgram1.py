# % represents the modulo operator. It wraps the number back into the appropriate domain.
# Basically, it gives you the "remainer" after a division.
# For example, 0 % 3 = 0, 1 % 3 = 1, 2 % 3 = 2, 3 % 3 = 0, 4 % 3 = 1, 5 % 3 = 2, 6 % 3 = 0

studentFirstNames = ["Akkarawin", "Anyanuj", ..., "Yay"]

studentHighSchools = ["Bangkok Christian International School", "Brighton College Bangkok", ..., "Unity Concord International School"]

studentFavoriteDishes = [...] # "Hamburger", "Khao Man Gai", "Okonomiyaki", "Wienerschnitzel", ...

studentBranchOfLawMostInterestedIn = [...] # "Criminal", "Commercial", "Administrative", "International", "Intellectual Property", "Maritime", "Tort", "Constitution", "Real Property", "Environmental", ...

studentFavoriteLegalSeries = [...] # "Suits", "The Good Wife", "Law School", "The Devil Judge", "Ace Attorney", ...

# Supposed that index i represents you

staffNicknames = ["Perth", "Vin", "Up", "Earn"]

staffFavoriteDishes = [...]

staffFavoriteLegalSeries = [...]

# 1

length = len(studentFirstNames)
if i == length - 1:
    print(studentFirstNames[0])
else:
    print(studentFirstNames[i + 1])

# 2

length = len(studentBranchOfLawMostInterestedIn)
if i == 0:
    print(studentBranchOfLawMostInterestedIn[length - 1])
else:
    print(studentBranchOfLawMostInterestedIn[i - 1])

# 3

length = len(studentFavoriteDishes)
print(studentFavoriteDishes[(i + 5) % length])

# 4

length = len(studentFavoriteLegalSeries)
print(studentFavoriteLegalSeries[(i + 30) % length])

# 5

count = 0

for highSchool in studentHighSchools:
    if (highSchool == studentHighSchools[i]):
        count = count + 1

print(count)

# 6

print(staffNicknames[i % 4])

# 7

print(staffFavoriteDishes[(i + 2) % 4])

# 8

result = 0

for show in staffFavoriteLegalSeries:
    if (show == studentFavoriteLegalSeries[i]):
        result = result + 1

print(result)
