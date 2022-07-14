# 118. Pascal's Triangle
class Solution:
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
