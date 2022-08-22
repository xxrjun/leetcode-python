# 1855. Maximum Distance Between a Pair of Values

class Solution:
    # Solution 1: Binary Search
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        # return the index the target should be at
        def binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        max_dist = 0

        for i, n in enumerate(nums2):
            idx = binary_search(nums1, n)

            if idx != len(nums1) and n >= nums1[idx]:
                max_dist = max(max_dist, (i - idx))
            else:
                # reach the end of nums1 or nums2[i] is not greater than nums1[idx]
                continue

        return max_dist

    # Solution 2: Two Pointers (Faster)
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        max_dist = 0

        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if p1 <= p2 and nums1[p1] <= nums2[p2]:
                max_dist = max(max_dist, (p2 - p1))
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return max_dist
