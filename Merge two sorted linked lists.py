# My solution for this Problem....

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        #Time Complexity: O(n + m), where `n` and `m` are the lengths of the two linked lists.
        #Space Complexity: O(1), as no extra space is used other than a few pointers.
        
        # Create a dummy node to act as the starting point of the merged list.
        dummy = Node(0)
        current = dummy  # Pointer to build the merged list.

        # Traverse both lists until one is exhausted.
        while head1 and head2:
            if head1.data <= head2.data:
                # If the current node in the first list is smaller or equal, add it to the merged list.
                current.next = head1
                head1 = head1.next  # Move to the next node in the first list.
            else:
                # Otherwise, add the current node from the second list to the merged list.
                current.next = head2
                head2 = head2.next  # Move to the next node in the second list.
            current = current.next  # Move the pointer of the merged list forward.

        if head1:
            current.next = head1

        if head2:
            current.next = head2

        return dummy.next
