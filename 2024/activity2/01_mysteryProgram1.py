# What's the output of this program given the following input?
#
# we
# will
# eat
# chicken
# with
# basil
# and
# omelette
# with
# pork
# for
# lunch
# exit

sentence = ""

while True:
    word = input("Enter a word: ")
    word = word.lower()

    if word == "exit":
        break # exit the loop
    
    if word == "chicken" or word == "duck":
        sentence = sentence + "pork" + " "
    elif word == "pork":
        sentence = sentence + "chicken" + " "
    else:
        sentence = sentence + word + " "

print(sentence)
