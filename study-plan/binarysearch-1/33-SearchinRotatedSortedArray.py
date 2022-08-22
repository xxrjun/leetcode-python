# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # return the index of target, -1 if not found
        def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        # find the index of largest number in nums
        largest_num_idx = len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                largest_num_idx = i
                break

        # determine which side should be done with binary searcch
        if target >= nums[0]:
            # doing bs in the left side
            return binary_search(nums, 0, largest_num_idx, target)
        else:
            # doing bs in the right side
            return binary_search(nums, largest_num_idx + 1, len(nums) - 1, target)
