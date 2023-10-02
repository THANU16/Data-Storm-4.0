import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load your dataset (replace 'your_dataset.csv' with your actual data)
data = pd.read_csv('your_dataset.csv')

# Perform feature scaling if necessary
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.show()

# Choose the optimal number of clusters (k) based on the Elbow Method plot
optimal_k = 3  # Adjust this based on your analysis of the Elbow Method

# Perform K-Means clustering with the chosen number of clusters
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(scaled_data)

# Add the cluster labels to your dataset
data['Cluster'] = cluster_labels

# Analyze the clusters and their characteristics
cluster_summary = data.groupby('Cluster').mean()
print(cluster_summary)

# Visualize the clusters (replace 'feature1' and 'feature2' with your actual feature names)
plt.figure(figsize=(10, 8))
sns.scatterplot(x='feature1', y='feature2', hue='Cluster', data=data, palette='Set1', s=100)
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
