class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        unique_elements = list(set(arr))
        if len(unique_elements) < 2:
            return -1
            
        unique_elements.sort(reverse=True)
        
        return unique_elements[1]