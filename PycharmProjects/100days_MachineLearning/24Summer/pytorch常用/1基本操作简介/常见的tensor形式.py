
import torch
from torch import tensor
## 0:scalar
## 1:vector
## 2:matrix
## 3:n-dimensional tensor

x = tensor(42)

print(x)
print(x.item())
print(x.dim())
print(x.size())


y = tensor([0,1,2])
print(y)
print(y.dim())
print(y.size())
