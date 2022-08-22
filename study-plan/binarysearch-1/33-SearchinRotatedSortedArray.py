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

        # return the index of minimum number in a list
        def find_min_idx(nums: List[int]) -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return left

        # find the index of largest number in nums
        # O(logn)
        min_idx = find_min_idx(nums)
        largest_num_idx = min_idx - 1 if min_idx != 0 else len(nums) - 1

        # determine which side should be done with binary searcch
        # O(logn)
        if target >= nums[0]:
            # doing bs in the left side
            return binary_search(nums, 0, largest_num_idx, target)
        else:
            # doing bs in the right side
            return binary_search(nums, largest_num_idx + 1, len(nums) - 1, target)
