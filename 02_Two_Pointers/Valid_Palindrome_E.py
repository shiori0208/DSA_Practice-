#Given a string s, return true if it is a palindrome, otherwise return false.

#Input: s = "Was it a car or a cat I saw?"
#Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s)-1 #two pointers at two sides of the string

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = 1 + l, r - 1 
        return True   


    def isAlphaNum(self, c): #function to check if character is a alphabet or numeric
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
    