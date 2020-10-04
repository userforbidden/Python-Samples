from itertools import product
import hashlib
import os 

class passwordcracker():
    def __init__(self):
        #Initializing the substitutions
        self.substitutions={'s':['$'], 'a': ['4'], 'l': ['1'], 'e': ['3'], 't': ['7'], 'i': ['1'], 'o': ['0'], 'b': ['8'], 'g': ['9']}
        for key in self.substitutions.keys():
            if key not in self.substitutions[key]:
                self.substitutions[key].append(key)
        #initializing the symbols and digits for appending
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>', '<']
        self.symbolCharacters = []
        self.symbolCharacters = self.symbolCharacters + [str(a)+str(b) for a,b in product(range(0,10),self.symbols)]
        self.symbolCharacters = self.symbolCharacters + [str(a)+str(b) for a,b in product(self.symbols,range(0,10))]
        #Initializing th salt for appending in the hash function
        self.shaSalt = str(2575198)
    
    def getPossibilities(self,word):
        wordlist = []
        wordlist.append(word)
        wordlist.append(word.capitalize())
        allPossibilities = []
        wordPossibilities = []
        #Finding all the combinations of substitutions for each word
        for nword in wordlist:
            for substitute in [zip(self.substitutions.keys(),character) for character in product(*self.substitutions.values())]:
                temp=nword
                for replacement in substitute:
                    temp=temp.replace(*replacement)
                wordPossibilities.append(temp)
        # print(wordPossibilities)
        allPossibilities = allPossibilities + wordPossibilities
        # print(len(allPossibilities))
        #Finding all the combination of digit and symbol to append in the word
        symbolPossibilities = [str(a)+str(b) for a,b in product(wordPossibilities,self.symbolCharacters)]
        # print(len(symbolPossibilities))
        allPossibilities = allPossibilities + symbolPossibilities
        # print(len(allPossibilities))
        return allPossibilities

    def getPasswordHash(self,password):
        #Generating the hash value
        return hashlib.sha256(password.encode()).hexdigest()

def main():
    #Reading the dictionary wordlist
    baseWords=open("words_all.txt", "r",encoding='utf-8').readlines()
    #Generating the list of words with length more than or equal to 10 characters
    morethan10 = [word.rstrip('\n').lower() for word in baseWords if len(word) > 10]

    # print(len(morethan10))
    #Opening the given hash values to crack
    hashFile=open("hash_2575198.txt","r").readlines()
    hashValues=[value.rstrip('\n') for value in hashFile ]
    run = passwordcracker()
    cracked = 0
    #Running the code for only 14 cracked passwords as of now
    for word in morethan10:
        possibilities=run.getPossibilities(word)
        # print(possibilities)
        #Comparing the generated hash values with given hash values
        for password in possibilities:
            hashValue = run.getPasswordHash('4621_ctf{%s}'%(password)+run.shaSalt)
            if  hashValue in hashValues:
                cracked += 1
                #If it matches,it prints
                print(str(cracked) + '-' + password + ',' + str(hashValue), flush=True)
                break
    
if __name__ == "__main__":
    main()