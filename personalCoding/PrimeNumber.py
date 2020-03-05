import multiprocessing
import time 
from math import ceil, sqrt
checknumbers = [10000000002065383,1111111111111111,10112269203786181,10269797835402631]
def is_Prime(n):
    sqrt_number = int(ceil(sqrt(n)))
    for i in range(2,sqrt_number+1):
        if n%i == 0:
            return False
    return True
 
def checkIftheNumberIsPrime():
    pool = multiprocessing.Pool(processes=1)
    result = pool.starmap(is_Prime, zip(checknumbers))
    return result
 
if __name__ == '__main__':
    start_time = time.time()
    primeresults = checkIftheNumberIsPrime()
    for i,n in enumerate(checknumbers):
        if primeresults[i]:
            print("%d is prime"%(n))
        else:
            print("%d is not prime"%(n))
    end_time = time.time()
    print("This took %.3f seconds"%(end_time-start_time))