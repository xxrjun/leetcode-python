# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startPixelColor = image[sr][sc]

        self.dfs(image, sr, sc, color, startPixelColor)

        return image

    def dfs(self, image: List[List[int]], row: int, col: int, color: int, startPixelColor: int) -> None:
        # check bound
        if row >= len(image) or row < 0 or col >= len(image[0]) or col < 0:
            return

        if image[row][col] != startPixelColor:
            return

        # Draw color
        image[row][col] = color

        # direction (row, col): right, left, down, up
        dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        self.dfs(image, row + dir[0][0], col +
                 dir[0][1], color, startPixelColor)
        self.dfs(image, row + dir[1][0], col +
                 dir[1][1], color, startPixelColor)
        self.dfs(image, row + dir[2][0], col +
                 dir[2][1], color, startPixelColor)
        self.dfs(image, row + dir[3][0], col +
                 dir[3][1], color, startPixelColor)
