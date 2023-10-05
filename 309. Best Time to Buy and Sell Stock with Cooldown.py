class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 分解
        # -> 買
        # -> 賣
        # -> 休息
        # -> 跳過

        statusProcess = ["可買", "可賣", "休息"]

        @cache
        def dp(priceIndex, statusIndex):
            if priceIndex == len(prices):
                return 0

            value = dp(priceIndex + 1, statusIndex)
            if statusIndex == 2:
                value = dp(priceIndex + 1, 0)
            if statusIndex == 0:
                value = max(value, -prices[priceIndex] + dp(priceIndex + 1, 1))
            if statusIndex == 1:
                value = max(value, prices[priceIndex] + dp(priceIndex + 1, 2))
            return value

        return dp(0, 0)
