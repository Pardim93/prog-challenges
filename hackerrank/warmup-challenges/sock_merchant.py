
def sockMerchant(n ,ar ):
    ar.sort()

    [1 2 3  4 4 4 5]
    i = s = 0
    while i < n :
        c = j = 0
        while j < n: 
            if i == j:
                break
            if j > i and ar[i] != ar[j]:
                break  
            if ar[i] == ar[j]:
                c += 1
                i = j 
            j += 1
        s += c // 2   
        i += 1          
    return s
