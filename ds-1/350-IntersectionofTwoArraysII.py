# 350. Intersection of Two Arrays II


class Solution:
    # Solution 1: Dictionary
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def getDict(nums: List[int]) -> Dict:
            dict = {}  # (number, counts)
            for n in nums:
                if n not in dict:
                    dict[n] = 1
                else:
                    dict[n] += 1

            return dict

        def findIntersection(dict: Dict, nums: List[int]) -> List[int]:
            intersection = []

            for n in nums:
                if n in dict.keys() and dict[n] > 0:
                    intersection.append(n)
                    dict[n] -= 1

            return intersection

        dict = getDict(nums1)

        return findIntersection(dict, nums2)

    # Solution 2: Two Pointers
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersection = []

        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                intersection.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1

        return intersection


"""
    Follow up:
        1. What if the given array is already sorted? How would you optimize your algorithm?
        2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
        3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load 
              all elements into the memory at once?
"""
