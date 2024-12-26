# My solution for this Problem.....


class Solution:
    
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # Step 1: Transpose the matrix by swapping elements at (i, j) with (j, i).
        # Step 2: Reverse the rows of the transposed matrix to achieve a 90-degree anticlockwise rotation.
        # Time Complexity: O(n^2)	# Space Complexity: O(1)
        
        l = len(mat)  # Get the size of the matrix (assuming it's square).

        for i in range(l):  # Transposing the matrix.
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]  # Swap elements.

        up = 0  # Pointer to the top row.
        down = l - 1  # Pointer to the bottom row.

        while up < down:  # Reversing the rows.
            mat[up], mat[down] = mat[down], mat[up]  # Swap top and bottom rows.
            up += 1
            down -= 1



# Onether possible ways to solve the problem
# Method - 1
class Solution:
    
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # Step 1: Reverse the columns of the matrix. 
        # Step 2: Transpose the matrix by swapping elements at (i, j) with (j, i).
        # Time Complexity: O(n^2)	# Space Complexity: O(1)
        
        l = len(mat)  # Get the size of the matrix (assuming it's square).

        # Step 1: Reverse the columns of the matrix.
        for j in range(l):
            top = 0
            bottom = l - 1
            while top < bottom:  # Swap top and bottom elements in each column.
                mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]
                top += 1
                bottom -= 1

        # Step 2: Transpose the matrix.
        for i in range(l):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# Method - 2
class Solution:
    
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # Step 1: Create an empty matrix of the same size to store the rotated matrix.
        # Step 2: Populate the rotated matrix such that the element at mat[i][j] is placed in the correct rotated position (new_matrix[n-j-1][i]).
        # Step 3: Copy the rotated matrix back to the original matrix (in-place).
        # Time Complexity: O(n^2)	# Space Complexity: O(n^2)

        n = len(mat)

        # Step 1: Create a new empty matrix of the same size.
        rotated = [[0] * n for _ in range(n)]

        # Step 2: Fill the rotated matrix by placing elements in the correct positions.
        for i in range(n):
            for j in range(n):
                rotated[n-j-1][i] = mat[i][j]

        # Step 3: Copy the rotated matrix back into the original matrix.
        for i in range(n):
            for j in range(n):
                mat[i][j] = rotated[i][j]
