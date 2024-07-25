import numpy as np
import pandas as pd
import datetime

import torch

## 读取数据
features = pd.read_csv('./temps.csv')
##
years = features['year']
month = features['month']
day = features['day']

## 热编码
features = pd.get_dummies(features)


## 取得y
labels = np.array(features['actual'])
## 去掉label取得X
features = features.drop('actual',axis=1) ## drop 中1代表列 0代表行

## 将特征名字转为list方便使用
features_list = list(features.columns)

# 转为np.array 格式
features = np.array(features)

## 归一化处理
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
input_features = std.fit_transform(features)


## 构建网络：
x = torch.tensor(input_features,dtype = float)
y = torch.tensor(labels,dtype=float)

# ## 权重矩阵初始化
# weights  = torch.randn((14,128),dtype=float,requires_grad=True)
# biases = torch.randn(128,dtype=float,requires_grad=True)
# weights2 = torch.randn((128,1),dtype=float,requires_grad=True)
# biases2 = torch.randn(1,dtype=float,requires_grad=True)

learning_rate = 0.001
# losses = []
#
# for i in range(1000):
#     # 计算隐藏层
#     hidden = x.mm(weights) + biases
#     ## 加入激活函数
#     hidden = torch.relu(hidden)
#     #预测结果
#     predictions = hidden.mm(weights2) + biases2
#     ## 计算损失
#     loss = torch.mean((predictions-y)**2)
#     losses.append(loss.data.numpy())
#
#     if i%100 == 0:
#         print('loss:',loss)
#     ## 反向传播
#     loss.backward()
#
#     ## 更新参数
#     weights.data.add_(- learning_rate * weights.grad.data)
#     biases.data.add_(- learning_rate * biases.grad.data)
#     weights2.data.add_(- learning_rate * weights2.grad.data)
#     biases2.data.add_(- learning_rate * biases2.grad.data)
#
#     ## 清零：
#     weights.grad.data.zero_()
#     biases.grad.data.zero_()
#     weights2.grad.data.zero_()
#     biases2.grad.data.zero_()


## 简单的方法构建网络模型：
input_size = input_features.shape[1]
print(input_size)
hidden_size = 128
output_size = 1
batch_size = 16
my_nn  = torch.nn.Sequential(
    torch.nn.Linear(input_size, hidden_size),
    torch.nn.Sigmoid(),
    torch.nn.Linear(hidden_size, output_size)
)
cost = torch.nn.MSELoss(reduction='mean')
optimizer = torch.optim.Adam(my_nn.parameters(),lr = learning_rate)

losses = []
for i in range(1000):
    batch_loss = []
    for start in range(0,len(input_features),batch_size):
        end = start + batch_size if start+batch_size < len(input_features) else len(input_features)
        xx = torch.tensor(input_features[start:end],dtype=torch.float,requires_grad=True)
        yy = torch.tensor(labels[start:end],dtype=torch.float,requires_grad=True)
        predictions = my_nn(xx)
        loss = cost(predictions,yy)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        batch_loss.append(loss.data.numpy())
    if i%100 == 0:
        losses.append(loss.data.numpy())
        print(i,np.mean(batch_loss))


x = torch.tensor(input_features,dtype=torch.float)
predic = my_nn(x)
print(predic)



