# My solution for this Problem....

# User function Template for python3

class Solution:
    def findTwoElement(self, arr):
        #Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(n), for storing the unique elements of the array in a set.
        n = len(arr)
        
        # Calculate the sum of unique elements in the array.
        total = sum(set(arr))
        
        # Calculate the expected sum of the first `n` natural numbers.
        actual_sum = (n * (n + 1)) // 2
        
        # The missing number is the difference between the expected sum and the unique elements' sum.
        missing = actual_sum - total
        
        # Calculate the sum of all elements in the array.
        doubled_sum = sum(arr)
        
        # The duplicate number is the difference between the array's sum and the unique elements' sum.
        duplicate = doubled_sum - total
        
        return [duplicate, missing]
