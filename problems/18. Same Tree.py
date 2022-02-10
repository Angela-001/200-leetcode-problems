def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    left_check = self.isSameTree(p.left, q.left)
    right_check = self.isSameTree(p.right, q.right)

    return left_check and right_check

# Input - p=[1,2,3], q=[1,2,3] --as binary trees
# Output - True

# https://leetcode.com/problems/same-tree/
