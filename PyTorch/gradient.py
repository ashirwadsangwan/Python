from hvplot import hvPlot
import numpy as np
import pandas as pd
import hvplot


def show(plt):
    return hvplot.show(plt)


x_data = [1.0, 2.0, 3.0, 4.0]
y_data = [2.0, 4.0, 6.0, 8.0]
w = 1.0

# our model for the forward pass
def forward(x):
    return x * w


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

def gradient(x,y):
    return 2 * x * (x * w - y)

# Before training
print("Prediction (before training)",  5, forward(5))

# Training loop
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        # Compute derivative w.r.t to the learned weights
        # Update the weights
        # Compute the loss and print progress
        grad = gradient(x_val, y_val)
        w = w - 0.01 * grad
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        l = loss(x_val, y_val)
    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))

# After training
print("Predicted score (after training)",  "4 hours of studying: ", forward(5))
