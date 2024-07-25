import torch
import torch.nn as nn
import torch.optim as optim
import torch.functional as F
from torchvision import datasets,transforms
import numpy as np


# 超参数
input_size = 28
num_classes = 10
num_epoch = 3
batch_size = 64

train_dataset = datasets.MNIST(root='./data',train=True,transform=transforms.ToTensor(),download=True)

test_dataset = datasets.MNIST(root='./data',train = False,transform=transforms.ToTensor())


train_loader = torch.utils.data.DataLoader(dataset = train_dataset,batch_size = batch_size,shuffle = True)
test_loader = torch.utils.data.DataLoader(dataset = test_dataset,batch_size = batch_size,shuffle = True)



class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=5,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.out = nn.Linear(in_features=32*7*7,out_features=10)

    def forward(self,x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0),-1)
        output = self.out(x)
        return output

def accuracy(predictions, labels):
    pred = torch.max(predictions.data, 1)[1]
    rights = pred.eq(labels.data.view_as(pred)).sum()
    return rights, len(labels)

## 实例化

net = CNN()
criterion = nn.CrossEntropyLoss()
opt = optim.Adam(net.parameters(),lr = 0.001)


for epoch in range(num_epoch):
    train_right = []

    for batch_id,(data,target) in enumerate(train_loader):
        net.train()
        output = net(data)
        loss = criterion(output,target)
        opt.zero_grad()
        loss.backward()
        opt.step()
        right = accuracy(output,target)
        train_right.append(right)

        if batch_id %100 == 0:
            net.eval()
            val_right = []

            for (data,target) in test_loader:
                output = net(data)
                right = accuracy(output,target)
                val_right.append(right)

            train_r = (sum([tup[0] for tup in train_right]), sum([tup[1] for tup in train_right]))
            val_r = (sum([tup[0] for tup in val_right]), sum([tup[1] for tup in val_right]))

            print('当前epoch: {} [{}/{} ({:.0f}%)]\t损失: {:.6f}\t训练集准确率: {:.2f}%\t测试集正确率: {:.2f}%'.format(
                epoch, batch_id * batch_size, len(train_loader.dataset),
                       100. * batch_id / len(train_loader),
                loss.data,
                       100. * train_r[0].numpy() / train_r[1],
                       100. * val_r[0].numpy() / val_r[1]))









