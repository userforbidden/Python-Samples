def twoSumLessThanK(A,K):
        #Initialize the answer for -1 for a default return value 
        ans = -1
        # set two pointers I, j 
        #i to the starting j to the end of the array 
        i,j = 0, len(A)-1
        # Sort the array
        A = sorted(A)

        # Loop until both i and j meet 
        while i < j:
            # if sum of number in index i and index j less than K add the sum to result answer, 
            # take the max out of current answer and current sum 
            # Now increase the i pointer  
            if A[i]+A[j] < K:
                ans = max(ans,A[i]+A[j])
                i += 1
            # else if the sum number in i and j is greater than K, Dont update the answer. Just 
            # decrease the Index of j by 1
            else:
                j -= 1
        return ans

# Time complexity here is we are making n-1 comparisions 
# Space Complexity is constant No extra space is used 

print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))