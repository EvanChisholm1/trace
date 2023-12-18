import torch
import torch.nn as nn

# class SimpleConvNet(nn.Module):
#     def __init__(self):
#         super(SimpleConvNet, self).__init__()

#         # Define the convolutional layers
#         self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=4, stride=1, padding=1)
#         self.relu1 = nn.ReLU()
#         self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

#         self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
#         self.relu2 = nn.ReLU()
#         self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

#         # Define fully connected layers
#         self.fc1 = nn.Linear(111104, 512)  # Adjust the input size based on your image dimensions
#         self.relu3 = nn.ReLU()

#         # Output layer
#         self.fc2 = nn.Linear(512, 4)  # Output 4 logits

#     def forward(self, x):
#         # Input: (batch_size, channels, height, width)
#         # Example: (batch_size, 3, 128, 228)

#         # Convolutional layers
#         x = self.conv1(x)
#         x = self.relu1(x)
#         x = self.pool1(x)

#         x = self.conv2(x)
#         x = self.relu2(x)
#         x = self.pool2(x)

#         # Flatten the output for the fully connected layers
#         x = x.view(x.size(0), -1)

#         # Fully connected layers
#         x = self.fc1(x)
#         x = self.relu3(x)

#         # Output layer
#         x = self.fc2(x)
#         return x


class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()

        # Define the convolutional layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        # Define fully connected layers
        self.fc1 = nn.Linear(222208, 512)  # Adjust the input size based on your image dimensions
        self.relu3 = nn.ReLU()

        # Output layer
        self.fc2 = nn.Linear(512, 4)  # Output 4 logits

    def forward(self, x):
        # Input: (batch_size, channels, height, width)
        # Example: (batch_size, 3, 128, 228)

        # Convolutional layers
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)

        # Flatten the output for the fully connected layers
        x = x.view(x.size(0), -1)

        # Fully connected layers
        x = self.fc1(x)
        x = self.relu3(x)

        # Output layer
        x = self.fc2(x)

        return x

# m = SimpleConvNet()
# m = m.cuda()