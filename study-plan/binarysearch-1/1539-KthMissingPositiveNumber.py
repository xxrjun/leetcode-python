# 1539. Kth Missing Positive Number

class Solution:
    # Solution 1: Cool
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 小於 K 的算 not missing nubmer
        # Not missing number 會讓 k 增加，因為我們要算的是 Kth missing number
        for n in arr:
            if n <= k:
                k += 1
            else:
                break

        return k

    # Solution 2: Binary Search (Faster)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k

    # Solution 3: Brute Force and Easy understand
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k

        # make array to set for better searching performance
        arr_set = set(arr)

        # iterate 1 to the last number in array
        i = 1
        while i < arr[len(arr) - 1]:
            # if i is not in arr_set, it means i is a missing number
            if i not in arr_set:
                k -= 1

            # find kth missing number when k is equal to 0
            if k == 0:
                return i

            i += 1

        while k > 0:
            k -= 1
            i += 1

        return i
