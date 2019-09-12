def staircase(n):
    print( '\n'.join([(n-x)*' '+x*'#'  for x in range(1,n+1)]), end ='')
