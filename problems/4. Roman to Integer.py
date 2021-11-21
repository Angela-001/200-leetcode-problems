table = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = "III"

ans = 0
for i in range(len(s)-1):
    current_roman = table[s[i]]
    next_roman = table[s[i+1]]
    if current_roman < next_roman:
        ans -= current_roman
    else:
        ans += current_roman

print(ans + table[s[-1]])
