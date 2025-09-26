import numpy as np
import csv
import matplotlib.pyplot as plt


input_txt = "/home/arpg-miles/code/projectsMLAI/data/sonar.all-data.txt"
output_csv = "/home/arpg-miles/code/projectsMLAI/data/sonar.all-data.csv"


delimiter = ","   # "\t" for tab, " " for space, "," for comma, "|" for pipe

with open(input_txt, "r") as txt_file, open(output_csv, "w", newline="") as csv_file:
    reader = csv.reader(txt_file, delimiter=delimiter)
    writer = csv.writer(csv_file)

    for row in reader:
        if row:
            last_val = row[-1].strip()
            if last_val == "M":
                row[-1] = "0"
            elif last_val == "R":
                row[-1] = "1"
        writer.writerow(row)


data = np.genfromtxt(output_csv, delimiter=',')
np.random.shuffle(data)

X = data[:, :-1]
y = data[:, -1]

def plot_raw_data(X, y,  plot_name,row_num1 = 0, row_num2 = 0 ):
    plt.scatter(X[:, row_num1], X[:, row_num2], c = y, cmap = 'Dark2')
    
    # plt.show()
    plt.savefig(f"plots/{plot_name}.png")


plot_raw_data(X,y,"playground", 2,3)


# PCA
X_normalized = X - np.mean(X, axis=0)
covariance_matrix = np.cov(X_normalized, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
k = 2  # Example: choose 2 principal components
projection_matrix = sorted_eigenvectors[:, :k]
transformed_data = np.dot(X_normalized, projection_matrix)

plot_raw_data(transformed_data, y, "PCA_playground")
