# My solution for this Problem....

class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)

    # Function to count pairs with sum less than the target
    def countPairs(self, arr, target):
        arr.sort()  # Sort the array to enable the two-pointer approach.
        l = len(arr)  # Length of the array.

        st = 0
        end = l - 1

        count = 0

        # Iterate until the two pointers meet.
        while st < end:
            # If the sum of the pair is less than the target.
            if arr[st] + arr[end] < target:
                count += end - st  # All pairs from st to end are valid.
                st += 1  # Move the start pointer forward.
            else:
                end -= 1  # Reduce the end pointer if the sum is not less.

        return count
