from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)

        minima=prices[0]
        maxima=prices[0]
        
        res=0
        i=0
        if n < 2:
            return 0
            
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
                
        return res