def animalCrackers(text):
    wordlist = text.split() #split the text to words
    # print(wordlist)
    return wordlist[0][0] == wordlist[1][0] #compare first letter of first word with first letter of 2nd word and return true or false

# the below is the drive code 
print(animalCrackers('hippo hitle'))
