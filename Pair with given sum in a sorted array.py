# My solution for this Problem....

# User function Template for python3

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def countPairs(self, arr, target):
        mp = {}
        count = 0
        
        # Iterate through the array.
        for i in arr:
            # Calculate the required value to form a pair with the current element.
            temp = target - i
            
            # If the current element is already in the map, it forms a valid pair.
            if i in mp:
                count += mp[i]
            
            # Update the frequency of the required value in the hashmap.
            if temp in mp:
                mp[temp] += 1
            else:
                mp[temp] = 1
        
        return count
