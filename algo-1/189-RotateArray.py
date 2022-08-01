# 189. Rotate Array
# Two Solution:
#   1.  Reverse Array
#   2.  Python List Slicing

# Solution 1. Reverse Array (Faster):
#   1.  把整個 array reverse
#   2.  把 [0:k] reverse
#   3.  把 [k:] reverse
# Solution 2. List Alicing (More convenient?):
#   1.  把四種 cases 畫出來就可以找出規律
#   2.  result front (nums[:k]) 會是 nums[len(nums) - k:]
#       result back (nums[k:]) 會是 nums[:len(nums) -k]
#   3.  注意 k > len(nums) 的狀況，可以使用 mod %

class Solution:

    # Solution 1. Reverse array
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverseArray(nums, 0, len(nums) - 1)
        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, len(nums) - 1)

    # Helper function for Solution 1: Reverse Function
    def reverseArray(self, arr: List[int], startIndex: int, endIndex: int):
        left = startIndex
        right = endIndex
        while left <= right:
            self.swap(arr, left, right)
            left += 1
            right -= 1

    # Helper funcetion for Solution 1: Swap Function
    def swap(self, arr: List[int], index1: int, index2: int):
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp

    # Solution 2. List Slicing
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """

    #     if k == 0 or len(nums) <= 1:
    #         return

    #     k = k % len(nums)
    #     front = nums[len(nums) - k:]
    #     nums[k:] = nums[:len(nums) - k]
    #     nums[:k] = front
