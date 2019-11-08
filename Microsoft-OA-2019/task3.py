"""
Given a String S consisting og N Lowercase letters that must be deleted to obtain a word in which every letter occurs 
a unique number of times. We Only care about the occurrences of letters that appear at least once in result


Examples: 
1. Given S='eeeeffff', the function should return 1. We can delete one occurence of e or one occurence of f. 
Then one letter will occur four times and the other three times 
2. Given S = 'aabbffddeaee' the function should return 6. For example, we can delete all occurences of e and f and one occurence of d to obtain the word  'aabbda' Note that both e and f will occur zero times in the new word, but that's fine, since we only care about the letter that appear at least once
3. Given S = 'llll' the function should return 0( there is no need to delete any character)
4. Given S = 'example' the function should return 4
"""

def removeNforUnique(str):
    ans = 0 
    charHash = {i:str.count(i) for i in set(str)}

    for i,data in enumerate(charHash):
        print(data)
    return ans

print(removeNforUnique('example'))