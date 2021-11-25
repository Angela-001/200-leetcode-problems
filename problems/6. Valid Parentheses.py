s = '()[]{'

checkin = ['()', '{}', '[]']

for i in range(0, len(s)-2, 2):
    first_s = s[i]
    second_s = s[i+1]
    
    if first_s + second_s not in checkin:
        print(False)

if s[-2] + s[-1] not in checkin:
    print(False)

print(True)