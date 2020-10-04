baseWords=open("dictionaryComWordList.txt",'rb').readlines()
newwords = []
# lsit = ['a','b','c']
f=open('parseddictionaycomwordList.txt','w')
for word in baseWords:
    newwords.append(word.decode("utf-8").split('|')[0].strip())
    # data = str(word).split('|')[0].strip().encode('utf-8')
    # f.write(str(data)+'\n')
f.write("\n".join(newwords))
f.close()

