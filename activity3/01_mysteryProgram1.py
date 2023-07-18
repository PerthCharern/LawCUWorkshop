while True:
    sentence = input("Give me an English sentence: ")
    if (sentence == "exit"):
        break;

    sentenceAsList = sentence.split(" ")
    
    newList = []

    for word in sentenceAsList:
        if len(word) == 2:
            word = word + "*"
        elif len(word) == 1:
            word = word + "**"
        newList.append(word)

    newList.reverse()

    print(" ".join(newList))
