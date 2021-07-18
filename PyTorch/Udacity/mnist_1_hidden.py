import torch
import numpy
from intro import activation, softmax
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

# now we'll make a bigger structure for computer vision

# define a transform to normalize the data
transform = transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

# download and load the training data
trainset = datasets.MNIST("MNIST_data/", download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
images, labels = dataiter.next()

print(type(images))
print(images.shape[0])
print(labels.shape)

# plt.imshow(images[0].numpy().squeeze(), cmap="Greys_r")
# plt.show()

inputs = images.view(images.shape[0], -1)  # gives us the shape (64, 784)

# print(inputs.shape)

# create parameters for the network
w1 = torch.randn(784, 256)
w2 = torch.randn(256, 10)
b1 = torch.randn(256)
b2 = torch.randn(10)

h = activation(torch.mm(inputs, w1) + b1)
out = torch.mm(h, w2) + b2
probabilities = softmax(out)
print(probabilities.shape)
print(probabilities.sum(dim=1))
