# My solution for this Problem....

# User function Template for Python3

class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        #Time Complexity: O(n^2), where n is the number of elements in the array.
        #Space Complexity: O(1), as no additional space is used apart from variables.
      
        arr.sort()
        n = len(arr)
        count = 0
    
        # Fix the largest side as arr[k].
        for k in range(2, n):
            i, j = 0, k - 1  # Start with the smallest and second-largest sides.
            
            # Use a two-pointer approach to check pairs (i, j).
            while i < j:
                # Check if arr[i] + arr[j] > arr[k].
                if arr[i] + arr[j] > arr[k]:
                    # All pairs from i to j will satisfy the triangle condition.
                    count += (j - i)
                    j -= 1  # Decrease j to try smaller pairs.
                else:
                    i += 1  # Increase i to try larger pairs.
    
        return count
