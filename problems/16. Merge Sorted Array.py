def merge(nums1, m, nums2, n):
    if n == 0:
        return

    p = m - 1
    q = n - 1
    r = m + n - 1

    while p != -1 and q != -1:
        if nums1[p] >= nums2[q]:
            nums1[r] = nums1[p]
            p -= 1
        else:
            nums1[r] = nums2[q]
            q -= 1
        r -= 1
    if p != -1:
        nums1[0:r+1] = nums1[0:p+1]
    else:
        nums1[0:r+1] = nums2[0:q+1]

first = [1, 2, 3, 0, 0, 0]
second = [2, 5, 6,]
merge(first, 3, second, 3)

print(first)

# https://leetcode.com/problems/merge-sorted-array/
# DOUBT!!!!
