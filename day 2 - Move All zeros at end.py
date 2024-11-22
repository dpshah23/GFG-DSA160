class Solution:
	def pushZerosToEnd(self,arr):
    	# code here

        n = len(arr)
        non_zero_index = 0

        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1

        for i in range(non_zero_index, n):
            arr[i] = 0

        return arr
