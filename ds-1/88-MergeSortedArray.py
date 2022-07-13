# 88. Merge Sorted Array
# Idea:
#     Solution 1. Two pointers (Slower): Using two pointer to fill nums1 from back to head
#     Solution 2 (Faster). Merge two array and do quick sort
class Solution:
    # Solution 1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # pointer for nums1
        p2 = n - 1  # pointer for nums2

        for i in range(m + n - 1, -1, -1):
          if p2 < 0:
            break

          if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
          else:
            nums1[i] = nums2[p2]
            p2 -= 1
            

    # Solution 2
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m != 0 and n != 0:
          nums1[0:m+n] = nums1[0:m] + nums2[0:n]
        elif m == 0 and n != 0:
          nums1[0:n] = nums2
        elif m != 0 and n == 0:
          nums1 = nums1

        self.quickSort(nums1, 0, len(nums1) - 1)
        

        
    # Quick sort function
    def quickSort(self, data, left, right):
        if left >= right:
          return
      
        i = left
        j = right
        key = data[left]

        while i != j:
            while data[j] > key and i < j:
              j -= 1
            while data[i] <= key and i < j:
              i += 1
            if i < j:
              data[i], data[j] = data[j], data[i]

        data[left] = data[i]
        data[i] = key

        self.quickSort(data, left, i - 1)
        self.quickSort(data, i + 1, right)


