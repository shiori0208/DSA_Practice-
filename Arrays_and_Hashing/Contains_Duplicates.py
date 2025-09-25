#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set() #making a hashset in python 

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False    