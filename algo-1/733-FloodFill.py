# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalCenterColor = image[sr][sc]

        # # starting pixel is already colored with given color,
        # # so no changes are made to the image.
        if originalCenterColor == color:
            return image

        self.dfs(image, sr, sc, originalCenterColor, color)

        return image

    # helper function: dfs
    def dfs(self, image: List[List[int]], row: int, col: int, originalCenterColor: int, color: int):
        # out of bound
        if row >= len(image) or row < 0 or col >= len(image[row]) or col < 0:
            return

        # Pixel's color is not the same as starting pixel's
        if image[row][col] != originalCenterColor:
            return

        # Draw color
        image[row][col] = color

        # Traverse 4 directions
        self.dfs(image, row + 1, col, originalCenterColor, color)
        self.dfs(image, row - 1, col, originalCenterColor, color)
        self.dfs(image, row, col + 1, originalCenterColor, color)
        self.dfs(image, row, col - 1, originalCenterColor, color)
