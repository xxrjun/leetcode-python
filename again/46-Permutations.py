# 46. Permutations

from tracemalloc import start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

    def backtrack(self, res: List[List[int]], nums: List[int], startIdx: int) -> None:
