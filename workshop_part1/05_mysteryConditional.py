yeaVoteCount = int(input("Enter the number of people voting Yea: "))
nayVoteCount = int(input("Enter the number of people voting Nay: "))
noOpinionVoteCount = int(input("Enter the number of people casting no vote: "))
absentCount = int(input("Enter the number of people absent: "))
total = yeaVoteCount + nayVoteCount + noOpinionVoteCount + absentCount

input("Press any key to see the vote result... drumrolls...")

if (yeaVoteCount > total / 2):
    print("You get to eat cake")
elif (yeaVoteCount > nayVoteCount):
    print("You don't get to eat cake, even though the number of Yea votes are greater than the number of Nay votes")
else:
    print("You don't get to eat cake, obviously")