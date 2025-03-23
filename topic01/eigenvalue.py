import numpy as np
from numpy import linalg as LA

user_input = np.array([[2,2],[8,2]])

eig_val, eig_vect = LA.eig(user_input)

print(eig_val)
print(eig_vect)