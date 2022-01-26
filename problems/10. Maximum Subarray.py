def maxSubArray(nums):
    ans = nums[0]
    currentSum = 0

    for i in nums:
        currentSum += i

        if ans < currentSum:
            ans = currentSum

        if currentSum < 0:
            currentSum = 0

    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# https://leetcode.com/problems/maximum-subarray/
