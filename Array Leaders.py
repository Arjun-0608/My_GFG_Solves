# My solution for this Problem....

class Solution:
    def leaders(self, arr):
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        l = len(arr)
        max_ele = arr[-1]  # Start by considering the last element as the maximum.
        res = [max_ele]  # The last element is always a leader.

        # Traverse the array from right to left.
        for i in range(-2, -l - 1, -1):  # Using negative indexing to move from right to left.
            if arr[i] >= max_ele:  # If the current element is greater than or equal to the max seen so far:
                res.append(arr[i])
                max_ele = arr[i]

        return res[::-1]  # Reverse the result to maintain the original order of leaders.
