import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

# xy = np.loadtxt("./data/diabetes.csv.gz", delimiter=",", dtype=np.float32)
# x_data = torch.from_numpy(xy[:, 0:-1])
# y_data = torch.from_numpy(xy[:, [-1]])
# print(f"X's shape: {x_data.shape} | Y's shape: {y_data.shape}")


class DiabetesDataset(Dataset):
    """ Diabetes dataset."""

    # Initialize your data, download, etc.
    def __init__(self):
        xy = np.loadtxt("./data/diabetes.csv.gz", delimiter=",", dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:, 0:-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


dataset = DiabetesDataset()
train_loader = DataLoader(dataset=dataset, batch_size=20, shuffle=True, num_workers=0)


class DiabetesLogistic(torch.nn.Module):
    def __init__(self):

        super(DiabetesLogistic, self).__init__()
        self.l1 = torch.nn.Linear(8, 6)  # eight inputs and one output
        self.l2 = torch.nn.Linear(6, 4)
        self.l3 = torch.nn.Linear(4, 1)

        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):

        out1 = self.sigmoid(self.l1(x))
        out2 = self.sigmoid(self.l2(out1))
        pred = self.sigmoid(self.l3(out2))
        return pred


model = DiabetesLogistic()

# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.
criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Training loop
for epoch in range(2):
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, labels = data

        # Forward pass: Compute predicted y by passing x to the model
        y_pred = model(inputs)

        # Compute and print loss
        loss = criterion(y_pred, labels)
        print(f"Epoch {epoch + 1} | Batch: {i+1} | Loss: {loss.item():.4f}")

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
