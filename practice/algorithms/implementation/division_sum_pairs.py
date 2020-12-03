def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if (i != j):
                if ((ar[j]+ar[i]) % k == 0):
                    count = count + 1
    print(int(count/2))


divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
