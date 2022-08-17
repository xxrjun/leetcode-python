# 20. Valid Parentheses


class Solution:

    def isValid(self, s: str) -> bool:
        dict = {"(": ")", "{": "}", "[": "]"}

        stack = []  # Be used to store "(", "{", "["

        # loop through our string
        for i in range(len(s)):
            if s[i] in dict.keys():
                stack.append(s[i])
            else:
                # If we has ")", "}", "]", but stack is empty.
                # It means open brackets is not closed by the same type of brackets
                if len(stack) == 0:
                    return False

                # Open brackets is not closed in the correct order
                if s[i] != dict[stack.pop()]:
                    return False

        # stack remain means open brackets is not closed by the same type of brackets
        if len(stack) != 0:
            return False

        return True
