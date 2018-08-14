DICTIONARY = ['peanut','butter']

def breakintospaces(s):
#  print(s)
  for i in range(1,len(s)):
    left = s[0:i]
    right = s[i:len(s)]
    if(left in DICTIONARY and right in DICTIONARY):
      return left + " " + right


s = input("Enter the string to break into spaces:")
result = breakintospaces(s)
if result is None:
  print(s)
else: 
  print(result)
