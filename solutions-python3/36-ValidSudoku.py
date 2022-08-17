# 36. Valid Sudoku
# Rules:
#       1. Each row must contain the digits 1-9 without repetition.
#       2. Each column must contain the digits 1-9 without repetition.
#       3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Idea:
#       
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        curSet = set()
        # Check row element first
        for r in range(rows):
            curSet.clear()  # reset the curSet each row
            for c in range(cols):
                if board[r][c] != ".":
                    number = board[r][c]

                    if number in curSet: return False

                    curSet.add(number)

        # Check col element
        for c in range(cols):
            curSet.clear()  # reset the curSet each col
            for r in range(rows):
                if board[r][c] != ".":
                    number = board[r][c]

                    if number in curSet: return False
                    
                    curSet.add(number)


        # Check nine 3*3 sub-boxes
        for rowStart in range(0, rows - 1, 3):
            for colStart in range(0, cols - 1, 3):
                curSet.clear()    # reset the curSet each sub-boxes
                for r in range(rowStart, rowStart + 3):
                    for c in range(colStart, colStart + 3):
                        if board[c][r] != ".":
                            number = board[c][r]
                            if number in curSet: return False
                            
                            curSet.add(number)

        return True