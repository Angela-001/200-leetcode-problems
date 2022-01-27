def addBinary(a, b):
    if len(a) < len(b):
        a = "0" * (len(b)-len(a)) + a
    else:
        b = "0" * (len(a)-len(b)) + b

    result = ""
    carry = 0

    for i in range(len(a)-1, -1, -1):
        x = int(a[i])
        y = int(b[i])

        _sum = x + y + carry

        if _sum == 3:
            result += "1"
            carry = 1
        elif _sum == 2:
            result += "0"
            carry = 1
        elif _sum == 1:
            result += "1"
            carry = 0
        else:
            result += "0"
            carry = 0

    if carry == 1:
        result += "1"

    return result[::-1]

print(addBinary("1010", "1011"))

# https://leetcode.com/problems/add-binary/
