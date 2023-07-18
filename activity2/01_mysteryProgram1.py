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
    word = input("Enter a word: ")

    if (word.lower() == "exit"):
        break;
    
    if (word.lower() == "democracy" or word.lower() == "constitution"):
        sentence = sentence + "[censored]" + " "
    else:
        sentence = sentence + word + " "
    
    print("Word added")

sentence = sentence[:-1] # Remove last character from string
sentence = sentence + "."

print(sentence)
