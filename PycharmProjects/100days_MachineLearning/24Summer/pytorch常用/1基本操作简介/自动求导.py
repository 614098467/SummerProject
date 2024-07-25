

import torch

# 方法1:
x = torch.randn(3,4,requires_grad=True)

w = torch.randn(4,3,requires_grad=True)

b = torch.randn(3,3,requires_grad=True)

y = torch.matmul(x,w) + b

y.backward(torch.ones_like(y),retain_graph = True)

print(x.grad)
















