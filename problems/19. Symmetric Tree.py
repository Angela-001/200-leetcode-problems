def isSymmetric(root):
    def recur(root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        left = recur(root1.left, root2.right)
        right = recur(root1.right, root2.left)

        return left and right

    return recur(root.left, root.right)

# Input - root=[1,2,2,3,4,4,3] --as a binary tree
# Output - True

# https://leetcode.com/problems/symmetric-tree/
