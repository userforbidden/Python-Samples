def factorialfunc(n):
    factorial = 1 
    if n < 0:
      print("Factorial cannot be processed for negative number : %d"%(n))
    elif n == 0:
      print("Factorial of 0 is 1")
    else:
      for i in range(1,n+1):
        factorial = factorial * i
      print("Factorial of %s is %s"%(n,factorial))

def recursivefactorial(n):
    if n == 1:
      return 1
    else:
      return n * recursivefactorial(n-1)

num = int(input("Enter the number for which Factorial to be found:"))
factorialfunc(num)
print("Now using recursive method")
if num < 0:
    print("Factorial cannot be processed for a negative number: %d"%(num))
elif num == 0: 
    print("Factorial of 0 is 1")
else:
    print("Recursion factorial of %s is %s"%(num,recursivefactorial(num)))
