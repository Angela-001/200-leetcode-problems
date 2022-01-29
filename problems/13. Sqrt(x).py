def mySqrt(x):
    left_index = 0
    right_index = x

    while left_index < right_index:
        mid = (left_index + right_index) // 2

        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        if mid * mid > x:
            right_index = mid
        else:
            left_index = mid + 1

    return x

print(mySqrt(67))

# https://leetcode.com/problems/sqrtx/
