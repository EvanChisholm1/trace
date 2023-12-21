import torch
import torch.nn as nn

class ResBlock(nn.Module):
    def __init__(self, in_channels=3, out_channels=3, kernel_size=3, stride=1):
        super(ResBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=out_channels)
        self.relu1 = nn.ReLU()

        self.conv2 = nn.Conv2d(in_channels=out_channels, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=out_channels)
        self.relu2 = nn.ReLU()

        self.shortcut = nn.Sequential()
    
    def forward(self, x):
        shortcut = self.shortcut(x)
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.bn1(x)

        x = self.conv2(x)
        x += shortcut
        x = self.relu2(x)
        # x = F.relu(x)
        x = self.bn2(x)


        return x

class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7, stride=2)
        self.bn1 = nn.BatchNorm2d(64)
        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=2)
        self.relu1 = nn.ReLU()
        
        self.res_blocks = nn.Sequential(
            ResBlock(in_channels=64, out_channels=64, kernel_size=3),
            ResBlock(in_channels=64, out_channels=64, kernel_size=3),
            ResBlock(in_channels=64, out_channels=64, kernel_size=3),
        )

        self.gap = nn.AdaptiveAvgPool2d((1, 1))
        self.ff = nn.Linear(in_features=64, out_features=4)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.bn1(x)
        x = self.pool1(x)

        x = self.res_blocks(x)

        x = self.gap(x)
        x = torch.flatten(x, 1)

        return self.ff(x)
    