# 441. Arranging Coins

class Solution:
    # Solution 1: Brute Force
    def arrangeCoins(self, n: int) -> int:
        for i in range(n + 1):
            n -= i
            if n < 0:
                return i - 1
            elif n == 0:
                return i

    # Solution 2: Binary Search
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            temp = int(mid * (mid + 1) / 2)

            if temp == n:
                return mid
            elif temp < n:
                left = mid + 1
            else:
                right = mid - 1

        return left
