# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            n = n ^ nums[i]

        return n
