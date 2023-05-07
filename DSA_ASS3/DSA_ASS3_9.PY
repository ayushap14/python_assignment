class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def max_level_sum(root):
    if root is None:
        return 0
    
    max_sum = float('-inf')
    max_level = 0
    queue = [root]
    
    level = 1
    while queue:
        level_sum = 0
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
            
        level += 1
        
    return max_level
