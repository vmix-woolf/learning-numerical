import numpy as np

# Создадим одномерный массив (вектор)
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.transpose())

# Создадим двумерный массив (матрицу)
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original matrix:\n {arr2}")
print(f"Transposed matrix:\n {arr2.transpose()} ")

# Создадим трёхмерный массив
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3-dimensional matrix:\n {arr3}")


print(arr1.shape)  # (5,) - одномерный массив из 5 элементов
print(arr2.shape)  # (2, 3) - 2 строки, 3 столбца
print(arr3.shape)  # (2, 2, 2) - трехмерный массив 2x2x2
