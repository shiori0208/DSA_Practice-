#Given an integer array nums and an integer k, return the k most frequent elements within the array.

#Input: nums = [1,2,2,3,3,3], k = 2
#Output: [2,3]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {} #dictionary storing key value pair {freq: num}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 + count.get(n, 0)

         #items returns a key-value pair   
        for n, c in count.items():
            freq[c].append(n)

        res=[]
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


             


