# My solution for this Problem.....

class Solution:
    # Function to search a given number in a row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        n, m = len(mat), len(mat[0])  # Get matrix dimensions
        # Time Complexity: O(n * log m)		# Space Complexity: O(1)
        
        st = 0
        while st < n:
            li = mat[st]  # Access the current row
            
            # Perform binary search in the current row
            p1, p2 = 0, m - 1
            while p1 <= p2:
                mid = (p1 + p2) // 2
                
                if li[mid] == x:
                    return True
                elif li[mid] < x:
                    p1 = mid + 1
                else:
                    p2 = mid - 1
            
            st += 1  # Move to the next row
        
        return False
