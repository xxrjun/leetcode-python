# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

    def backtrack(self, res: List[List[int]], cur_list: List[int], start: int,  n: int, k: int) -> None:
