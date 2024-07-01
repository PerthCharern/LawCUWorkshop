nameToSchool = {
    "Topaz": "Triam Udom Suksa School",
    "Thanutcha": "Saint Joseph Convent School",
    "Tanchanok": "Burirampitayakom School",
    "Dhann": "Triam Udom Suksa School",
    "Thada": "Mahavajiravudh Songkhla School",
    "Nonthakrit": "Ekamai International School"
}

while True:
    name = input("Enter name: ")
    if name == "exit":
        break;
    
    school = nameToSchool[name]
    print(school)
