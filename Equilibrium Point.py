# My solution for this Problem....

def find_equilibrium_point(arr):
    # Time Complexity: O(n)      # Space Complexity: O(1)

    total_sum = sum(arr)  # Calculate the total sum of the array
    left_sum = 0          # Initialize left_sum as 0
    
    # Iterate through the array to find the equilibrium point
    for i in range(len(arr)):
        # Calculate the right sum as total_sum - left_sum - arr[i]
        right_sum = total_sum - left_sum - arr[i]
        
        # Check if left_sum is equal to right_sum
        if left_sum == right_sum:
            return i + 1  # Return 1-based index
        
        # Update left_sum to include the current element
        left_sum += arr[i]
      
    return -1  

