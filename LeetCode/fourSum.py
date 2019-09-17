def fourSum(n, t):
    n.sort()
    if not n: 
        return []
    length, valueDict, resultSet, lastvalue = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]
    
    for i in range(length-3):
        a = n[i]
        if a + 3*lastvalue < t:
            continue
        if 4*a > t:
            break
        for j in range(i+1,length-2):
            b = n[j]
            if a + b + 2*lastvalue < t:
                continue
            if a + 3*b > t:
                break
            for k in range(j+1,length-1):
                c = n[k]
                d = t-(a+b+c)
                if d > lastvalue:
                    continue
                if d < c:
                    break
                if d in valueDict and valueDict[d] > k:
                    resultSet.add((a,b,c,d))
    print(resultSet)

<<<<<<< Updated upstream
fourSum([1, 0, -1, 0, -2, 2,6,7,3,2,10],5)
=======
fourSum([1, 0, -1, 0, -2, 2,2,1,5,-5],0)
>>>>>>> Stashed changes
