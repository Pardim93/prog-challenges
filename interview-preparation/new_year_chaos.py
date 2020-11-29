def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i, P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1, 0), i):
            if Q[j] > P:
                moves += 1
    print(moves)
