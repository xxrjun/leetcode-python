# 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Get the sum of each row and sort
        return sorted(range(len(mat)), key=lambda row: sum(mat[row]))[:k]
