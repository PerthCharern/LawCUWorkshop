# What's the output from the last line of this program, with the following input?
#
# I
# like
# democracy
# and
# I
# read
# a
# lot
# of
# constitutions

sentence = ""
while True:
    mystery = input("Enter a word: ")
    
    if (mystery.lower() == "exit"):
        break;
    
    if (mystery.lower() == "democracy" or mystery.lower() == "constitution"):
        sentence = sentence + "[censored]" + " "
    else:
        sentence = sentence + mystery + " "
    print("Word added")
sentence = sentence[:-1] # Remove last character from string
sentence = sentence + "."

print(sentence)
