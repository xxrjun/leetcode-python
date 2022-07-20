# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalCenterColor = image[sr][sc]

        # # starting pixel is already colored with given color,
        # # so no changes are made to the image.
        # if originalCenterColor == color:
        #     return image


        self.dfs(image, sr, sc, originalCenterColor, color)


        return image

    # helper function: dfs
    def dfs(self, image: List[List[int]], i: int, j: int, originalCenterColor: int, color: int):
        # out of bound
        if i >= len(image) or i < 0 or j >=len(image[i]) or j < 0:
            return 

        # Pixel's color is not the same as starting pixel's
        if image[i][j] != originalCenterColor:
            return 
            
        # Draw color
        image[i][j] = color

        # Traverse 4 directions
        self.dfs(image, i + 1, j, originalCenterColor, color)
        self.dfs(image, i - 1, j, originalCenterColor, color)
        self.dfs(image, i, j + 1, originalCenterColor, color)
        self.dfs(image, i, j - 1, originalCenterColor, color)
