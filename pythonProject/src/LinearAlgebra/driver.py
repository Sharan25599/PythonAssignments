from util import calculate_rounded_determinant

import numpy as np
my_matrix = np.array([[1, 2, -1], [3, 0, 4], [-2, 1, 5]])  # Sample matrix
rounded_det = calculate_rounded_determinant(my_matrix)
print(rounded_det)