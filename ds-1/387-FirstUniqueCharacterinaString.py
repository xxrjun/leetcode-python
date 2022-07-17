# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashTable = {}  # (character, index)

        for i, c in enumerate(s):
            if c in hashTable.keys():
                hashTable[c] = -1
            else:
                hashTable[c] = i

        minIndex = len(s)
        for key in hashTable.keys():
            if hashTable[key] != -1:
                minIndex = min(minIndex, hashTable[key])

        if minIndex == len(s):
            minIndex = -1

        return minIndex