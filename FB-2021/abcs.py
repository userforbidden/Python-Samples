'''
ABC's Warmup 
Given three integers AA, BB, and CC, determine their sum.
Your task is to implement the function getSum(A, B, C) which returns the sum A + B + CA+B+C.
Constraints
1 \le A, B, C \le 1001≤A,B,C≤100
Sample Test Case #1
A = 1
B = 2
C = 3
Expected Return Value = 6
Sample Test Case #2
A = 100
B = 100
C = 100
Expected Return Value = 300
Sample Test Case #3
A = 85
B = 16
C = 93
Expected Return Value = 194
'''
def Solution(A,B,C):
    # This is simple straight forward solution. Just return the sum of all the variables provided 
    # it is the correct solution 
    return A+B+C

    # MY code was able to complete all the test cases 

print(Solution(1,2,3))
    
