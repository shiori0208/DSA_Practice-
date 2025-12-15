#Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
#By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

#Input: nums = [2,3,1,5,4], k = 2
#Output: 4
 
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)
        