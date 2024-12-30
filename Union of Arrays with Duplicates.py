# My solution for this Problem.....
class Solution:    
    def findUnion(self, a, b):
        # Time Complexity: O(n + m)      # Space Complexity: O(n + m)
        dit = {}
        
        # Add all elements from the first array to the dictionary
        for i in a:
            dit[i] = 1
        
        # Add elements from the second array only if they're not already in the dictionary
        for j in b:
            dit[j] = 1  # This works directly as `dit[j]` will be added if not present
        
        # The size of the dictionary represents the union count
        return len(dit)


#Method - 2

class Solution:    
    def findUnion(self, a, b):
        # Initialize an empty dictionary to store unique elements
        dit = {}
        
        # Traverse through the first array and add elements to the dictionary
        for i in a:
            dit[i] = 1  # Mark the element as seen
            
        # Traverse through the second array
        for j in b:
            # If the element is not already in the dictionary, add it
            if j not in dit.keys():
                dit[j] = 1
                
        # Return the count of unique elements (size of the dictionary)
        return len(dit)
