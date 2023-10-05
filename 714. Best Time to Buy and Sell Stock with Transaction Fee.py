class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        @cache
        def dp(i, hold):
            # 終止在走完
            if i == len(prices):
                return 0

            # pass
            value = dp(i + 1, hold)
            # 買
            if hold == False:
                value = max(value, -prices[i] + dp(i + 1, True))
            # 賣
            else:
                value = max(value, prices[i] - fee + dp(i + 1, False))

            return value

        return dp(0, False)


print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))  # 8
print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))  # 6
