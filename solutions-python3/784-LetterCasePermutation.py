# 784. Letter Case Permutation


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        self.backtrack(res, s, "", 0)

        return res

    def backtrack(self, res: List[str], s: str, sub_str: str, startIdx: int) -> None:
        if len(sub_str) == len(s):
            res.append(sub_str)
            return

        for i in range(startIdx, len(s)):
            # 如果是字母，就將 uppercase 跟 lowercase 加到 cur_str 分別做 backtrack
            if s[i].isalpha():

                self.backtrack(res, s, sub_str + s[i].upper(), i + 1)
                self.backtrack(res, s, sub_str + s[i].lower(), i + 1)

            # 如果是數字，直接加到 cur_str 做 backtrack
            elif s[i].isdigit():
                self.backtrack(res, s, sub_str + s[i], i + 1)
