#You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:
#Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

#Input: nums = [2,4,1,1,1,1]
#Output: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1 
        return res
