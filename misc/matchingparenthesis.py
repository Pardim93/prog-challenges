s = str(input())
c = 0
for x in s:
    if x == '(':
        c = c + 1
    elif x == ')':
        c = c - 1
    if c == -1:
        break
print(str(c == 0).lower())
