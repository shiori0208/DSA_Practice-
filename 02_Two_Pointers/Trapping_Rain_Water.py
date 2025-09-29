#You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1. Return the maximum area of water that can be trapped between the bars.

#Input: height = [0,2,0,3,1,0,1,3,2,1]
#Output: 9

class Solution:
    def trap(self, height: list[int]) -> int:
        
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res 


