# My solution for this Problem.....

class Solution:
    # Function to find the intersection of two arrays, considering duplicates.
    # Time Complexity: O(n + m)      # Space Complexity: O(n)
    def intersectionWithDuplicates(self, a, b):
        # Dictionary to store the count of elements in array 'a'
        dit = {}
        
        # Populate the dictionary with elements from array 'a'
        for i in a:
            dit[i] = 1
        
        # Iterate through array 'b' and update counts in the dictionary if the element exists
        for j in b:
            if j in dit:
                dit[j] += 1
        
        # Initialize the result list to store the intersection elements
        res = []
        
        # Iterate through the dictionary to find elements appearing in both arrays
        for i, j in dit.items():
            if j >= 2:  # If the count is 2 or more, it means the element exists in both arrays
                res.append(i)
        
        # Return the result list
        return res
