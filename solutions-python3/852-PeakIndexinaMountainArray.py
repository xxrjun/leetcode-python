# 852. Peak Index in a Mountain Array

# Find i where arr[i - 1] < arr[i] > arr[i + 1]

class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                # peek in mountain
                return mid
            elif (arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]) or mid == 0:
                # mountain going up
                left = mid + 1
            elif (arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]) or mid == len(arr):
                # mountain going down
                right = mid - 1

        return -1
