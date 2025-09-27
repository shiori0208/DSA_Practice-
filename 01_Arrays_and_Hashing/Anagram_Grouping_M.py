#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

#Input: strs = ["act","pots","tops","cat","stop","hat"]
#Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        res = defaultdict(list) #mapping character Counts to the list of anagrams

        #for every string in input...
        for s in strs: 
            count = [0] * 26 #making an array of all alphabets a....z

            #for every letter in string...
            for c in s:
                count[ord(c) - ord("a")] += 1 
                #ord gives numeric value of letter to place count at right index
                #eg: c=82 82-80 = 2 (index[2]=1)

            res[tuple(count)].append(s)

        return list(res.values())
    
    #o(m*n) 
    #m is no. of strings in input list
    #n is avg length of string in inputs 