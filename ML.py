import torch as t
import torch.nn as nn


class A(nn.Module):
    def __init__(self):
        super(A, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(2, 32, 3, 1, 1),  # 40,60,2
            nn.MaxPool2d(2, 2),  # 40,60,32
            nn.LeakyReLU(),  # 20,30,32

            nn.Conv2d(32, 64, 3, 1, 1),
            nn.MaxPool2d(2, 2),  # 20,30,64
            nn.LeakyReLU(),  # 10,15,64

            nn.Conv2d(64, 128, 3, 1, 1),
            nn.MaxPool2d(2, 2),  # 10,15,128
            nn.LeakyReLU(),  # 5,7,128
        )
        self.fc = nn.Sequential(
            nn.Linear(4480, 1024),
            nn.LeakyReLU(),
            nn.Linear(1024, 128),
            nn.LeakyReLU(),
            nn.Linear(128, 64),
            nn.LeakyReLU(),
            nn.Linear(64, 5),
            nn.Softmax()
        )
        self.opt = t.optim.Adam(self.parameters(), lr=1e-3)
        self.mls = nn.MSELoss()

    def forward(self, inputs):
        out = self.cnn(inputs)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out


class C(nn.Module):
    def __init__(self):
        super(C, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(4805, 4000),
            nn.LeakyReLU(),
            nn.Linear(4000, 1000),
            nn.LeakyReLU(),
            nn.Linear(1000, 500),
            nn.LeakyReLU(),
            nn.Linear(500, 1)
        )
        self.opt = t.optim.Adam(self.parameters(), lr=1e-3)
        self.mls = nn.MSELoss()
