# My solution for this Problem.....


# User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # Time Complexity: O(n)      # Space Complexity: O(n)

        seen = set()  # Set to store values needed to complete the target sum

        for i in arr:  # Iterate through the array
            if i in seen:  # If current number is in the set, the pair is found
                return True
            else:
                seen.add(target - i)  # Add the required value to the set
        
        return False  # Return False if no pair is found
