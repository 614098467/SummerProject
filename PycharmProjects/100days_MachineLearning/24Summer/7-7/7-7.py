import tushare as ts
import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df = DataFrame(data = {
    'items':['apple','banana','grape','watermelon','apple','banana'],
    'price':[5.5,2.3,4.3,3.3,2.8,0.3],
    'color':['red','yellow','purple','green','red','yellow'],
    'weight':[20,10,30,50,20,30]
})

print(df.groupby(by='items')['price'].mean())

def my_mean(s):
    m_sum = 0
    for i in s:
        m_sum += i
    return m_sum/len(s)

print(df.groupby(by='items')['price'].transform(my_mean))
print(df.groupby(by='items')['price'].apply(my_mean))





