# My solution for this Problem....

# User function Template for python3
class Solution:
    # Time Complexity: O(n log n), where n is the length of the array. Sorting takes O(n log n), and the two-pointer traversal takes O(n).
    # Space Complexity: O(1)

    def sumClosest(self, arr, target):
        # If the array has less than two elements, return an empty result.
        if len(arr) < 2:
            return []
        
        # Sort the array to use the two-pointer approach.
        arr.sort()
        
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')  # Track the closest sum to the target.
        res = []
        
        # Traverse the array using the two pointers.
        while left < right:
            current_sum = arr[left] + arr[right]
            
            # Update the closest sum and result if the current sum is closer to the target.
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                res = [arr[left], arr[right]]
            # If two sums are equally close, prioritize the pair with the larger difference.
            elif abs(target - current_sum) == abs(target - closest_sum):
                if (arr[right] - arr[left]) > (res[1] - res[0]):
                    res = [arr[left], arr[right]]
            
            # Move pointers to explore other pairs.
            if current_sum < target:
                left += 1  # Move the left pointer right to increase the sum.
            else:
                right -= 1  # Move the right pointer left to decrease the sum.
        
        return res
