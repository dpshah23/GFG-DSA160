class Solution:
    def getMinDiff(self, arr, k):
        # Number of towers
        n = len(arr)
        if n == 1:
            return 0  
            
        arr.sort()

        res = arr[n - 1] - arr[0]

        for i in range(1, n):
        
            if arr[i] - k < 0:
                continue

            minH = min(arr[0] + k, arr[i] - k)
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        
            res = min(res, maxH - minH)

        return res
