class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(node):
    height = 0
    while node is not None:
        height += 1
        node = node.left
    return height

def sum_of_nodes(root):
    if root is None:
        return 0
    
    height = get_height(root)
    total_nodes = 2**(height+1) - 1
    return root.val * total_nodes
