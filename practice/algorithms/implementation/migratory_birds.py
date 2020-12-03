def migratoryBirds(arr):
    birds_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for bird in arr:
        birds_dict[bird] = birds_dict[bird] + 1

    return(max(birds_dict.items(), key=lambda x: x[1])[0])
