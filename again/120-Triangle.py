# 120. Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if len(triangle) < 1:
            return triangle[0]

        min_sum = triangle[0][0]
        last_choosen_idx = 0
        for i in range(1, len(triangle)):
            choosen_idx = 0
            if triangle[i][last_choosen_idx] > triangle[i][last_choosen_idx + 1]:
                choosen_idx = last_choosen_idx + 1
            else:
                choosen_idx = last_choosen_idx

            min_sum += triangle[i][choosen_idx]

            last_choosen_idx = choosen_idx

        return min_sum
