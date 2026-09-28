class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1  # 1. Calculate carry
            a = a ^ b             # 2. Add without carry
            b = carry             # 3. Set b to carry for next iteration
        return a
        