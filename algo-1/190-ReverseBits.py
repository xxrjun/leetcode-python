# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:

        # convert number to binary
        # and remove first two characters
        n = bin(n)[2:]

        # filled space with '0'
        n = '0' * (32 - len(n)) + n

        # return reverse number in integer
        return int(n[::-1], 2)
