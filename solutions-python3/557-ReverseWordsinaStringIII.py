# 557. Reverse Words in a String III

# Solution 1: Using built-in method, Double reverse, Faster
# Solution 2: Naive, Slow
#       1. 暫存空格前的字串，遇到空格將前方暫存的字串 reverse 並加入 returnString
#       2. 加入後將暫存之字串清空

class Solution:

    # Solution 1: Using built-in method, Double reverse, Faster
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]

    # # Solution 2: Naive, Slow
    # def reverseWords(self, s: str) -> str:
    #     returnString = ""
        
    #     curString = ""
    #     for i in range(len(s)):
    #         if s[i] == " ":
    #             returnString += curString[::-1]
    #             returnString += " "
    #             curString = ""  # clear curString
    #         elif i == len(s) - 1:
    #             curString += s[i]
    #             returnString += curString[::-1]
    #         else:
    #             curString += s[i]
        
    #     return returnString