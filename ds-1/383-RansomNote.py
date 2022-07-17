# 383. Ransom Noteclass Solution:
# 

# Solution 1: Using set and count (Faster)
#       1. 比較 ransomNote 中特定字符之數量與 magazine 中特定字符之數量
# Solution 2: Using Hash Table (Slow)
#       1. 將 magazine 存入 hash table，(character, count)
#       2. loop magazine 去篩

class Solution:
    # Solution 1: Using set and count (Faster)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for character in set(ransomNote):
            if magazine.count(character) < ransomNote.count(character):
                return False

        return True

    # Solution 2: Using Hash Table (Slow)
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     hashTable = {}  # (character, count)

    #     for c in magazine:
    #         if c in hashTable.keys():
    #             hashTable[c] += 1
    #         else:
    #             hashTable[c] = 1

    #     for c in ransomNote:
    #         if c in hashTable.keys() and hashTable[c] >= 1:
    #             hashTable[c] -= 1
    #         else:
    #             return False

    #     return True


        
        