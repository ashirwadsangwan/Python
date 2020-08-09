from abc import ABC

import torch
from torch.autograd import Variable

x_data = Variable(torch.tensor([[1.0], [2.0], [3.0], [4.0]]))
y_data = Variable(torch.tensor([[2.0], [4.0], [6.0], [8.0]]))


class LinearRegression(torch.nn.Module, ABC):
    def __init__(self):

        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(1, 1)  # one input and one output

    def forward(self, x):
        return self.linear(x)  # y_pred // linear computes the y_pred for us


# Our model
model = LinearRegression()

# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.

criterion = torch.nn.MSELoss(reduction="sum")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop

for epoch in range(1000):
    # forward pass: compute y_pred by passing x to the model
    y_pred = model(x_data)

    # Compute the loss
    loss = criterion(y_pred, y_data)
    print(f"Epoch: {epoch} | Loss: {loss.item()} ")

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# After training
hour_var = torch.tensor([[5.0]])
y_pred = model(hour_var)
print("Prediction (after training)", 5, model(hour_var).data[0][0].item())
