nameToAllDetails = {
    "Topaz": {
        "name": "Topaz",
        "school":  "Triam Udom Suksa School",
        "lastName": "Phayungtham",
        "nickname": "Namnung"
    },
    "Thanutcha": {
        "name": "Thanutcha",
        "school": "Saint Joseph Convent School",
        "lastName": "Srikunarak",
        "nickname": "Nene"

    },
    "Tanchanok": {
        "name": "Tanchanok",
        "school": "Burirampitayakom School",
        "lastName": "Kosawatwanit",
        "nickname": "Nam"
    },
    "Dhann": {
        "name": "Dhann",
        "school": "Triam Udom Suksa School",
        "lastName": "Sutchritpongsa",
        "nickname": "Poom"
    },
    "Thada": {
        "name": "Thada",
        "school": "Mahavajiravudh Songkhla School",
        "lastName": "Amnuaykit",
        "nickname": "Tai"

    },
    "Nonthakrit": {
        "name": "Nonthakrit",
        "school": "Ekamai International School",
        "lastName": "Sachdev",
        "nickname": "Nont"
    } 
}

while True:
    name = input("Enter name: ")
    if name == "exit":
        break;
    
    school = nameToAllDetails[name]["school"]
    lastName = nameToAllDetails[name]["lastName"]
    nickname = nameToAllDetails[name]["nickname"]
    print(school)
    print(lastName)
    print(nickname)
    print(nameToAllDetails[name])
