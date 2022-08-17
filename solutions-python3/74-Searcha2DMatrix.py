# 74. Search a 2D Matrix
# Idea:
#       1. Naive way: 對每一列作 Binary Search: O(logn * n)
#       2. Better way: 將 matrix 做 flatten，再做 Binary Search: O(n + logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for i in range (len(matrix)):
                flatten += matrix[i]
        
        return self.binarySearch(flatten, target) >= 0

    
    def binarySearch(self, arr: List[int], target) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return -1