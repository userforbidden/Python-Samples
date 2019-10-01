arr = [8,5,4,6,1,2]

def swap(ar,first,second):
    temp = ar[first]
    ar[first] = ar[second]
    ar[second] = temp

n = len(arr)

i = n-1
while i > 0:
    t = 1
    for j in range(1,i+1):
        if arr[j-1] > arr[j]:
            swap(arr,j-1,j)
            t=j
    i = t - 1 
"""
Simple raw bubblesort
for i in range(n,1,-1):
    for j in range(1,n):
        if arr[j-1] > arr[j]:
            swap(arr,j-1,j)
"""
print(arr)

