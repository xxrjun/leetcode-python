# 53. Maximum Subarray
# Idea:
#   1. 從正數當起點 
#   2. sum 小於 0 就換起點

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = - sys.maxsize - 1
        for n in nums:
          sum += n
          maxSum = max(maxSum, sum)
          if sum < 0: sum = 0

        return maxSum
