#Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

#Input:
#["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

#Output:
#[null, 3, 3, 3, 5, 6]

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
