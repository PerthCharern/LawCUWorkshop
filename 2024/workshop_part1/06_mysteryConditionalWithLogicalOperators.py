# What does this program do?

color = input("Enter your car color: ")
make = input("Enter your car make: ")
accident = input("Have you had an accident in the past 2 years (Y/N)?: ")

if (color.lower() == "red" or make.lower() == "bmw" or accident.lower() == "y"):
    print("Your car insurance dues will be higher.")
else:
    print("Your car insurance dues will be standard.")