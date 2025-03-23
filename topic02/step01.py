import numpy as np

# Приклад матриці
# matrix_a = np.array([[1, 2, 3],
#                     [4, 5, 6]])

matrix_a = np.array([[4, 0],
[3, -5]])

# Обчислення транспонованої матриці
matrix_a_transposed = np.transpose(matrix_a)# або matrix_a.T

# Обчислення добутку матриці на її транспоновану
result = np.dot(matrix_a, matrix_a_transposed) # або matrix_a @ matrix_a_transposed

# Виведення результату
print("Матриця A:")
print(matrix_a)

print("\nТранспонована матриця A:")
print(matrix_a_transposed)

print("\nДобуток матриці A на її транспоновану:")
print(result)

# step02
# Обчислення власних векторів та власних значень
eigenvalues, eigenvectors = np.linalg.eig(result)

# Виведення результату
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# step03
# Отримання індексів, які відсортовують масив за першим стовпцем
sorted_indices = np.argsort(eigenvectors[:, 0])

V = eigenvectors[sorted_indices]

# Виведення результату
print("Output array:")
print(eigenvectors)

print("\nMatrix V:")
print(V)

# step04
# Створення діагонального масиву
Sigma = np.diag(sorted(eigenvalues, reverse=True))
Sigma = np.sqrt(Sigma)
print("\nMatrix Σ:")
print(Sigma)
