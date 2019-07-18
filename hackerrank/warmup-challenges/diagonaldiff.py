def diagonalDifference(arr):
    return abs(sum([line[index]-line[-(index+1)]for index,line in enumerate(arr) ] ))
