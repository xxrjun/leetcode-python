# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            rob1 代表前面可以 rob 的 max total
            rob2 代表當前 house 的前一間 house 可以 rob 的 max total (若要 rob 當前 house 就不可算入 rob2)
        """
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = rob1 + n
            rob1 = rob2
            rob2 = max(rob2, tmp)

        return rob2
