import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

data = pd.read_csv('Mall_Customers.csv')
X = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Perform hierarchical clustering using Euclidean distance and ward linkage
linked = hierarchy.linkage(X, method='ward')

# Create a dendrogram
plt.figure(figsize=(10, 5))
dendrogram = hierarchy.dendrogram(linked, orientation='top', labels=data['CustomerID'].tolist(),
                                  distance_sort='descending', show_leaf_counts=True)

plt.xlabel('Customer IDs')
plt.ylabel('Distance')
plt.title('Hierarchical Clustering Dendrogram')
plt.show()
