def twoSumLessThanK(A,K):
        ans = -1

        i,j = 0, len(A)-1
        A = sorted(A)

        while i < j:
            if A[i]+A[j] < K:
                ans = max(ans,A[i]+A[j])
                i += 1
            else:
                j -= 1
        return ans


print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))