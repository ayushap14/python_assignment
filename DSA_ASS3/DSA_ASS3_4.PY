class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_leaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val)
    else:
        print_leaves(root.left)
        print_leaves(root.right)
