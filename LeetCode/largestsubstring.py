class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        # Used Characters hashmap or set to hold the values
        usedChar = {}
        for index, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
                # print(start)
            else:
                maxLength = max(maxLength,index-start+1)
                # print(maxLength)
            usedChar[char] = index
            print(usedChar)
        return maxLength


print(Solution().lengthOfLongestSubstring('abcabcdefgabcdefghijabcbcdefghijklb'))