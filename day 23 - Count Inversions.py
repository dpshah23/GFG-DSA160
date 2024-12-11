class Solution:
    #User function Template for python3
    #Function to count inversions in the array.

    def merge_and_count(arr, temp, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp[i]

        return inv_count

    @staticmethod
    def merge_sort_and_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += Solution.merge_sort_and_count(arr, temp, left, mid)
            inv_count += Solution.merge_sort_and_count(arr, temp, mid + 1, right)
            inv_count += Solution.merge_and_count(arr, temp, left, mid, right)
        return inv_count

    def inversionCount(self, arr):
        n = len(arr)
        temp = [0] * n
        return Solution.merge_sort_and_count(arr, temp, 0, n - 1)
