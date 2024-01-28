import numpy as np

def calculate_floor_ceil_rint(input_numbers):

    np.set_printoptions(legacy='1.13')  # Set NumPy print options

    arr = np.array(input_numbers, dtype=float)
    floored_values = np.floor(arr)
    ceiled_values = np.ceil(arr)
    rounded_values = np.rint(arr)
    print(ceiled_values)
    return floored_values, ceiled_values, rounded_values