# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        self.backtrack(res, [], 1, n, k)

        return res

    def backtrack(self, res: List[List[int]], cur_list: List[int], start: int,  n: int, k: int) -> None:
        # 路徑內個數達條件，新增至 res 並中止
        if len(cur_list) == k:
            res.append(cur_list.copy())
            return

        for i in range(start, n + 1):
            cur_list.append(i)  # 做選擇
            self.backtrack(res, cur_list, i + 1, n, k)
            cur_list.pop()  # 撤銷選擇
