import torch
import numpy as np

# Tensor: Multidimensional matrix containing elements of single datatype
arr = np.array([1, 2, 3, 4, 5])
# converting numpy to pytorch tensor

tensor = torch.from_numpy(
    arr
)  # it creates a direct link to numpy array if the array is changes so will the tensor.
print(tensor)
print(type(tensor))


# we don't want any dependency on numpy so we can do the following
import torch
import numpy as np

# Tensor: Multidimensional matrix containing elements of single datatype
arr = np.array([1, 2, 3, 4, 5])
# converting numpy to pytorch tensor

tensor = torch.from_numpy(
    arr
)  # it creates a direct link to numpy array if the array is changes so will the tensor.
print(tensor)
print(type(tensor))


# we don't want any dependency on numpy so we can do the following

tensor2 = torch.tensor(arr)
arr[0] = 23
print(tensor)
print(
    tensor2
)  # so we can see that it doesn't copy the new change in the numpy array here.
print(tensor2.dtype)
