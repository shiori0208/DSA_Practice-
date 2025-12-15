#You are given an array of integers stones where stones[i] represents the weight of the ith stone.

#Input: stones = [2,3,6,2,4]
#Output: 1

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first =  heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first-second)
            
        stones.append(0)
        return abs(stones[0])
        