import torch


def activation(x):
    """Sigmoid activation function

    Parameters
    ----------
    x : torch.tensor
    """
    return 1 / (1 + torch.exp(-x))


torch.manual_seed(17)
features = torch.randn((1, 5))
weights = torch.rand_like(features)
bias = torch.randn((1, 1))

# The data generated above will help us get the output for a simple framework. This is all random for now, going
# forward we'll start using normal data.

output = activation(torch.sum(features * weights) + bias)  # by using torch.sum
print(output)
output1 = activation(torch.mm(features, weights.view(5, 1)) + bias)
print(output1)

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
