"""
This function flattens a binary tree into a linked list in-place.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    if not root:
        return
    flatten(root.left)

    left_subtree = root.left
    right_subtree = root.right

    root.left = None
    root.right = left_subtree

    current = root
    while current.right:
        current = current.right
    current.right = right_subtree
