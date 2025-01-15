# My solution for this Problem....

# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        #Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(n), for storing prefix sums in a dictionary.
        
        # Dictionary to store the first occurrence of each prefix sum.
        prefix_sum_indices = {}
        current_sum = 0  # Variable to store the running sum of the array.
        max_length = 0   # Variable to store the maximum length of the subarray with sum `k`.
    
        # Iterate through the array.
        for index, value in enumerate(arr):
            # Update the running sum.
            current_sum += value
    
            # Check if the current sum itself is equal to `k`.
            if current_sum == k:
                max_length = index + 1  # Update the maximum length.

            # Check if there's a prefix sum such that removing it results in sum `k`.
            if (current_sum - k) in prefix_sum_indices:
                # Update the maximum length using the difference between indices.
                max_length = max(max_length, index - prefix_sum_indices[current_sum - k])
    
            # Store the first occurrence of the current prefix sum.
            if current_sum not in prefix_sum_indices:
                prefix_sum_indices[current_sum] = index
    
        return max_length
