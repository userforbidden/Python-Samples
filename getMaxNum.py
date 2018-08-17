import re
'''
#Input: given and alphanumeric character and number of commas to split that string
#Output: get the numeric number join them together split them based on the comma, find the max number 
'''
def getMaxNum(s,k):
	#Split the alphanumeric into string and numeric
	s = ''.join(re.findall('\d+',s))

	if k == 0:
		return int(s) 
	else:
		d = len(s) - k
		list1 = []
		temp = ''
		for i in range(0,len(s)):
			list1.append(int(s[i:(i+d)]))
		return max(list1)
	
s = input('Enter the number as a string:')
k = int(input('Enter number of commas:'))
print(getMaxNum(s,k))
