# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        returnMaxValue = 0     # Initialize the max value of area of island

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # encounter island
                if grid[i][j] == 1:
                    # update maxumum value
                    returnMaxValue = max(returnMaxValue, self.dfs(grid, i, j))


        return returnMaxValue

    
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:

        # out of bound
        if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
            return 0
        
        # encounter water
        if grid[i][j] == 0:
            return 0

        
        grid[i][j] = 0  # set the area we encoutered to 0
        count = 1

        # traverse 4 direction
        count += self.dfs(grid, i + 1, j)
        count += self.dfs(grid, i - 1, j)
        count += self.dfs(grid, i, j + 1)
        count += self.dfs(grid, i, j - 1)


        return count

