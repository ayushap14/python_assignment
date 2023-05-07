class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.val)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val)

tree = BinaryTree()
tree.add_node(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(1)
tree.add_node(4)
tree.add_node(6)
tree.add_node(8)

tree.inorder_traversal(tree.root) # Output: 1 3 4 5 6 7 8
tree.preorder_traversal(tree.root) # Output: 5 3 1 4 7 6 8
tree.postorder_traversal(tree.root) # Output: 1 4 3 6 8 7 5
