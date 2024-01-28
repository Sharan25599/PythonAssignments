import numpy as np
def minAndMax(data):
    min_values = np.min(data, axis=1)

    # Find the maximum of the minimum values
    max_min_sum = np.max(min_values)

    return max_min_sum
