import os
import sys
import numpy as np
import math


class level1():

    def __init__(self):
        pass

    
    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
    def findEfficientWay(self,l):
        arr2D = np.array(l)
        print(np.amin(arr2D))
        print(np.amax(arr2D))
        print(math.floor(np.average(arr2D)))
        return np.amin(arr2D), np.amax(arr2D), math.floor(np.average(arr2D))

def main():
    filepath = 'C:\data\personal-github\Python-Samples\Catalyst-Coding\level1\level1_5.in'
    with open(filepath, 'r') as f:
        # print(f.readlines())
        l = [[int(num) for num in line.rstrip().split()] for line in f.readlines()]
        # print(l[1:])
        dial = level1()
        print(dial.findEfficientWay(l[1:]))


if __name__ == '__main__':
    main()
