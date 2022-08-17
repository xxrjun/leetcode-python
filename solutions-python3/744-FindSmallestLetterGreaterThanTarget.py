# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Doing Binary Search
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] == target:
                left = mid + 1
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Check bounder, because the letters wrap around, if out of bound, just return the first letter
        return letters[left] if left <= len(letters) - 1 else letters[0]
