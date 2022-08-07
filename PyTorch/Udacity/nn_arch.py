from torch import nn
import torch.nn.functional as F


class Network(nn.Module):
    def __init__(self):
        super().__init__()

        # Input to hidden layer linear transformation
        self.hidden = nn.Linear(784, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        """Applies the forward pass of the network"""

        # Hidden layer with sigmoid activation
        x = F.sigmoid(self.hidden(x))
        # Output layer with softmax activation
        prob = F.softmax(self.output(x), dim=1)

        return prob
