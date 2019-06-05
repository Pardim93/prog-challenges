
from itertools import groupby

def sockMerchant(n ,ar):
    ar.sort()
    total = 0
    for key, group in groupby(ar, lambda x: int(x)):
        total+= len(list(group)) // 2

    return total
