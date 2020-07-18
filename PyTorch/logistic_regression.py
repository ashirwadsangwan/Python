import torch
import math
from torch.nn import functional as F
from torch.autograd import Variable

x_data = Variable(torch.tensor([[1.0], [2.0], [3.0], [4.0]]))
y_data = Variable(torch.tensor([[0.0], [1.0], [0.0], [1.0]]))


class LogisticRegression(torch.nn.Module):
    def __init__(self):

        super(LogisticRegression, self).__init__()
        self.linear = torch.nn.Linear(1, 1)  # one input and one output

    def forward(self, x):
        return F.sigmoid(
            self.linear(x)
        )  # y_pred // linear computes the y_pred and we use
        # sigmoid on it.


# Our model
model = LogisticRegression()

# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.

criterion = torch.nn.BCELoss(reduction="mean")
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
print(f'\nLet\'s predict the hours need to score above 50%\n{"=" * 50}')
hour_var = model(torch.tensor([[1.0]]))
print(
    f"Prediction after 1 hour of training: {hour_var.item():.4f} | Above 50%: {hour_var.item() > 0.5}"
)
hour_var = model(torch.tensor([[7.0]]))
print(
    f"Prediction after 7 hours of training: {hour_var.item():.4f} | Above 50%: { hour_var.item() > 0.5}"
)
