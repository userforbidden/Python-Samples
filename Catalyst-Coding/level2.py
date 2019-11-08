import os
import sys
import numpy as np
import math


class level2():

    def __init__(self):
        pass

    
    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
    def checkLeft(self,v,row,col,arr):
        return not (v == arr[row,col-1])
    def checkRight(self,v,row,col,arr):
        return not (v == arr[row,col+1])
    def checkBottom(self,v,row,col,arr):
        return not (v == arr[row+1,col])
    def checkTop(self,v,row,col,arr):
        return not (v == arr[row-1,col])
    def findBorderIndices(self,arrlen,altitude,country):
        # print(country)
        arr2D = np.array(country,np.int32)
        # for country in np.unique(arr2D):
        #     result = np.where(arr2D == country)
        # print(arr2D.shape)
        # print(arr2D[49,49])
        for country in np.unique(arr2D):
            row, col = np.where(arr2D == country)
            # print(row)
            # print(col)
            count = 0 
            rowmax = arrlen[0]-1
            colmax = arrlen[1]-1

            for i in range(0,len(row)):
                if row[i] == 0 or col[i] == 0: 
                    count += 1
                elif row[i] == rowmax or col[i] == colmax:
                    count += 1
                elif self.checkLeft(country,row[i],col[i],arr2D) or self.checkRight(country,row[i],col[i],arr2D) or self.checkTop(country,row[i],col[i],arr2D) or self.checkBottom(country,row[i],col[i],arr2D) :
                    count += 1

            # print('country %d : %d '%(country,count))
            print(count)
        # print(self.checkLeft(0,12,38,arr2D))




def main():
    filepath = 'C:\data\personal-github\Python-Samples\Catalyst-Coding\level2\level2_5.in'

    with open(filepath, 'r') as f:
        dial = level2()
        list1 = [[altitude for altitude in dial.chunks(line.rstrip().split(),2)] for line in f.readlines()]
        altitude = [[int(alt[0]) for alt in line] for line in list1]
        country = [[int(alt[1]) for alt in line] for line in list1]
        dial.findBorderIndices([int(altitude[0][0]),int(country[0][0])],altitude[1:],country[1:])


if __name__ == '__main__':
    main()
