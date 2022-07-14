# 1. Two Sum
# Idea:
#     1. 將 (target - nums[i], i) 放入 Hash Table
#     2. 查找 number 是否在 Hash Table 的 keys 中即為答案
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i, n in enumerate(nums):
          if n in hashTable.keys():
            return [hashTable[n], i]

          #  n not in hashTable.keys():
          hashTable[target - n] = i

  