party1 = int(input("Party 1 Votes: "))
party2 = int(input("Party 2 Votes: "))
party3 = int(input("Party 3 Votes: "))

if party1 > party2 and party1 > party3:
    print("Party 1 wins!")
elif party2 > party1 and party2 > party3:
    print("Party 2 wins!")
elif party3 > party1 and party3 > party2:
    print("Party 3 wins!")