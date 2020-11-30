def breakingRecords(scores):
    min_value = max_value = scores[0]
    min_count = max_count = 0

    for score in scores[1:]:
        if(score > max_value):
            max_value = score
            max_count = max_count + 1
        elif(score < min_value):
            min_value = score
            min_count = min_count + 1

    return [max_count, min_count]


print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
