#Given an array of integers numbers that is sorted in non-decreasing order.
#Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
#There will always be exactly one valid solution.

#Input: numbers = [1,2,3,4], target = 3
#Output: [1,2]

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
        