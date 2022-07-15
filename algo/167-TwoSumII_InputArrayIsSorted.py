# 167. Two Sum II - Input Array Is Sorted
# Idea:
#       1. Using Hash Table store pair (target - number, index)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashTable = {}
        returnResult = [0] * 2
        for i, n in enumerate(numbers):
            if n in hashTable.keys():
                returnResult[0] = hashTable[n] + 1
                returnResult[1] = i + 1
                return returnResult

            hashTable[target - n] = i

        return None