# 633. Sum of Square Numbers

class Solution:
    # Solution 1: Two Pointers
    def judgeSquareSum(self, c: int) -> bool:
        end = int(c ** 0.5)
        p1, p2 = 0, end

        while p1 <= p2:
            sum = p1 ** 2 + p2 ** 2
            if sum == c:
                return True
            elif sum > c:
                p2 -= 1
            else:
                p1 += 1

        return False

    # Solution 2: Binary Search (Pretty Slower)
    def judgeSquareSum(self, c: int) -> bool:

        def binary_search(start: int, end: int, target: int) -> bool:
            left, right = start, end
            while left <= right:
                mid = left + (right - left) // 2

                if mid ** 2 == target:
                    return True
                elif mid ** 2 > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return False

        end = int(c ** 0.5)
        for i in range(end, -1, -1):
            remain = c - i ** 2
            if binary_search(start=0, end=i, target=remain):
                return True

        return False
