# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        # doing binary search in each row, find the first negative idx and get the total of negative numbers
        for row in grid:
            idx = self.bs_non_increasing(row)
            if idx != -1:
                count += len(row) - idx

        return count

    def bs_non_increasing(self, row: List[int]) -> int:
        left, right = 0, len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if (mid - 1 >= 0 and row[mid] < 0 and row[mid - 1] >= 0) or (mid == 0 and row[mid] < 0):
                return mid
            elif row[mid] >= 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1
