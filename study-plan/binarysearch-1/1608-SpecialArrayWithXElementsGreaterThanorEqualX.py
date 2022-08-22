# 1608. Special Array With X Elements Greater Than or Equal X

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # sort array first
        sorted_nums = sorted(nums)

        for x in range(len(sorted_nums) + 1):
            # there should be x numbers >= x
            # using binary search to get the position where is start to be greater than x

            start = len(sorted_nums) - 1

            left, right = 0, len(sorted_nums) - 1
            while left <= right:
                mid = left + (right - left) // 2

                if sorted_nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            start = left

            # return answer if x numbers >= x
            if len(sorted_nums) - start == x:
                return x

        return -1
