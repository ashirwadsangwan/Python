import torch
import numpy as np
import matplotlib.pyplot as plt

def view_classify(img, ps, version="MNIST"):
    ''' Function for viewing an image and it's predicted classes.
    '''
    ps = ps.data.numpy().squeeze()

    fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
    ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
    ax1.axis('off')
    ax2.barh(np.arange(10), ps)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    if version == "MNIST":
        ax2.set_yticklabels(np.arange(10))
    elif version == "Fashion":
        ax2.set_yticklabels(['T-shirt/top',
                            'Trouser',
                            'Pullover',
                            'Dress',
                            'Coat',
                            'Sandal',
                            'Shirt',
                            'Sneaker',
                            'Bag',
                            'Ankle Boot'], size='small')
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)




def activation(x):
    """Sigmoid activation function

    Parameters
    ----------
    x : torch.tensor
    """
    return 1 / (1 + torch.exp(-x))

def softmax(x):
    """Softmax activation function

    Parameters
    ----------
    x : torch.tensor
    """
    return torch.exp(x) / torch.sum(torch.exp(x), dim=1).view(-1, 1)


torch.manual_seed(17)
features = torch.randn((1, 5))
weights = torch.rand_like(features)
bias = torch.randn((1, 1))

# The data generated above will help us get the output for a simple framework. This is all random for now, going
# forward we'll start using normal data.

output = activation(torch.sum(features * weights) + bias)  # by using torch.sum
# print(output)
output1 = activation(torch.mm(features, weights.view(5, 1)) + bias)  # changing the weights to be a column vector
# print(output1)

# we can use weights.resize_ method this "_" at the end indicates the operation is happening in inplace. The problem with
# resize method is that if you do not use inplace, you have to make a copy of the tensor.

## Using multi-layer network 
# torch.manual_seed(7)
features = torch.randn(1, 3)
n_input = features.shape[1]
n_hidden = 2
n_output = 1

W1 = torch.randn(n_input, n_hidden)
W2 = torch.randn(n_hidden, n_output)
B1 = torch.randn(1, n_hidden)
B2 = torch.randn(1, n_output)
h = activation(torch.mm(features, W1) + B1)
output = activation(torch.mm(h, W2) + B2)
print(output)



