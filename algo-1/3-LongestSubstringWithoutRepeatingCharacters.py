# Solution 1 (Faster)
class Solution:

    # Solution 1 (Faster)
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ''
        maxLength = 0

        for c in s:
            if c not in seen:
                seen += c
            else:
                maxLength = max(maxLength, len(seen))
                seen = seen[seen.index(c) + 1:] + c

        # Fix the case that array has non-repeating elements
        return max(maxLength, len(seen))

    # Solution 2 (Naive, Very Slow, O(n)): Nested for loop
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1

        visitedTable = []
        maxLength = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in visitedTable:
                    visitedTable += [s[j]]  # add new number into visited table
                else:   # ecnounter repeating characters
                    maxLength = max(maxLength, len(visitedTable))

                    visitedTable = []   # reset visited table

                    break

        return maxLength
