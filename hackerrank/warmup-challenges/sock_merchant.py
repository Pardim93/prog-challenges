
def sockMerchant(n ,ar ):
    ar.sort()
    i = s = 0
    while i < n :
        c = j = 0
        while j < n: 
            if i == j:
                break  
            if ar[i] == ar[j]:
                c += 1
                i = j 
            j += 1
        s += c // 2   
        i += 1          
    return s
