class Solution(object):
    def recParenthesis(self,numopen,numclose,currentresult,result):
        if numopen == 0 and numclose == 0:
            result.append(currentresult)
            return result
        
        if numopen > 0:
            self.recParenthesis(numopen-1,numclose,currentresult+"(",result)
    
        if numopen < numclose:
            self.recParenthesis(numopen,numclose-1,currentresult+")",result)
        
        return result
        
    def generateParenthesis(self, n):
        result = []
        return self.recParenthesis(n,n,"",result)

    # def generateParanthesis(self,numopen,numclose,resultinprogress,result):
    #     if numopen == 0 and numclose == 0:
    #         result.append(resultinprogress)
    #         return result
        
    #     if numopen > 0:
            
    #         self.generateParanthesis(numopen-1,numclose,resultinprogress+'(',result)
        
    #     if numopen < numclose:
    #         self.generateParanthesis(numopen,numclose-1,resultinprogress+')',result)
        
    #     return result


n = 4
print(Solution().generateParenthesis(n))