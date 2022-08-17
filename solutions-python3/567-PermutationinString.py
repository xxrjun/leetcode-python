# 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 1. 將 s1 放入 hash table (chracter, count)
        hashTable = {}
        for c in s1:
            if c in hashTable.keys():
                hashTable[c] += 1
            else:
                hashTable[c] = 1

        # 2. Iterate s2，遇到存在在 hashTable 的元素就開始進行比對
        startIdx = 0
        while startIdx <= len(s2) - len(s1):
            if s2[startIdx] in hashTable.keys():
                hashTableCopy = hashTable.copy()
                checkCount = 0

                for i in range(startIdx, startIdx + len(s1)):
                    if s2[i] in hashTableCopy.keys() and hashTableCopy[s2[i]] > 0:
                        hashTableCopy[s2[i]] -= 1
                        checkCount += 1
                    else:
                        break

                if checkCount == len(s1):
                    return True

            startIdx += 1

        return False
