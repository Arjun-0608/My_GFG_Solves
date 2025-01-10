# My solution for this Problem....

class Solution:
    def countDistinct(self, arr, k):
        #Time Complexity: O(n * k), where `n` is the length of the array and `k` is the size of the subarray.
        #Space Complexity: O(k), for the set to store elements of each subarray.

        arr_len = len(arr)  # Length of the input array.
        distincts = []  # List to store the count of distinct elements for each subarray.

        # Iterate through the array and calculate distinct elements for each subarray of size k.
        for i in range(arr_len - k + 1):
            distincts.append(len(set(arr[i : i + k])))  # Use `set` to find distinct elements.

        return distincts
