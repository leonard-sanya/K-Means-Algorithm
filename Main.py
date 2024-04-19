import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from KMeans import KMeans


# Generate sample data
for i in range(10):
  X, y = make_blobs(centers= 3 , n_samples= 500 , n_features= 2, shuffle= True , random_state= 42)


print("Data shape:", X.shape)

print("Number of clusters:", len(np.unique(y)))


# Plot
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', edgecolor='k', s=50)
plt.title('Visualizing Blob Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

X, y = make_blobs(centers= 3 , n_samples= 500 , n_features= 2, shuffle= True , random_state= 42)
clusters = len(np.unique(y))

model = KMeans(K = clusters, max_iters = 150, plot_steps = True)


def main():
    model.predict(X)
         
if __name__ == "__main__":
  main()