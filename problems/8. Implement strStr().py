def strStr(haystack, needle):
    if needle == "":
        return 0

    size = len(needle)
        
    for i in range(len(haystack)):
        if haystack[i:i+size] == needle:
            return i
    return -1


print(strStr("hello", "ll"))

# https://leetcode.com/problems/implement-strstr/
