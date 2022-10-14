#Concatenate a and b

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
arr = np.concatenate((a,b))

print("before concatenation")
print("a \n",a)
print("b \n",b)
print("after concatenation \n",arr)
