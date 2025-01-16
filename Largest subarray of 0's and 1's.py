# My solution for this Problem....

class Solution:
    def maxLen(self, arr):
        #Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(n), for storing cumulative sums in a hash map.
        n = len(arr)  # Length of the array.

        # Convert 0s to -1 to handle subarrays with equal 0s and 1s.
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1

        hash_map = {}  # Dictionary to store the first occurrence of cumulative sums.
        cum_sum = 0    # Variable to track the cumulative sum.
        max_len = 0    # Variable to track the maximum length of subarray with sum 0.

        # Iterate through the array.
        for i in range(n):
            cum_sum += arr[i]  # Update the cumulative sum.
            
            # If the cumulative sum is 0, the subarray from the start to `i` has sum 0.
            if cum_sum == 0:
                max_len = i + 1

            # If the cumulative sum has been seen before, calculate the length of the subarray.
            if cum_sum in hash_map:
                max_len = max(max_len, i - hash_map[cum_sum])
            else:
                # Store the first occurrence of this cumulative sum.
                hash_map[cum_sum] = i

        return max_len
