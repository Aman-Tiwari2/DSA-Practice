class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create nodes
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.right.left.left = TreeNode(8)

root.right.left.left.right = TreeNode(9)




def height_tree(node):
    if node == None:
        return 0
    
    leftHeight = height_tree(node.left)
    rightHeight = height_tree(node.right)
    
    return 1 + max(leftHeight,rightHeight)


print(height_tree(root))

