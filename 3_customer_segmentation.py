# Advanced Customer Segmentation using K-Means and PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import joblib

print("Loading Customer Data for Advanced Segmentation...")
df = pd.DataFrame(np.random.rand(300, 5), columns=['Age', 'Income', 'SpendingScore', 'LoyaltyPoints', 'Visits'])

scaler = StandardScaler()
scaled = scaler.fit_transform(df)

print("Applying PCA for Dimensionality Reduction...")
pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaled)

print("Finding optimal clusters using Silhouette Score...")
best_score = -1
best_k = 2
for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(scaled)
    score = silhouette_score(scaled, labels)
    if score > best_score:
        best_score = score
        best_k = k

print(f"Optimal Clusters Found: {best_k}")
final_kmeans = KMeans(n_clusters=best_k, random_state=42)
df['Cluster'] = final_kmeans.fit_predict(scaled)

print("Generating PCA 2D Scatter Plot for Clusters...")
plt.figure(figsize=(10,6))
sns.scatterplot(x=pca_features[:,0], y=pca_features[:,1], hue=df['Cluster'], palette='viridis')
plt.title('Customer Segments (PCA Projection)')
plt.savefig('customer_segments_pca.png')
plt.close()

joblib.dump(final_kmeans, 'kmeans_model.pkl')
print("Advanced Segmentation Pipeline Complete!")
