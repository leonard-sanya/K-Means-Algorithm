# K-Means-Algorithm

KMeans is an unsupervised learning algorithm that groups data into a predefined number of clusters.
It works by assigning each data point to the nearest cluster center. The means of the data points within each cluster are then recalculated, and this process repeats until convergence.

**Centroid Initialization**
- KMeans requires selecting random points as cluster centers (centroids). Centroids are the central points of each cluster, which the KMeans algorithm seeks to optimally place.

- In the context of KMeans, a centroid is essentially the mean of all points belonging to a cluster. Initially, these centroids are selected by some strategy before the iterative process of assigning points and updating centroids begins.
- The simplest and most common method is to randomly select K distinct data points from the dataset to serve as the initial centroids.

**Create Clusters**
- Once initial centroids are set, the algorithm proceeds to assign each data point to the nearest centroid, based on the chosen distance metric, typically Euclidean distance. This assignment step forms the clusters for one iteration of the algorithm.
The create_clusters function is responsible for grouping all the data points into clusters based on which centroid is closest to each point. This is a central step in each iteration of the KMeans algorithm.

# How It Works:

**Initialization of Clusters**

- The function starts by initializing an empty list for each cluster. These lists will hold the indices of the data points that belong to each respective cluster.
Assignment of Points to Clusters:
- It iterates over each data point in the dataset, and for each point, it determines the closest centroid. This decision is made using the _closest_centroid function, which calculates and compares the distances from the current data point to each centroid.
**Calculate Distances**

- Compute the Euclidean distance between the data point and each centroid in the list of centroids.
- Determine the Closest Centroid:
- Identify which centroid has the smallest distance to the data point, which indicates it is the closest.
  
**Update Cluster Memberships**

- Once the closest centroid is identified for a data point, the index of that data point is added to the corresponding cluster.
- The _closest_centroid function calculates the Euclidean distance from a single data point to each centroid and returns the index of the centroid that is closest to that point.
    
## Installation
- Inorder to run this implementation, clone the repository https:

       https://github.com/leonard-sanya/K-Means-Algorithm.git   
      
- Run the K-Means using the following command:

      python Main.py

## License

This project is licensed under the [MIT License](LICENSE.md). Please read the License file for more information.

## Acknowledgments

Feel free to explore each lab folder for detailed implementations, code examples, and any additional resources provided. Reach out to me via [email](lsanya@aimsammi.org) in case of any question or sharing of ideas and opportunities

