# 344. Reverse String

#  Solution 1: Two Pointer (Slow, less memory usage)
#  Solution 2: One line python command (Faster, more memory usage)
class Solution:
    #  Solution 1: Two Pointer
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


    # #  Solution 2: One line python command
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
        
    #     # Why s[:] ? Because we need to modify in-place
    #     # Under the hood, s[:] = is editing the actual memory bytes s points to, #       and s = points the variable name s to other bytes in the memory.
    #     s[:] = s[::-1]