#You are given an integer array heights where heights[i] represents the height of the ith col
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

#Input: height = [1,7,2,5,4,7,3,6]
#Output: 36

class Solution:
    def maxArea(self, heights: list[int]) -> int:

        res = 0 
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r]) #distance between two values (r-l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1

        return res 

