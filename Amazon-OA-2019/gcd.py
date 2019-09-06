def findGCD(x,y,iteration):
    
    
    while y > 0:
        print('Iteration : %d'%(iteration))
        print('Before - x:%d , y:%d'%(x,y))
        x, y = y, x%y
        print('After - x:%d , y:%d'%(x,y))
    
    return x
    

def generalGCD(num, arr):
    gcd = arr[0]
    for i in arr[1:]:
        gcd = findGCD(gcd,i,i)
    print(gcd)

generalGCD(5, [24,36,48])