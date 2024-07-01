# What do you think is the output here?

originalString = "natural law vs positive law"
originalStringAsList = originalString.split(" ")

newList = []

for mystery in originalStringAsList:
    if (mystery != "law"):
        newList.append(mystery)

newList.reverse()

for mystery in newList:
    print(mystery)