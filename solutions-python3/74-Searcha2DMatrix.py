# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the flatten matrix
        flatten = []
        for row in matrix:
            flatten += row

        # doing binary search
        left, right = 0, len(flatten) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if flatten[mid] == target:
                return True
            elif flatten[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
