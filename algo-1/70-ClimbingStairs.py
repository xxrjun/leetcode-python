# 70. Climbing Stairs


class Solution:

    # Dynamic Programming
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1, 2]

        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n - 1]
