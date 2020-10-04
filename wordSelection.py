#Reading the dictionary wordlist
baseWords=open("dictionaryWordList.txt", "r").readlines()
    #Generating the list of words with length more than or equal to 10 characters
wholeWords = [word.rstrip('\n') for word in baseWords if len(word.split()) < 2]

for w in wholeWords:
    print(w)