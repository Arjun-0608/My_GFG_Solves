# My solution for this Problem....

# User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Time Complexity: O(n), where `n` is the length of the array.
        #Space Complexity: O(k), where `k` is the number of unique elements in the array.
    
        # Special case: if the array has only one element, it is the majority element.
        if len(arr) == 1:
            return arr[0]
        
        # Dictionary to store the frequency of each element.
        dit = {}

        # Count the frequency of each element in the array.
        for i in arr:
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1

        # Check if any element appears more than n // 2 times.
        for key, val in dit.items():
            if val > (len(arr) // 2):
                return key

        # If no majority element is found, return -1.
        return -1
