import torch
import numpy
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

# now we'll make a bigger structure for computer vision

# define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5),
                                                     (0.5, 0.5, 0.5))
                                ])

# download and load the training data
trainset = datasets.MNIST('MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
images, labels = dataiter.next()

plt.imshow(images[0].numpy().squeeeze(), cmap="Greys_r")
