import numpy as np

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)

Q, R = np.linalg.qr(A)

print("Q (ортогональная матрица):\n", Q)
print("R (верхняя треугольная матрица):\n", R)
