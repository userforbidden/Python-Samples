from collections import Counter 


"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        l,r = 0,0
        window_count = {}
        ans = float('inf'), 0, 0
        
        while r < len(s):
            character = s[r]
            window_count[character] = window_count.get(character,0)+1
            if character in dict_t and window_count[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                window_count[character] -= 1
                if character in dict_t and window_count[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]