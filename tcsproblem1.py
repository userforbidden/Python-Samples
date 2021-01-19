#reading testcases
from itertools import islice

def divide_chunks(l, n):  
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

with open('testcases.txt') as infile:
    lines = [line[:-1] for line in infile]

iteration = lines[0]

test_cases = divide_chunks(lines[1:],3)

for i,tc in enumerate(test_cases):
    radius = tc[0]
    velocity = tc[1]
    clicks = tc[2]
    for i in range(0,int(clicks)):
        print(radius)
        print(velocity)