import time
import torch
from torch.functional import F
from hvplot import hvPlot
from torch import nn
from torch import optim
from intro import view_classify
import matplotlib.pyplot as plt
from torchvision import datasets, transforms


# now we'll make a bigger structure for computer vision

# define a transform to normalize the data
transform = transform = transforms.Compose([transforms.ToTensor(),
  transforms.Normalize((0.5,), (0.5,))
])

# download and load the training data
trainset = datasets.FashionMNIST("MNIST_data/", download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
images, labels = dataiter.next()

model = torch.nn.Sequential(nn.Linear(784, 128),
                            nn.ReLU(),  # activation function
                            nn.Linear(128, 64),
                            nn.ReLU(),
                            nn.Linear(64, 10),
                            nn.LogSoftmax(dim=1))

criterion = nn.NLLLoss()


# Clear the gradients 
optimizer = optim.SGD(model.parameters(), lr=0.003)

start = time.time()
epochs = 5
for e in range(epochs):
    running_loss = 0
    for images, labels in trainloader:

        # Flatten Images
        images = images.view(images.shape[0], -1)
        optimizer.zero_grad()
        
        output = model.forward(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    else:
        print("Training loss in epoch {} is {}:".format(e ,running_loss/len(trainloader)))
        
print("Time taken for {} epochs is {}:".format(epochs, time.time()-start))

images, labels = next(iter(trainloader))
img = images[12].view(1, 784)

with torch.no_grad():
    logps = model.forward(img)
ps = F.softmax(logps, dim=1)


print(ps)
view_classify(img.view(1, 28, 28), ps, version="Fashion")
plt.show()