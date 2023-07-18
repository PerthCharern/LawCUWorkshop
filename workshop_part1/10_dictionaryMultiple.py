nameToSchool = {
    "Topaz": "Triam Udom Suksa School",
    "Thanutcha": "Saint Joseph Convent School",
    "Tanchanok": "Burirampitayakom School",
    "Dhann": "Triam Udom Suksa School",
    "Thada": "Mahavajiravudh Songkhla School",
    "Nonthakrit": "Ekamai International School"
}

nameToLastName = {
    "Topaz": "Phayungtham",
    "Thanutcha": "Srikunarak",
    "Tanchanok": "Kosawatwanit",
    "Dhann": "Sutchritpongsa",
    "Thada": "Amnuaykit",
    "Nonthakrit": "Sachdev"
}

nameToNickname = {
    "Topaz": "Namnung",
    "Thanutcha": "Nene",
    "Tanchanok": "Nam",
    "Dhann": "Poom",
    "Thada": "Tai",
    "Nonthakrit": "Nont"
}

while True:
    name = input("Enter name: ")
    if name == "exit":
        break;
    
    school = nameToSchool[name]
    lastName = nameToLastName[name]
    nickname = nameToNickname[name]
    print(school)
    print(lastName)
    print(nickname)
