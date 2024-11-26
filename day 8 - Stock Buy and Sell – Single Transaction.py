class Solution:
    def maximumProfit(self, prices):
        # code here
        maxres=0
        min12=prices[0]
        
        for i in range(1,len(prices)):
            min12=min(min12,prices[i])
            
            maxres=max(maxres,prices[i]-min12)
            
        return maxres
                   