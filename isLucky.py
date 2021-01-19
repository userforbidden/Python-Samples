import math  
  
# This function returns true 
# if n is lucky 
def isLucky(n): 
      
    # Create an array of size 10 
    # and initialize all elements  
    # as false. This array is 
    # used to check if a digit  
    # is already seen or not. 
    ar = [0] * 10
    print(ar)
      
    # Traverse through all digits 
    # of given number 
    while (n > 0): 
          
        #Find the last digit 
        digit = math.floor(n % 10) 
  
        # If digit is already seen, 
        # return false 
        if (ar[digit]): 
            return 0
  
        # Mark this digit as seen 
        ar[digit] = 1
  
        # REmove the last digit 
        # from number 
        n = n / 10
      
    return 1
  
# Driver program to test above function. 
arr = [1291, 897, 4566, 1232, 80, 700] 
n = len(arr) 
  
for i in range(0, n): 
    k = arr[i] 
    if(isLucky(k)): 
        print(k, " is Lucky ") 
    else: 
        print(k, " is not Lucky ") 