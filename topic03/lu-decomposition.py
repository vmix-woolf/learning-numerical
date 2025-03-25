import scipy.linalg
import numpy as np

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)

P, L, U = scipy.linalg.lu(A)

print("L (нижняя треугольная):\n", L)
print("U (верхняя треугольная):\n", U)
