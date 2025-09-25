import argparse
import numpy as np
from sklearn.linear_model import LinearRegression
np.set_printoptions(suppress=True)


def main(args):
    arr = np.loadtxt(args.csv,delimiter=",", dtype=str)
    data  = np.array([[float(val) for val in string.split()] for string in arr])
    X = data[:,:-1]
    y = data[:, -1]
    
    model = LinearRegression().fit(X, y)

    r_sq = model.score(X, y)

    print(f"coefficient of determination: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linear Regression over a csv")

    parser.add_argument("-csv", "--csv", type = str, help = "File name of a csv")

    args = parser.parse_args()
    main(args = args)