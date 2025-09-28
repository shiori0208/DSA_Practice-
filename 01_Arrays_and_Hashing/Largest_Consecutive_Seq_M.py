#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

#Input: nums = [2,20,4,10,3,4,5]
#Output: 4

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numSet = set(nums) #turning it into a set
        longest = 0 #counting length of sequence

        for n in nums:
            #check if it has prev num
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest) #comparing sequence lengths

        return longest
        
