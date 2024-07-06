from pandas import Series
import numpy as np

s1 = Series(data=[1,2,3,'four'],index=['a', 'b', 'c','d'])
print(s1)

s2 = Series(data = np.random.randint(0,100,size=(3,)))
print(s2)


dic = {'语文':100,'数学':200,'英语':1000}
s3  = Series(data=dic)
print(s3)