num = 45
# symVal = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
# romanNum = ''
# i = 0 
# while num > 0 :
#     curVal = list(symVal)[i]
#     for _ in range(num // curVal):
#         # if (divmod(num,4)[1] == 0 or divmod(num,9)[1] == 0):

#         romanNum += symVal[curVal]
#         num -= curVal
#     i += 1

# print(romanNum)
class Solution(object):
    def __init__(self):
        self.roman = ''
    def intToRoman(self, num):
        self.num = num
        self.checkRoman(1000, 'M')
        self.checkRoman(500, 'D')
        self.checkRoman(100, 'C')
        self.checkRoman(50, 'L')
        self.checkRoman(10, 'X')  
        self.checkRoman(5, 'V') 
        self.checkRoman(1, 'I')
        return self.roman
        
    def checkRoman(self, value, strVal):
        numVal = self.num // value
        if (numVal > 0 and numVal < 4):          
            for _ in range(0, numVal):
                self.roman += strVal
            self.num -= value * numVal
        if (value > 100 and self.num / (value - 100) > 0):
            self.roman += 'C' + strVal
            self.num -= (value - 100)
        if (value > 10 and self.num / (value - 10) > 0):
            self.roman += 'X' + strVal
            self.num -= (value - 10)
        if (value > 1 and self.num / (value - 1) > 0):
            self.roman += 'I' + strVal
            self.num -= value - 1

print(Solution().intToRoman(49))