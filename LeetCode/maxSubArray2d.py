"""
Definition for KadaneResult
"""
class KadaneResult():
    def __init__(self,maxSum,startIndex,endIndex):
        self.maxSum = maxSum
        self.startIndex = startIndex
        self.endIndex = endIndex
"""
Definition for Rectangle
"""
class Rectangle():
    def __init__(self,interiorResult,leftIndex,rightIndex,topIndex,bottomIndex):
        self.interiorResult = interiorResult
        self.leftBorderIndex = leftIndex
        self.rightBorderIndex = rightIndex
        self.topBorderIndex = topIndex
        self.bottmBorderIndex = bottomIndex

"""
Main Solution class

"""
class Solution():
    def maxSumArray(self,matrix,budget):

        rows = len(matrix)
        cols = len(matrix[0])
        maxRectangle = Rectangle(0,0,0,0,0)

        # runningRowSums = 

        for left in range(0,cols):
            
            runningRowSums = [0 for i in range(rows)]
        
            for right in range(left,cols):
                runningRowSums = [matrix[i][right]+ ri for i,ri in enumerate(runningRowSums)]
                # for i in range(0,rows):
                #     runningRowSums[i] += matrix[i][right]

                kadaneResult = self.kadane(runningRowSums)

                if kadaneResult.maxSum > maxRectangle.interiorResult and kadaneResult.maxSum <= budget:
                    maxRectangle.interiorResult = kadaneResult.maxSum
                    maxRectangle.leftBorderIndex = left
                    maxRectangle.rightBorderIndex = right
                    maxRectangle.topBorderIndex = kadaneResult.startIndex
                    maxRectangle.bottmBorderIndex = kadaneResult.endIndex

        return maxRectangle

    #Calculate Maximum SubArray Window and get the Index using kadane's Algorithh
    def kadane(self,arr):
        maxstartingIndex = -1
        maxendingIndex = -1

        bestMaxSofar = 0 
        currStart = 0
        bestMaxatThisIndex = 0

        for i in range(0,len(arr)):
            bestMaxatThisIndex += arr[i]

            if bestMaxatThisIndex < 0:
                bestMaxatThisIndex = 0
                currStart = i + 1
            if bestMaxatThisIndex > bestMaxSofar:
                bestMaxSofar = bestMaxatThisIndex
                maxstartingIndex = currStart
                maxendingIndex = i 

        return KadaneResult(bestMaxSofar,maxstartingIndex,maxendingIndex)


def main():
    dial = Solution()
    matrix = [[7, -5,  -7,  4, -4],
    [  8,  3,  -6,  5,  2 ],
    [ 4,  4,   7, -6,  3 ],
    [ -8,  9,  -3,  3, -7 ]]
  
    rectangle = dial.maxSumArray(matrix,10)
    print(rectangle.interiorResult,rectangle.leftBorderIndex,rectangle.rightBorderIndex,rectangle.topBorderIndex,rectangle.bottmBorderIndex)

if __name__ == "__main__":
    main()
