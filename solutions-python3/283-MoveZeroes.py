# 283. Move Zeroes
# Idea:
# Solutin I. Two Pointer (Faster)
#               1. Using Two Pointer, and swap
# Solution II. (Slower, easy to understand)
#               1. Push every non-zero element front of the list
#               2. Fill Other space with 0
# Solution III: Two Pointer (4 Cases)
#               1. Two Pointer,
#               2. 四種可能 (0, 0), (non-0, 0), (0, non-0), (non-0, non-0)
class Solution:
    # Solution 1
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(1, len(nums)):            
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                
            if nums[slow] != 0:
                slow += 1


    # Solution 2
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     countZero = 0
    #     for n in nums:
    #         if n == 0: countZero += 1
        
    #     cur = 0
    #     for n in nums:
    #         if n != 0:
    #             nums[cur] = n
    #             cur += 1

    #     for i in range(countZero):
    #         nums[cur] = 0
    #         cur += 1


    # Solution 3
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     firstPointer = 0
    #     secondPointer = 1

    #     while firstPointer < len(nums) and secondPointer < len(nums):
    #         if nums[firstPointer] != 0 and nums[secondPointer] != 0:   # (non-0, non-0)
    #             firstPointer += 1
    #             secondPointer += 1
    #         elif nums[firstPointer] != 0 and nums[secondPointer] == 0:    # (non-0, 0)
    #             while nums[firstPointer] != 0 and firstPointer < len(nums) - 1:
    #                 firstPointer += 1
    #         elif nums[firstPointer] == 0 and nums[secondPointer] != 0:    #(0, non-0)
    #             nums[firstPointer], nums[secondPointer] = nums[secondPointer], nums[firstPointer]
    #             firstPointer += 1
    #             secondPointer += 1
    #         elif nums[firstPointer] == 0 and nums[secondPointer] == 0:      # (0, 0)
    #             while nums[secondPointer] == 0 and secondPointer < len(nums) - 1:
    #                 secondPointer += 1
    #             nums[firstPointer], nums[secondPointer] = nums[secondPointer], nums[firstPointer]
    #             firstPointer += 1
