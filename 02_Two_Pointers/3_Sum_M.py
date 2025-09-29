#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]: 

        res = []
        nums.sort() 

        for i, a in enumerate(nums): #making a the first element 
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1 #then making l and r pointers out of the rest two
            while l < r:
                threeSum = a + nums[l] +nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l = l+1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
        return res
        
