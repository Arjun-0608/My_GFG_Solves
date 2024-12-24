# My solution for this Problem.....

# User function Template for python3

class Solution:
    # Function to search a given number in a row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # Time Complexity: O(m + n)        # Space Complexity: O(1)
      
        m, n = len(mat), len(mat[0])  # Dimensions of the matrix
        st, end = 0, n - 1  # Start at the top-right corner

        while st < m and end >= 0:
            ele = mat[st][end]  # Current element

            if ele == x:  # Element found
                return True
              
            elif ele > x:  # Move left if the current element is too large
                end -= 1
              
            else:  # Move down if the current element is too small
                st += 1

        return False  # Element not found

