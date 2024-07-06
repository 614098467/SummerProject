import numpy as np
import matplotlib.pylab as plt



h = np.random.randint(0,100,size = (3,4))
f = np.random.randint(0,100,size = (3,5))

# z1 = np.concatenate((h,f),axis=0)
# print(z1)

z2 = np.concatenate((h,f),axis=1)
print(z2.var(axis=0))




