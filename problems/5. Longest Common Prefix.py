strs = ["flower","flow","flight"]

l = list(zip(*strs))

prefix = ""

for i in l:
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break
print(prefix)