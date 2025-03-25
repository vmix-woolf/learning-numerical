import numpy as np

def gauss_elimination(A):
    A = A.astype(float)  # Преобразуем в float для деления
    n = A.shape[0]

    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    return A

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

U = gauss_elimination(A)
print("Верхняя треугольная матрица:\n", U)


U = np.triu(A)  # Выделяет верхнюю треугольную часть матрицы
print(U)
