# 977. Squares of a Sorted Array
# Idea:
#     1. 使用前後兩個 pointer，並比較兩絕對值
#     2. 比較大的做 squaring 並放到 result array 後面


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        index = len(nums) - 1
        left, right = 0, len(nums) - 1  # front and back pointer
        returnResult = [0] * len(nums)

        while index >= 0:
            if abs(nums[left]) > abs(nums[right]):
                returnResult[index] = nums[left]**2
                left -= 1
            else:
                returnResult[index] = nums[right]**2
                right += 1

            index -= 1

        return returnResult
