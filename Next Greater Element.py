# My solution for this Problem.....

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
         # Time Complexity: O(n^2,)      # Space Complexity: O(n)
        # Initialize the length of the array
        l = len(arr)
        
        li = [-1] * l
        st = 0

        # Outer loop iterates over each element in the array
        while st < l - 1:
            ele = arr[st]
            pointer = st + 1
            
            # Inner loop to find the next greater element
            while pointer < l:
                if ele < arr[pointer]:  # If a greater element is found
                    li[st] = arr[pointer]  # Update the result list
                    break 
                  
                pointer += 1  # Move the pointer to the next element
            
            st += 1  # Move to the next element in the outer loop
            
        return li 
