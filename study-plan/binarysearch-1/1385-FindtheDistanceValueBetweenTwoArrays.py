# 1385. Find the Distance Value Between Two Arrays

class Solution:
    # Solution 1: Brute Force
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for n1 in arr1:
            valid = True
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count

    # Solution 2: Binary Search
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Sort arr2 to do binary search
        arr2.sort()

        # res would be return
        count = 0

        # loop arr1 and do binary search
        for n1 in arr1:
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if abs(n1 - arr2[mid]) <= d:
                    count -= 1  # this rount is invalid, to make count no change
                    break
                elif n1 > arr2[mid]:
                    # we want to find abs(n1 - arr[mid]) is smaller than d,
                    # so if arr1[i] > arr2[j], we just to find bigger num in arr2
                    left = mid + 1
                else:
                    right = mid - 1

            count += 1

        return count
