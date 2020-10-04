# files = ['unscramblerComadjectives.txt','unscramblerComadverbs.txt','unscramblerComNouns.txt','unscramblerComVerbs.txt','thesaurusComWordList.txt']
files = ['dictionaryComWordList.txt','parsedUnscramblerList.txt','dictionaryWordList.txt','words.txt']
combined = []
for fil in files:
    f = open(fil,'rb').readlines()
    print(len(f))
    for word in f:
        splt = word.decode("utf-8").split()
        # print(splt)
        for s in splt:
            if (s.lower() not in combined) and (len(s)>10):
                combined.append(s.lower())
    print(len(combined))

# f=open('parsedUnscramblerList.txt','w',encoding='utf-8')
f=open('finalWordList.txt','w',encoding='utf-8')
f.write("\n".join(sorted(combined)))
f.close()