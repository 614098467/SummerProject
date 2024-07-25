from pandas import DataFrame
import numpy as np


dic = {
    'alex':[100,50,123],
    'bob':[130,115,133],
    'cici':[120,130,114]
}
dic2 = {
    'alex':[130,90,123],
    'bob':[120,125,133],
    'cici':[110,140,112]
}

qizhong = DataFrame(data = dic,index=['语文','数学','英语'])
qimo = DataFrame(data = dic2,index=['语文','数学','英语'])


## 平均值
mean  = (qizhong + qimo) / 2
print(mean)

## alex 期中数学为0
qizhong.loc['数学','alex'] = 0
print(qizhong)

### bob所有科目期中加100分
qizhong.loc[:,'bob'] += 100
print(qizhong)


### 所有人加10分
qizhong += 10
print(qizhong)

