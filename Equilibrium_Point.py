# My solution for this Problem....

# User function Template for python3

class Solution:
    # Function to find the equilibrium point in the array.
    def findEquilibrium(self, arr):
        #Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(1), as no extra space is used apart from variables.
      
        l = len(arr)  # Length of the array.
        
        total = sum(arr)  # Calculate the total sum of the array.
        left = 0  # Initialize the sum of elements on the left to 0.

        # Iterate through the array to find the equilibrium point.
        for i in range(l):
            # Calculate the sum of elements on the right.
            right = total - left - arr[i]
            
            # Check if the left and right sums are equal.
            if right == left:
                return i  # Return the equilibrium index.

            # Update the left sum by adding the current element.
            left += arr[i]
        
        # If no equilibrium index is found, return -1.
        return -1
