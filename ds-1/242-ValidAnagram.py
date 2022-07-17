# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for character in set(s):
            if s.count(character) != t.count(character): 
                return False

        return True