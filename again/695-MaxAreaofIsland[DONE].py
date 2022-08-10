# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        returnMaxArea = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    returnMaxArea = max(returnMaxArea, self.dfs(
                        grid, row, col))

        return returnMaxArea

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:

        # Check bound
        if row >= len(grid) or row < 0 or col >= len(grid[row]) or col < 0:
            return 0

        # Stop when encounter 0
        if grid[row][col] == 0:
            return 0

        # Set 1 to 0 after we count it
        grid[row][col] = 0

        count = 1

        count += self.dfs(grid, row + 1, col)
        count += self.dfs(grid, row - 1, col)
        count += self.dfs(grid, row, col + 1)
        count += self.dfs(grid, row, col - 1)

        return count
