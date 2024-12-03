def circularSubarraySum(arr):
    ##Your code here

    total = 0    
    currentMaxSum = 0
    currentMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
      
       
        currentMaxSum = max(currentMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currentMaxSum) 
        
        currentMinSum = min(currentMinSum + arr[i], arr[i])
        minSum = min(minSum, currentMinSum)
        
        total += arr[i]
    
    normalSum = maxSum
    circularSum = total - minSum
    
    if minSum == total:
        return normalSum
    
    return max(normalSum, circularSum)