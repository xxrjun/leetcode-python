# 46. Permutations

# Solution 1. Using visited
class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        self.backtrack(res, nums, [], visited)

        return res

    def backtrack(self, res: List[List[int]], nums: List[int], cur_list: List[int], visited: List[int]) -> None:

        # 滿足條件，將 path 加入 res
        if len(cur_list) == len(nums):
            res.append(cur_list)

        # Decision tree
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(res, nums, cur_list + [nums[i]], visited)
                visited.remove(i)


# Solution 2. Using Swap
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.backtrack(res, nums, 0)

        return res

    def backtrack(self, res: List[List[int]], nums: List[int], startIdx: int) -> None:
        if startIdx == len(nums):
            res.append(nums.copy())
            return

        # Decision tree
        for i in range(startIdx, len(nums)):
            # 做選擇，將選到的放到前面，沒選到的放後面
            nums[startIdx], nums[i] = nums[i], nums[startIdx]

            self.backtrack(res, nums, startIdx + 1)

            # 撤銷選擇，放回去
            nums[startIdx], nums[i] = nums[i], nums[startIdx]
