#You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
#Return true if you can reach the last index starting from index 0, or false otherwise.

#Input: nums = [1,2,0,1,0]
#Output: true

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) - 1:
                return True
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False

        return dfs(0)
