# 278. First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# Idea:
#     1. 搭配 binary search

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        returnFisrBadVersion = n

        while left <= right:
          mid = (left + right) // 2
          if isBadVersion(mid):
            if mid < returnFisrBadVersion:
              returnFisrBadVersion = mid
            right = mid - 1
          elif:
            left = mid + 1

        return returnFisrBadVersion