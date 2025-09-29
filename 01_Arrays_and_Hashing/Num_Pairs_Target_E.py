#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

#Input: nums = [3,4,5,6], target = 7
#Output: [0,1]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        prevMap = {} #val : index 

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 