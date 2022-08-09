# 120. Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 在原有三角形下面以一排 0 作為開始
        dp = [0] * (len(triangle) + 1)

        # 每列由下而上去算出最小總和
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        # 最後的頂端就會是 minimum total
        return dp[0]
