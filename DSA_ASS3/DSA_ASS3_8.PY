class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def count_subtrees_with_sum_x(root, x):
    count = 0
    
    def postorder(node):
        nonlocal count
        if node is None:
            return 0
        
        left_sum = postorder(node.left)
        right_sum = postorder(node.right)
        subtree_sum = node.val + left_sum + right_sum
        
        if subtree_sum == x:
            count += 1
        
        return subtree_sum
    
    postorder(root)
    return count
