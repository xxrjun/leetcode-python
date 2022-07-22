# 118. Pascal's Triangle
class Solution:
    # Solution 1: Recursion
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            curLastRow = [0] + res[i - 1] + [0]  # add 0 front and back
            left, right = 0, 1   # two pointers to the two numbers would be added

            curRow = []
            while right < i + 2:
                curRow += [curLastRow[left] + curLastRow[right]]
                left += 1
                right += 1

            res += [curRow]

        return res

    # Solution 2: Dynamic Programming
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for r in range(1, numRows):
            curRow = [1]

            for i in range(1, r):
                curRow.append(res[r - 1][i - 1] + res[r - 1][i])

            curRow.append(1)

            res.append(curRow)

        return res
