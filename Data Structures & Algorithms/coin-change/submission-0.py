class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        a = 1
        while a <= amount:
            i = 0
            while i < len(coins):
                c = coins[i]
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                i += 1
            a += 1

        return dp[amount] if dp[amount] != amount + 1 else -1