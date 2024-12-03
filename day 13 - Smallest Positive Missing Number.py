class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        
        r=1
        for num in arr:
            if num==r:
                r+=1
            
            elif num > r:
                break
            
        return r