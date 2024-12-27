# My solution for this Problem.....

class Solution:
    def swapKth(self, k, arr):
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # Swap the k-th element from the start with the k-th element from the end
        arr[k - 1], arr[-k] = arr[-k], arr[k - 1]

        return arr  # Return the modified array


