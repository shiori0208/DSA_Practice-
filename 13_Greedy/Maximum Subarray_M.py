#Given an array of integers nums, find the subarray with the largest sum and return the sum.
#A subarray is a contiguous non-empty sequence of elements within an array.

#Input: nums = [2,-3,4,-2,2,1,-1,4]
#Output: 8

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n 
            maxSub = max(maxSub, curSum)
        return maxSub
