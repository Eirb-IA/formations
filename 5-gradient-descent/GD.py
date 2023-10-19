import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)

# Gradient Descent parameters
learning_rate = 0.1
epochs = 100

x_start = 9
y_start = 9
z_start = x_start**2 + y_start**2


x_points = [x_start]
y_points = [y_start]
z_points = [z_start]

# Gradient Descent algorithm
for _ in range(epochs):
    grad_x = 2 * x_start
    grad_y = 2 * y_start
    
    x_start -= learning_rate * grad_x
    y_start -= learning_rate * grad_y
    
    print(x_start, y_start, x_start**2 + y_start**2)
    x_points.append(x_start)
    y_points.append(y_start)
    z_points.append(x_start**2 + y_start**2)

# Plotting the 3D graph
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the true x^2 + y^2 plane
xx, yy = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))
zz_true = xx**2 + yy**2
ax.plot_surface(xx, yy, zz_true, color='b', alpha=0.5, label='True x^2 + y^2 Plane')

# Plot the points
ax.plot(x_points, y_points, z_points, color='g', label='Intermediate Points', linewidth=2, marker='o')
ax.scatter(x_start, y_start, x_start**2 + y_start**2, color='r', s=100, label='Gradient Descent Endpoint')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gradient Descent on x^2 + y^2 Plane')
plt.show()
print("Endpoint after Gradient Descent: (x={}, y={}, z={})".format(x_start, y_start, x_start**2 + y_start**2))
