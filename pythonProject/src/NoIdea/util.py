def calculate_happiness(n, m, arr, set_A, set_B):
    happiness = 0
    for num in arr:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1
    return happiness
