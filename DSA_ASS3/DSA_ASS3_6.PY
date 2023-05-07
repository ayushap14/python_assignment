class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    def is_leaf(node):
        return node is not None and node.left is None and node.right is None
    
    def dfs(node, is_left):
        nonlocal total
        if node is None:
            return
        if is_leaf(node) and is_left:
            total += node.val
        dfs(node.left, True)
        dfs(node.right, False)

    total = 0
    dfs(root, False)
    return total
