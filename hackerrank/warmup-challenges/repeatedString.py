def repeatedString(s, n):
    return (n//len(s)) * s.count('a')  +( s[:n%len(s):].count('a'))
