import numpy as np
import numpy.linalg as LA

apmat = np.array([[1 , 2 ],[ 1 , 6]])
apvec = np.array([5 , 9 ]).reshape(-1,1)
print(LA.solve(apmat,apvec))
