import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


class Data:
    def __init__(self, name = "iris"):
        if name == "iris":
            self.raw_data = load_iris()
            self.X = self.raw_data.data[:, :2]
            self.y = np.where(self.raw_data.target == 0, -1, 1)
        elif name == "random":
            size = 300
            zero_size = (int(2 * size / 3),1)
            one_size = (int(size /3), 1)
            targets = np.vstack((np.ones(one_size), np.zeros(zero_size)))
            self.raw_data = np.hstack((np.random.rand(size,2), targets))

            self.X = self.raw_data[:, :2]
            self.y = np.where(self.raw_data[:, 2] <= 0, -1, 1)
        else:
            print("WARNING: no self.raw_data")

        
            

    def plot_raw_data(self):
        plt.scatter(self.X[:, 0], self.X[:, 1], c = self.y, cmap = 'Dark2')
        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')
        plt.title('Iris Dataset (Setosa vs. Non-Setosa)')
        # plt.show()
        plt.savefig("plots/raw_data.png")

