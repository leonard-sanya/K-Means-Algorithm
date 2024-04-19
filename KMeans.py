
import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, K=5, max_iters=100, plot_steps=False):
       self.K = K
       self.max_iters = max_iters
       self.plot_steps = plot_steps

    def predict(self, X):
      self.X = X
      self.centroids = self.initialize_centroids()

      for i in range(self.max_iters):
          self.clusters = self._create_clusters(self.centroids)
          if self.plot_steps:
              self.plot()
          centroids_old = self.centroids.copy()
          self.centroids = self._get_centroids(self.clusters)
          if self._is_converged(centroids_old, self.centroids):
              break
          if self.plot_steps:
              self.plot()
      return self._get_cluster_labels(self.clusters)


    def initialize_centroids(self):
      idx = np.random.choice(len(self.X), size=self.K, replace=False)
      centroids = self.X[idx]
      return centroids

    def _get_cluster_labels(self, clusters):
      n_samples = self.X.shape[0]
      labels = np.empty(n_samples)
      for cluster_idx, cluster in enumerate(clusters):
          labels[cluster] = cluster_idx
      return labels


    def _create_clusters(self, centroids):
      clusters = [[] for _ in range(self.K)]
      for idx, sample in enumerate(self.X):
          idx_centroid = self._closest_centroid(sample,centroids)
          clusters[idx_centroid].append(idx)

      return clusters



    def _closest_centroid(self, sample, centroids):
      dist = []
      for i in range(len(centroids)):
        dist.append(self.euclidean_distance(sample,centroids[i]))
      closest_index = np.argmin(dist)
      return closest_index

    def euclidean_distance(self,x1, x2):
      return np.sqrt(np.sum((x1 - x2)**2))



    def _get_centroids(self, clusters):
      for cluster_idx, cluster in enumerate(clusters):
          if len(cluster) > 0:
              cluster_mean = np.mean(self.X[cluster],axis=0)

              self.centroids[cluster_idx] = cluster_mean
          else:
              self.centroids[cluster_idx] = self.X[np.random.choice(len(self.X))]
      return self.centroids


    def _is_converged(self, centroids_old, centroids):
      distances = self.euclidean_distance(centroids_old,centroids)
      return np.sum(distances) == 0


    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color="black", linewidth=2)

        plt.show()