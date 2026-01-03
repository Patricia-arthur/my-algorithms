"""
This function removes all nodes from a singly linked list
whose value is equal to a given integer.

Input:
    head : ListNode
        The head of the linked list.
    val : int
        The value to be removed from the list.

Output:
    ListNode
        The head of the modified linked list after removals.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head

    current = dummy

    while current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
