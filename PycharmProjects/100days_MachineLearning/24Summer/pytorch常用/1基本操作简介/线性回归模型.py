
import torch
import torch.nn as nn
import numpy as np
#
# x_value = [i for i in range(11)]
# x_train = np.array(x_value,dtype=np.float32)
# x_train = x_train.reshape(-1,1)
#
# y_value = [2*i+1 for i in x_value]
# y_train = np.array(y_value,dtype=np.float32)
# y_train = y_train.reshape(-1,1)
#
#
# class LinearRegression(nn.Module):
#     def __init__ (self,input_dim,output_dim):
#         super(LinearRegression,self).__init__()
#         self.linear = nn.Linear(input_dim,output_dim)
#
#     def forward(self,x):
#         out = self.linear(x)
#         return out
#
# input_dim = 1
# output_dim = 1
# model = LinearRegression(input_dim,output_dim)
#
# ## 优化器和损失函数
# epochs = 1000
# learningRate = 0.01
# optimizer = torch.optim.SGD(model.parameters(),lr = learningRate)
# criterion = nn.MSELoss()
#
#
# for epoch in range(epochs):
#     epoch += 1
#     inputs = torch.from_numpy(x_train)
#     labels = torch.from_numpy(y_train)
#     # 梯度清零
#     optimizer.zero_grad()
#     # 前向传播
#     ouputs = model(inputs)
#     # 计算损失
#     loss = criterion(ouputs,labels)
#
#     ## 反向传播
#     loss.backward()
#
#     # 更新权重参数
#     optimizer.step()
#
#     if epoch % 50 == 0:
#         print(epoch,loss.item())


## 预测：
# predict = model(torch.from_numpy(x_train).requires_grad_()).data.numpy()
# print(predict)


## 储存模型和保存：

# torch.save(model.state_dict(),'LineraRegressionModel.pkl')

# model.load_state_dict(torch.load('LineraRegressionModel.pkl'))

##  使用GPU进行训练


# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#
# input = torch.from_numpy().to(device)
# labels = torch.from_numpy().to(device)




