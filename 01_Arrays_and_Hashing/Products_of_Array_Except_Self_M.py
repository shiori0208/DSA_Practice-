#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

#Input: nums = [1,2,4,6]
#Output: [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = [1] * (len(nums))

        prefix=1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*postfix
            postfix *= nums[i]

        return res
    
    #more logic heavy code rather than conceptual



        
