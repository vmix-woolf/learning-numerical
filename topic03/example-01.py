import numpy as np


# Дано вектори
# а1=(1;2;−3); а2=(−1;2;4); a3=(1;6;−2)
A = np.array([
    [1, 2, -3],
    [-1, 2, 4],
    [1, 6, -2],
])

At = np.array(A).transpose()
rank_A = np.linalg.matrix_rank(A)
print(At, "\n", rank_A)
