numbers = [-1,0]
target = -1

hashMap = {}

for index, num in enumerate(numbers):
    diff = target - num
    if diff in hashMap:
        print([hashMap[diff]+1, index+1])
    
    hashMap[num] = index