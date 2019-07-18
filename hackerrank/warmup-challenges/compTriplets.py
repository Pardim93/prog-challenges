def compareTriplets(a, b):
    res = [0,0]
    for ita, itb in zip(a, b):
        if ita > itb:
            res[0] += 1
        elif itb > ita:
            res[1] += 1
    return res
