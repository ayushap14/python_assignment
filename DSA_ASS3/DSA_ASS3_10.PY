class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def print_odd_levels(root, level=1):
    if root is None:
        return
    
    if level % 2 == 1:
        print(root.val)
        
    print_odd_levels(root.left, level+1)
    print_odd_levels(root.right, level+1)
