def searchInsert(nums, target):
    left_index = 0
    right_index = len(nums) - 1

    mid_index = (left_index + right_index) // 2

    while left_index <= right_index:
        mid_number = nums[mid_index]

        if mid_number > target:
            right_index = mid_index - 1
        elif mid_number < target:
            left_index = mid_index + 1
        else:
            return mid_index

# https://leetcode.com/problems/search-insert-position/
