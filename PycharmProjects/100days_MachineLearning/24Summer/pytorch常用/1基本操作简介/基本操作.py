import  numpy as np
import torch

## 创建矩阵
x = torch.empty(5,3)

## 基本计算方法
y = torch.rand(5,3)

# print(x+y)
# print(y.size())
# print(x)

## view操作改变矩阵纬度
z = y.view(15)
z2 = y.view(-1,3)


## numpy 和 tensor 格式互换
z_numpy = z2.numpy()

a = np.random.randint(0,100,(5,5))
print(a)

a_tensor  = torch.from_numpy(a)
print(a_tensor)
