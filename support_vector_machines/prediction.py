import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from svm import SVM
from data import Data


def plot_decision_boundary(X,y, model):
    plt.scatter(X[:, 0], X[:, 1], c = y, cmap = "Dark2")
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0],ylim[1], 50))

    xy = np.vstack([xx.ravel(), yy.ravel()]).T

    Z = model.predict(xy).reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.1, cmap='bwr')

    # plt.show()
    plt.savefig("plots/smv_predictions.png")


if __name__ == "__main__":
    data = Data(name = 'iris')
    svm = SVM()
    svm.fit(data.X,data.y)

    data.plot_raw_data()
    plot_decision_boundary(data.X,data.y,svm)

    new_samples = np.array([[0, 0], [4, 4]])
    predictions = svm.predict(new_samples)
    print(predictions)