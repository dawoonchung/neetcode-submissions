class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = -1
        profit = 0

        for price in prices:
            if prev < 0:
                prev = price
                continue
            
            if price < prev:
                prev = price
                continue
            
            if (price - prev) > profit:
                profit = price - prev

        return profit
                