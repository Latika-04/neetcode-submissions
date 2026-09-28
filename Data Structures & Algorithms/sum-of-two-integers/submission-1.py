class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask of all 1s (0b1111...1111)

        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # If b & mask is 0, 'a' contains our result.
        # If 'a' is positive, (a & mask) gives the value.
        # If 'a' is negative, we map the 32-bit unsigned integer back to signed.
        return (a & mask) if b > 0 else a