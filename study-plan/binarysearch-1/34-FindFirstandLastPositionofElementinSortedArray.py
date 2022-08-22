# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                # found target, search front and last
                cur_left, cur_right = mid, mid
                while cur_left > 0 and nums[cur_left - 1] == target:
                    cur_left -= 1

                while cur_right < len(nums) - 1 and nums[cur_right + 1] == target:
                    cur_right += 1

                return [cur_left, cur_right]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Target is Not found
        return [-1, - 1]
