"""
This function checks whether a singly linked list is a palindrome.

Input:
    head : ListNode
        The head of the singly linked list.

Output:
    bool
        True if the linked list is a palindrome, False otherwise.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    values = []

    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]
