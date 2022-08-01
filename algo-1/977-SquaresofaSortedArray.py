# 977. Squares of a Sorted Array
# Idea:
#     1. 如果陣列第一個數字是正數就直接全部做 square. O(n)
#     2. 如果陣列第一個數字是負數就用兩個 pointer 指前與後
#     3. 前後都是負數就做 square 並由倒序排，
#     4. 前負後正的話就做做 square 比較後由後往前排
#        直到前面的數字為正就可以把剩下的做 square 就好


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        index = len(nums) - 1
        left, right = 0, len(nums) - 1  # front and back pointer
        returnResult = [0] * len(nums)

        while index >= 0:
            if abs(nums[left]) > abs(nums[right]):
                returnResult[index] = nums[left]**2
                left += 1
            else:
                returnResult[index] = nums[right]**2
                right -= 1

            index -= 1

        return returnResult
