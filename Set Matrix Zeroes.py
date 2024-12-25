# My solution for this Problem.....


class Solution:
    def setMatrixZeroes(self, mat):
        # Time Complexity: O(m * n)      # Space Complexity: O(m + n)

        m, n = len(mat), len(mat[0])  # Dimensions of the matrix
        
        rows = []  # To store rows that need to be zeroed
        cols = []  # To store columns that need to be zeroed
        
        # Step 1: Identify rows and columns to be zeroed
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    if i not in rows:
                        rows.append(i)  # Add row index
                    if j not in cols:
                        cols.append(j)  # Add column index
                    
        # Step 2: Zero out rows
        for i in rows:
            for j in range(n):
                mat[i][j] = 0  # Set entire row to zero
                
        # Step 3: Zero out columns
        for j in cols:
            for i in range(m):
                mat[i][j] = 0  # Set entire column to zero

