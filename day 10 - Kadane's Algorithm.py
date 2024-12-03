#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here

        best_sum = float('-inf')
        current_sum = 0
        
        for x in arr:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
            
        return best_sum