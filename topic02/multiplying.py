from numpy import array

vec = array([3, 5])
scaled_vec = .5 * vec
print(scaled_vec)

# создаем базисную матрицу из векторов î и ĵ
basis = array(
[[3, 0],
[0, 2]]
)
# объявляем вектор v
v = array([1,1])
# создаем новый вектор как сумму скалярных произведений
new_v = basis.dot(v)
print(new_v) # [3 2]
