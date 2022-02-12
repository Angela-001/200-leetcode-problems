def maxDepth(root):
    if not root:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1 + max(left, right)

# Input - root=[3,9,20,null,null,15,7] --as a binary tree
# Output - 3

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
