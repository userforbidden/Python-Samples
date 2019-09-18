import heapq

files = [4,4,6,12,2,6,7,12]

resultList = []
"""
Simple approach

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

""" 
#Heap Approach
heapq.heapify(files)

while len(files) > 1:
    x = heapq.heappop(files)
    y = heapq.heappop(files)
    resultList.append(x+y)
    heapq.heappush(files,x+y)


print(sum(resultList))

