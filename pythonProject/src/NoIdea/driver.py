from util import calculate_happiness
n, m = 3, 2
arr = [1, 5, 3]
set_A = {3, 1}
set_B = {5, 7}
final_happiness = calculate_happiness(n, m, arr, set_A, set_B)
print(final_happiness)