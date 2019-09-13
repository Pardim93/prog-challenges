def repeatedString(s, n):
    o = 0
    for x in s:
        if 'a' == x:
            o += 1
    return (n//len(s)) * o  +( s[:n%len(s):].count('a'))
