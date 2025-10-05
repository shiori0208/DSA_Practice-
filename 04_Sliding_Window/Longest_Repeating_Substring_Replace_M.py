#You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

#Input: s = "XYYX", k = 2
#Output: 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 
        l = 0
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res 