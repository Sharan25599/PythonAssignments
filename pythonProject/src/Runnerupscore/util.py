def find_second_highest(n, arr):

    sorted_scores = sorted(set(arr), reverse=True)

    if len(sorted_scores) > 1:
        return sorted_scores[1]
    else:
        return None
