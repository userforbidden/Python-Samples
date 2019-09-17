intarr = [2,1,4,7,4,8,3,6,4,7]
strarr = int(''.join(map(str,intarr))) + 1
print(list(map(int,list(str(strarr)))))