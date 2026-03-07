import numpy as np
import matplotlib.pyplot as plt

# Define MSE loss function (simple quadratic function)
def loss_function(x, y):
    return x**2 + y**2

# Gradient of loss function
def gradient(x, y):
    dx = 2*x
    dy = 2*y
    return dx, dy

# Starting point
x, y = 4, 4

# Learning rate
learning_rate = 0.2

# Store path
x_path = [x]
y_path = [y]

# Gradient descent iterations
for i in range(15):
    dx, dy = gradient(x, y)
    x = x - learning_rate * dx
    y = y - learning_rate * dy
    x_path.append(x)
    y_path.append(y)

# Create contour plot
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = loss_function(X, Y)

plt.figure(figsize=(8,6))
plt.contour(X, Y, Z, levels=20)

# Plot optimization path
plt.plot(x_path, y_path, marker='o', color='red')

plt.title("Gradient Descent Optimization Path Minimizing MSE")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")

plt.show()
