# 1. Two Sum
# Idea:
#     1. 將 (target - nums[i], i) 放入 Hash Table
#     2. 查找 number 是否在 Hash Table 的 keys 中即為答案
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnResult = [None] * 2
        hashTable = {}

        for i, number in enumerate(nums):
          if number in hashTable.keys():
            returnResult[0] = hashTable[number]
            returnResult[1] = i

          if number not in hashTable.keys():
            hashTable[target - number] = i
          

        return returnResult

  