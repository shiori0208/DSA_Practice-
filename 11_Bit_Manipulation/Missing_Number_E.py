#Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

#Input: nums = [1,2,3]
#Output: 0

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res 

