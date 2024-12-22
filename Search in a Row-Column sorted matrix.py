# My solution for this Problem.....

class Solution:
    def matSearch(self, mat, x):
        # Step 1: Get the dimensions of the matrix.
        # 'n' is the number of rows and 'm' is the number of columns.
        n, m = len(mat), len(mat[0])

        # Step 2: Start searching from the top-right corner of the matrix.
        # Time Complexity: O(n + m)	# Space Complexity: O(1)
        st = 0
        end = m - 1

        # Step 3: Traverse the matrix using the row and column pointers.
        while st < n and end >= 0:
            # If the current element matches the target, return 1 (element found).
            if mat[st][end] == x:
                return 1

            # If the current element is greater than the target, move left.
            # This is because all elements to the left in the same row are smaller.
            if mat[st][end] > x:
                end -= 1

            # Otherwise, move down. This is because all elements below in the same column are larger.
            else:
                st += 1

        # Step 4: If the entire matrix is traversed and the target is not found,
        return 0
