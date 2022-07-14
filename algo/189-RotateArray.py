# 189. Rotate Array
# Idea & Step:
#   1.  把四種 cases 畫出來就可以找出規律
#   2.  result front (nums[:k]) 會是 nums[len(nums) - k:]
#       result back (nums[k:]) 會是 nums[:len(nums) -k]
#   3.  注意 k > len(nums) 的狀況，可以使用 mod %


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
      Do not return anything, modify nums in-place instead.
      """

        self.reverse_array(nums, 0, len(nums), k)

    def reverse_array(self, nums, start, end, k):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        if len(nums) > 1:

            k = k % len(nums)

            self.reverse_array(len(nums) - k, len(nums) - 1)
            self.reverse_array(0, len(nums) - (k + 1))
            self.reverse_array(0, len(nums) - 1)

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