num = 353
reverse_num = 0
temp = num 
# print(num,reverse_num)

while(temp != 0):
    remainder = int(temp % 10)
    print(remainder)
    reverse_num = int((reverse_num*10) + remainder)
    print(reverse_num)
    temp = int(temp / 10)
# print(reverse_num)
if reverse_num == num:
    print('It is Palindrome')
else:
    print('not Palindrome')