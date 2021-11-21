numbers = [2,7,11,15]
target = 9

hashMap = {}
for index, num in enumerate(nums):
    diff = target - num
    if diff in hashMap:
        print([hashMap[diff], index])

    hashMap[num] = index