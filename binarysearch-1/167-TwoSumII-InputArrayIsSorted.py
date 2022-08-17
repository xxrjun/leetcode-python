# 167. Two Sum II - Input Array Is Sorted

class Solution:
    # Solution 1: Dictionary
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, n in enumerate(numbers):
            if n in hashTable.keys():
                return [hashTable[n] + 1, i + 1]
            hashTable[target - n] = i

        return None

    # Solution 2: Two Pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return None
