# My solution for this Problem.....

class Solution:
    
    # arr[] : the input array
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        # Time complexity: O(n)      # Space complexity: O(n)
        arr_set = set(arr)
        max_length = 0  # To store the maximum length of a consecutive subsequence
        
        # Step 2: Iterate through each number in the array
        for num in arr:
            # Check if the current number is the start of a sequence
            if num - 1 not in arr_set:  # O(1) lookup
                current_num = num
                current_length = 1
                
                # Step 3: Count consecutive numbers in the sequence
                # Time complexity for this inner loop: O(n) in total across all iterations
                while current_num + 1 in arr_set:  # O(1) lookup
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length if the current sequence is longer
                max_length = max(max_length, current_length)
        
        # Return the maximum length of a consecutive subsequence
        return max_length
