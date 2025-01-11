# My solution for this Problem....

class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        #Time Complexity: O(n), where `n` is the length of the string `s`.
        #Space Complexity: O(k), where `k` is the size of the character set (e.g., 26 for lowercase English letters).
        
        res_set = set()  # Set to store unique characters in the current substring.
        res = 0  # Variable to track the maximum length of unique substring.
        l = 0  # Left pointer of the sliding window.
        n = len(s)  # Length of the input string.

        # Iterate through the string using the right pointer `i`.
        for i in range(n):
            # If the character `s[i]` is already in the set, remove characters from the left.
            while s[i] in res_set:
                res_set.remove(s[l])
                l += 1  # Move the left pointer to shrink the window.

            # Add the current character to the set.
            res_set.add(s[i])

            # Update the maximum length of the substring.
            res = max(res, i - l + 1)

        return res
