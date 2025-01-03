# My solution for this Problem....

class Solution:
    def subarrayXor(self, arr, k):
        # Time Complexity: O(n), where n is the length of the array.
        # Space Complexity: O(n), as we use a dictionary to store XOR values.

        map = {}
        ans = 0  
        xor = 0  
        for i in range(len(arr)):
            xor ^= arr[i]  # Compute the running XOR up to the current index.

            # If the current XOR equals k, it means the subarray from the start to this index has XOR k.
            if xor == k:
                ans += 1
            
            # Check if there exists a prefix with XOR equal to (xor ^ k). 
            # This ensures the subarray between this prefix and current index has XOR k.
            if xor ^ k in map:
                ans += map[xor ^ k]
            
            # Update the frequency of the current XOR in the dictionary.
            if xor not in map:
                map[xor] = 1
            else:
                map[xor] += 1
        
        return ans
