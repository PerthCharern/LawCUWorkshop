import random 
import csv
from time import sleep

print("----------------------------------------------------")
print("Welcome to the Volunteer Volunteering Machine")
print("We help you choose a volunteer when one is needed.")
print("----------------------------------------------------")
input()

with open("./roster.csv", 'r') as file:
    csvreader = csv.reader(file)
    list = []
    for row in csvreader:
        list.append(row)
    while True:
        studentNumber = random.randint(0, 57)
        waitTime = random.randint(5, 30) / 100
        sleep(waitTime)
        row = list[studentNumber]
        print(row[0])
        exitNumber = random.randint(1, 40) 
        if exitNumber == 1:
            break;
    print("You are our next volunteer: " + row[0])
