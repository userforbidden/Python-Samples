import re
class Solution:
	def myAtoi(self, str):
		'''
		:param str: 
		:return: 
		'''
		str = str.strip()
        if re.search(pattern=r"^[+-]?\d+", string=str):
            num_res = re.search(pattern=r"^[+-]?\d+", string=str).group()
            return max(-pow(2, 31), min(pow(2, 31) - 1, int(num_res)))
		else:
			return 0
print(Solution().myAtoi('-4564564 who are you'))