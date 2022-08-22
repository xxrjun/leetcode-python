# 566. Reshape the Matrix
# Solutions:
#       1. Faster
#       2. Slower (Easy to understand)


# Solution 1:
#       1. 將原本的 matrix 做 flatten，並搭配 curRow 將 element 放入要回傳的 matrix
# Solution 2:
#       1. 找出原本的 row, col
#       2. 檢查給定的 r, c 是不是 possible and legal (length == r*c)，
#          不是的話回傳原本的 matrix。
#       3. 是的話依照給定的 r, c 做 matrix 並將數字填入

class Solution:
    # Solution 1: O(originRows * r)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        originRows = len(mat) # get the origin matrix's row
        originCols = len(mat[0])  # get the origin matrix's col

        # not possible or not legal
        if originRows * originCols != r * c or r <= 0 or c <= 0:  
            return mat
        
        # same matrix
        if originRows == r and originCols == c:
            return mat

        
        flatten = []
        for curRow in range(originRows):
            flatten += mat[curRow]
        
        returnMatrix = [flatten[curRow * c : curRow * c + c] for curRow in range(r)]

        return returnMatrix



    # Solution 2
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     originRows = len(mat) # get the origin matrix's row
    #     originCols = len(mat[0])  # get the origin matrix's col

    #     # not possible or not legal
    #     if originRows * originCols != r * c or r <= 0 or c <= 0:  
    #         return mat
        
    #     # same matrix
    #     if originRows == r and originCols == c:
    #         return mat

    #     returnMatrix = [[0] * c for i in range(r)]
    #     curRow = 0
    #     curCol = 0
    #     for oneRow in mat:
    #         for element in oneRow:
    #             returnMatrix[curRow][curCol] = element
    #             curCol += 1

    #             if curCol == c:
    #                 curRow += 1
    #                 curCol = 0



    #     return returnMatrix