# 217. Contains Duplicate
# Idea:
#     1. 遇到過的數字放進 hash table 做查找

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for n in nums:
            if n in dict.keys():
              return True
            else:
              dict[n] = n

        return False