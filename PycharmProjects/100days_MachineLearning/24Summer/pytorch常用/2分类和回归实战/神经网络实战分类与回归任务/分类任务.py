
from pathlib import Path
import  torch
import pickle
import gzip
import matplotlib.pyplot as plt
import numpy as np
from torch import nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader


DataPath = Path("data")
PATH = DataPath/'mnist'
FILENAME = "mnist.pkl.gz"
print(type(PATH))
with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
    ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")


plt.imshow(x_train[34343].reshape((28,28)),cmap='gray')

x_train,y_train,x_valid,y_valid = map(torch.tensor,
                                      (x_train,y_train,x_valid,y_valid))

number_of_sample,input_size = x_train.shape



class MNist_NN(nn.Module):

    def __init__(self):
        super().__init__()
        self.hidden1 = nn.Linear(784,128)
        self.hidden2 = nn.Linear(128,256)
        self.out = nn.Linear(256,10)

    def forward(self,x):
        x = F.relu(self.hidden1(x))
        x = F.relu(self.hidden2(x))
        x = self.out(x)
        return  x

loss_func = F.cross_entropy
my_nn = MNist_NN()

train_ds = TensorDataset(x_train,y_train)
train_dl = DataLoader(train_ds,batch_size=16,shuffle=True)

valid_ds = TensorDataset(x_train,y_train)
valid_dl = DataLoader(valid_ds,batch_size=32)


def fit(steps,model,loss_func,opt,train_dl,valid_dl):
    for step in range(steps):
        model.train()
        for xb,yb in train_dl:
            loss_batch(model,loss_func,xb,yb,opt)
        model.eval()
        with torch.no_grad():
            losses, nums = zip(
                *[loss_batch(model, loss_func, xb, yb) for xb, yb in valid_dl]
            )
        val_loss = np.sum(np.multiply(losses, nums)) / np.sum(nums)
        print('当前step:'+str(step), '验证集损失：'+str(val_loss))

def get_model():
    model = MNist_NN()
    return model,torch.optim.Adam(model.parameters(),lr = 0.001)

def loss_batch(model,loss_func,xb,yb,opt=None):
    loss = loss_func(model(xb),yb)
    if opt is not None:
        loss.backward()
        opt.step()
        opt.zero_grad()

    return loss.item(),len(xb)

if __name__ == '__main__':
    model,opt = get_model()
    fit(25,model,loss_func,opt,train_dl,valid_dl)


