files = [4,4,6,12]

resultList = []
tempFile = files[:]
for n in files:
    if len(tempFile) != 1:
        x = min(tempFile)
        tempFile.remove(x)
        y = min(tempFile)
        tempFile.remove(y)
        z = x + y
        resultList.append(z)
        tempFile.append(z)
print(sum(resultList))

