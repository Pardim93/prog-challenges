def birthday(s, d, m):
    index = count = 0
    while(index + m < len(s)):
        value = sum(s[index:index+m])
        if(value == d):
            count = count + 1
        index = index + 1

    return count
