num = 45
symVal = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
romanNum = ''
i = 0 
while num > 0 :
    curVal = list(symVal)[i]
    for _ in range(num // curVal):
        # if (divmod(num,4)[1] == 0 or divmod(num,9)[1] == 0):

        romanNum += symVal[curVal]
        num -= curVal
    i += 1

print(romanNum)