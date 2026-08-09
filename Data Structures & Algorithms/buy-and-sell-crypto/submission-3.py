class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        profit = 0
        diff = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                diff = prices[r] - prices[l]
                profit = max(profit, diff)
            else:
                l += 1
            r += 1
        r-=1
        while l != r:
            if prices[l] <= prices[r]:
                diff = prices[r] - prices[l]
                profit = max(profit, diff)
            l += 1
        return profit
               