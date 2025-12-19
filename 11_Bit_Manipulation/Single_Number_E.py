#You are given a non-empty array of integers nums. Every integer appears twice except for one. Return the integer that appears only once.

#Input: nums = [3,2,3]
#Output: 2

#using XOR to compare bitwise

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res 
        return res
