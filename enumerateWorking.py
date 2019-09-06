intList = [1,2,3,4,5,1,2,3,4,5]
intDict = {}

for i,j in enumerate(intList):
    print(i,j)
    intDict.update({j:i})
    print(intDict)