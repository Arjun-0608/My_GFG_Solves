# My solution for this Problem....

# User function template for Python 3

class Solution:
    def productExceptSelf(self, arr):
        3Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(n), for storing the result array. Additional space usage is O(1) if we ignore the result array.
        
        length = len(arr)  # Length of the input array.
        result = [1] * length  # Initialize the result array with 1s.

        # Calculate the left product for each index.
        left_product = 1
        for i in range(length):
            result[i] = left_product  # Store the product of elements to the left of index `i`.
            left_product *= arr[i]   # Update the left product.

        # Calculate the right product for each index and multiply with the result array.
        right_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right_product  # Multiply with the product of elements to the right of index `i`.
            right_product *= arr[i]    # Update the right product.

        return result
