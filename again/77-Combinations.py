# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        self.backtrack(res, [],
                       1, n, k)

        return res

    def backtrack(self, res: List[List[int]], cur_list: List[int], start: int,  n: int, k: int) -> None:
        if len(cur_list) == k:
            res.append(cur_list.copy())
            return

        for i in range(start, n + 1):
            cur_list.append(i)
            self.backtrack(res, cur_list, i + 1, n, k)
            cur_list.remove(i)
