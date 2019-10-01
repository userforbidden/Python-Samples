def longestValidParentheses(s):
        maxans = 0
        res = [-1]
        
        for i in range(len(s)):
            if s[i] == '(':
                res.append(i)
            else:
                res.pop()
                if not res:
                    res.append(i)
                else:
                    maxans = max(maxans,i-res[-1])
        
        return maxans

print(longestValidParentheses(')((())))'))