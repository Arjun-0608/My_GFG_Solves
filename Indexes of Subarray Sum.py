# My solution for this Problem....

# User function Template for Python3

class Solution:
    def subarraySum(self, arr, target):
        #Time Complexity: O(n), where n is the size of the array.
        #Space Complexity: O(n), due to the hash map.

        n = len(arr)
        mp = {0: 0}  # Hash map to store prefix sums and their indices.
        prefix = 0   # Initialize prefix sum.
        
        for i in range(n):
            prefix += arr[i]  # Update prefix sum with the current element.
            
            # Check if there exists a subarray with the given target sum.
            if prefix - target in mp:
                return [mp[prefix - target] + 1, i + 1]  # Return 1-based indices.
            
            # Store the current prefix sum with its 1-based index.
            mp[prefix] = i + 1
        
        return [-1]
