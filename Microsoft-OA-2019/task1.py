def removeconsecutiveThreeChars(string):
    res = ''
    count = 0

    while count < len(string): 
        if count < len(string) - 2 and string[count]*3 == string[count:count+3]:
            res += string[count] + string[count+1]
            count += 3
        else:
            res += string[count]
            count += 1
    if len(res) == len(string):
        return res
    else:
        return removeconsecutiveThreeChars(res)

print(removeconsecutiveThreeChars('ddddeedaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad'))