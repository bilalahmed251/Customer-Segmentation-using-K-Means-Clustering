# Customer Segmentation using K-Means
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading Customer Data...")
df = pd.DataFrame(np.random.rand(200, 3), columns=['Age', 'Annual Income', 'Spending Score'])

scaler = StandardScaler()
scaled = scaler.fit_transform(df)

print("Applying K-Means Clustering...")
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled)

print("Segmentation Complete!")
