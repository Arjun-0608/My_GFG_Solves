# My solution for this Problem....

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    # Function to rotate a linked list.
    def rotate(self, head, k):

        #Time Complexity: O(n), where `n` is the number of nodes in the linked list.
        #Space Complexity: O(1), as no extra space is used apart from a few variables.
        
        # Edge case: If the list is empty or has only one node, or if `k` is 0.
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Count the number of nodes in the list.
        count = 1  # Start with 1 as we are already at `head`.
        current = head
        while current.next:
            current = current.next
            count += 1
        
        # Step 2: Handle cases where `k` is larger than the length of the list.
        k = k % count
        if k == 0:  # If `k` is a multiple of the list length, no rotation is needed.
            return head
        
        # Step 3: Traverse to the (count - k)th node to break the list.
        current = head
        for _ in range(count - k - 1):  # Stop one node before the split point.
            current = current.next
        
        # Step 4: Adjust the links to perform the rotation.
        new_head = current.next  # The new head is the (count - k)th node's next.
        current.next = None  # Break the link to make two separate lists.
        
        # Step 5: Connect the end of the second list to the original head.
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        
        return new_head
