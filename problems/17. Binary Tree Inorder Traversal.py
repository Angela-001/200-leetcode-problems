def inorderTraversal(root):
    elements = []

    if not root:
        return elements

    if root.left:
        elements += self.inorderTraversal(root.left)

    elements.append(root.val)

    if root.right:
        elements += self.inorderTraversal(root.right)

    return elements

# Input - [1,null,2,3] --as a binary tree
# Output - [1,2,3]

# https://leetcode.com/problems/binary-tree-inorder-traversal/
