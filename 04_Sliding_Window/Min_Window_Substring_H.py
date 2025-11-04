#Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

#Input: s = "OUZODYXAZV", t = "XYZ"
#Output: "YXAZ"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #edge case in case target string is null
        if t == "": return ""

        #making the hashmaps...
        countT, window = {}, {}

        #countT is hash map of t
        #counting the characters and their frequencies
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #making sure the hash counts match
        #have is measuring frequencies in variable snippets of s 
        #need is fixed at length of t 
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0 

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1 

            while have==need:
                #update the result and length
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                #now keep popping from left side to shorten result
                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have -= 1 
                l += 1 

        #l, r here unpacks the indices of the res
        l, r = res 
        return s[l: r+1] if resLen != float("infinity") else ""







