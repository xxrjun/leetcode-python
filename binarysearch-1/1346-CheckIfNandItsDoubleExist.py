# 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)

        for n in sorted_arr:

            if n * 2 in sorted_arr or n / 2 in sorted_arr:
                # 0 * 2 = 0, 0 / 2 = 0
                # If number of zero is less than 2, it would not be true
                if n == 0 and sorted_arr.count(0) < 2:
                    continue

                return True

        return False
