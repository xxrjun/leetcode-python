# 191. Number of 1 Bits

class Solution:
    # Solution 1. Mod and Move
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n % 2
            n = n >> 1

        return count

    # Solution 2.
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += 1
            n &= (n - 1)

        return count
