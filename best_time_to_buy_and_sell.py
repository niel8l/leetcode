from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        if len(prices) < 2:
            return r
        p = 0
        q = 1
        n = len(prices)
        while p < n - 1:
            while q < n:
                profit = prices[q] - prices[p]
                if profit > r:
                    r = profit
                q += 1
            p += 1
            q = p + 1
        return r


class Solution:  # NOQA
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        if len(prices) < 2:
            return r
        p = 0
        q = 1
        n = len(prices)
        while p < n - 1 and q < n:
            profit = prices[q] - prices[p]
            if profit > r:
                r = profit
            if profit > 0:
                q += 1
            else:
                p = q
                q = p + 1
        return r


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
