"""
This program defines a singly linked list node and implements an
algorithm to reverse a singly linked list in-place.

The reversal is achieved by iteratively updating the `next` pointer of
each node so that it points to the previous node instead of the next one.

Input:
    head : ListNode
        The head of the original singly linked list.

Output:
    ListNode
        The head of the reversed singly linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

