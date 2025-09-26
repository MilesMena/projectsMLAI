import numpy as np
import matplotlib.pyplot as plt

def plot_raw_data(X, y,  plot_name,row_num1 = 0, row_num2 = 0 ):
    plt.scatter(X[:, row_num1], X[:, row_num2], c = y, cmap = 'Dark2')
    
    # plt.show()
    plt.savefig(f"plots/{plot_name}.png")




# plot_raw_data(data1[:,:2], data1[:,2], plot_name="normal")

# Separate x and y
def plot_mesh_grid(data, plot_name):
    x = data[:,0]
    y = data[:, 1]
    targets = data[:,2]

    # Create a mesh grid (for example, covering min to max range)
    x_grid = np.linspace(min(x) - 1, max(x) + 1, 50)
    y_grid = np.linspace(min(y) - 1, max(y) + 1, 50)
    X, Y = np.meshgrid(x_grid, y_grid)

    # Plot scatter points on top of mesh grid
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c=targets, cmap = "Dark2", label="Points")
    plt.plot(X, Y*0, alpha=0)  # this ensures mesh grid is considered

    # Plot the grid
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points on Mesh Grid")
    plt.legend()
    plt.savefig(f"plots/{plot_name}.png")


size = 300
zeros = np.zeros((size,1))
ones = np.ones((size,1))
d1_mean = 1
d1_var= 2
d2_mean = 10
d2_var = 2
data1 = np.hstack((np.random.normal(d1_mean,d1_var,(size, 2)),zeros))
data2 = np.hstack((np.random.normal(d2_mean,d2_var,(size, 2)),ones))
print(data1.size, data2.size)
data = np.vstack((data1, data2))


plot_mesh_grid(data, "normal_mesh")