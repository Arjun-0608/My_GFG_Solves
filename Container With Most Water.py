# My solution for this Problem....

class Solution:
    def maxWater(self, arr):
        #Time Complexity: O(n), where `n` is the length of the array `arr`.
        #Space Complexity: O(1), as no extra space is used apart from variables.
        
        l = len(arr)  # Length of the array.
        max_water = 0  # Variable to store the maximum water trapped.
        
        # Two-pointer approach: initialize pointers at the start and end of the array.
        st = 0
        end = l - 1

        # Continue until the two pointers meet.
        while st < end:
            # Calculate the water trapped between the current pair of lines.
            max_water = max(max_water, (end - st) * min(arr[st], arr[end]))
            
            # Move the pointer pointing to the shorter line.
            if arr[end] < arr[st]:
                end -= 1
            else:
                st += 1

        return max_water
