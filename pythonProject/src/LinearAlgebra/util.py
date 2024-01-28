import numpy as np

def calculate_rounded_determinant(matrix):
  det_value = np.linalg.det(matrix)
  return round(det_value, 2)