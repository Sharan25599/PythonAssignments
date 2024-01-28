import itertools

def at_least_one_a(n, letters, k):
    a_indices = [i for i, letter in enumerate(letters) if letter == 'a']
    total_combinations = len(list(itertools.combinations(range(n), k)))
    favorable_combinations = len(list(itertools.combinations(range(n), k) for comb in itertools.combinations(range(n), k) if any(i in a_indices for i in comb)))
    probability = favorable_combinations / total_combinations
    return round(probability, 4)